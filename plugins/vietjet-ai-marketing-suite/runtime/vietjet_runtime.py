#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, re, sys, unicodedata, urllib.request, urllib.error
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FRONT = re.compile(r'^---\n(.*?)\n---\n', re.S)

def suite_version(root: Path = ROOT) -> str:
    try:
        return str(json.loads((root/'.codex-plugin'/'plugin.json').read_text(encoding='utf-8'))['version'])
    except (OSError, KeyError, json.JSONDecodeError):
        return 'unknown'

def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding='utf-8')
    m = FRONT.match(text)
    meta: dict[str, Any] = {}
    body = text
    if m:
        body = text[m.end():]
        for raw in m.group(1).splitlines():
            if ':' not in raw: continue
            k, v = raw.split(':', 1)
            v = v.strip().strip('"')
            if v.lower() in {'true','false'}: value: Any = v.lower() == 'true'
            else: value = v
            meta[k.strip()] = value
    return meta, body

@dataclass
class Item:
    name: str
    kind: str
    path: str
    description: str = ''
    version: str = ''
    role: str = ''


REQUIRED_MISSION_FIELDS = (
    'mission_id', 'objective', 'decision_required', 'market',
    'market_scope_type', 'risk_tier',
)
MARKET_SCOPE_TYPES = {'operating_entity', 'point_of_sale', 'source_market', 'route_corridor'}
RISK_TIERS = {'low', 'medium', 'high', 'critical'}


@dataclass
class Mission:
    mission_id: str
    objective: str
    decision_required: str
    market: str
    market_scope_type: str
    risk_tier: str
    operating_entity: str = ''
    route_or_corridor: str = ''
    deadline: str = ''
    requested_outputs: list[str] | None = None
    evidence_refs: list[str] | None = None
    constraints: list[str] | None = None

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> 'Mission':
        missing = [key for key in REQUIRED_MISSION_FIELDS if not raw.get(key)]
        if missing:
            raise ValueError('missing mission fields: ' + ', '.join(missing))
        unknown = sorted(set(raw) - set(cls.__dataclass_fields__))
        if unknown:
            raise ValueError('unknown mission fields: ' + ', '.join(unknown))
        if raw['market_scope_type'] not in MARKET_SCOPE_TYPES:
            raise ValueError('invalid market_scope_type: ' + str(raw['market_scope_type']))
        if raw['risk_tier'] not in RISK_TIERS:
            raise ValueError('invalid risk_tier: ' + str(raw['risk_tier']))
        if raw['market_scope_type'] == 'route_corridor' and not raw.get('route_or_corridor'):
            raise ValueError('route_or_corridor is required for route_corridor missions')
        if len(str(raw['objective']).strip()) < 10:
            raise ValueError('objective must be at least 10 characters')
        return cls(**raw)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

class Registry:
    def __init__(self, root: Path = ROOT):
        self.root = root
        self.agents: dict[str, Item] = {}
        self.skills: dict[str, Item] = {}
        self.rules: dict[str, Item] = {}
        self.plugins: dict[str, dict[str, Any]] = {}
        self.reload()

    def reload(self):
        self.agents.clear(); self.skills.clear(); self.rules.clear(); self.plugins.clear()
        for p in sorted((self.root/'agents').glob('*.md')):
            m,_ = parse_frontmatter(p); name=m.get('name') or p.stem
            self.agents[name] = Item(name,'agent',str(p.relative_to(self.root)),m.get('description',''),str(m.get('version','')),m.get('role',''))
        for p in sorted((self.root/'skills').glob('*/SKILL.md')):
            m,_=parse_frontmatter(p); name=m.get('name') or p.parent.name
            self.skills[name] = Item(name,'skill',str(p.relative_to(self.root)),m.get('description',''),str(m.get('version','')))
        for p in sorted((self.root/'rules').glob('*.md')):
            m,_=parse_frontmatter(p); name=p.stem
            self.rules[name] = Item(name,'rule',str(p.relative_to(self.root)),m.get('title',''),str(m.get('version','')))
        for p in sorted((self.root/'plugins').glob('*.json')):
            try:
                d=json.loads(p.read_text(encoding='utf-8')); self.plugins[d['name']]=d
            except Exception: pass

    def manifest(self):
        return {
            'suite':'vietjet-ai-marketing-suite','version':suite_version(self.root),
            'agents':[asdict(x) for x in self.agents.values()],
            'skills':[asdict(x) for x in self.skills.values()],
            'rules':[asdict(x) for x in self.rules.values()],
            'plugins':list(self.plugins.values()),
        }

    def resolve_ref(self, ref: str) -> Path:
        p=(self.root/ref.rstrip('/')).resolve()
        if p.is_dir(): p=p/'SKILL.md'
        if self.root.resolve() not in p.parents and p != self.root.resolve(): raise ValueError('path outside suite')
        if not p.exists(): raise FileNotFoundError(ref)
        return p

    def preload_for_agent(self, agent: str) -> list[Path]:
        item=self.agents[agent]; p=self.root/item.path
        txt=p.read_text(encoding='utf-8')
        refs=re.findall(r'`((?:rules|skills|schemas)/[^`\s]+)`', txt)
        out=[]
        for ref in refs:
            ref=ref.rstrip('.,;')
            try: out.append(self.resolve_ref(ref))
            except FileNotFoundError: pass
        # all always_on rules are mandatory baseline
        for ri in self.rules.values():
            rp=self.root/ri.path
            meta,_=parse_frontmatter(rp)
            if meta.get('trigger')=='always_on' and rp not in out: out.insert(0,rp)
        # preserve order and unique
        seen=set(); uniq=[]
        for x in out:
            if x not in seen: seen.add(x); uniq.append(x)
        return uniq

    def build_prompt(self, agent: str, task: str) -> str:
        if agent not in self.agents: raise KeyError(agent)
        chunks=['# VIETJET AI MARKETING SUITE — RUNTIME CONTEXT']
        for p in self.preload_for_agent(agent):
            chunks += [f'\n## PRELOADED: {p.relative_to(self.root)}\n', p.read_text(encoding='utf-8')]
        ap=self.root/self.agents[agent].path
        chunks += [f'\n## ACTIVE AGENT: {agent}\n', ap.read_text(encoding='utf-8'), '\n## USER TASK\n', task]
        return '\n'.join(chunks)


class TeamRouter:
    """Deterministic, explainable routing. It selects roles; it grants no authority."""

    ORDER = [
        'vietjet_cmo_orchestrator',
        'vietjet_martech_ai_operations',
        'vietjet_market_intelligence',
        'vietjet_bi_data_analyst',
        'vietjet_market_pod_lead',
        'vietjet_group_brand_portfolio_strategist',
        'vietjet_revenue_management',
        'vietjet_finance_cost_controller',
        'vietjet_flight_ops_network_planner',
        'vietjet_trade_distribution_sales',
        'vietjet_customer_journey_experience',
        'vietjet_performance_growth',
        'vietjet_creative_studio',
        'vietjet_crm_skyjoy_ancillary',
        'vietjet_content_organic_discovery',
        'vietjet_pr_social_crisis',
        'vietjet_marketing_science_experimentation',
        'vietjet_legal_regulatory_compliance',
    ]
    WAVE = {
        'vietjet_martech_ai_operations': '0_CONTROL',
        'vietjet_market_intelligence': '1_SENSE',
        'vietjet_bi_data_analyst': '1_SENSE',
        'vietjet_market_pod_lead': '1_SENSE',
        'vietjet_group_brand_portfolio_strategist': '2_CHOOSE',
        'vietjet_revenue_management': '2_CHOOSE',
        'vietjet_finance_cost_controller': '2_CHOOSE',
        'vietjet_flight_ops_network_planner': '2_CHOOSE',
        'vietjet_trade_distribution_sales': '2_CHOOSE',
        'vietjet_customer_journey_experience': '3_DESIGN',
        'vietjet_performance_growth': '3_DESIGN',
        'vietjet_creative_studio': '3_DESIGN',
        'vietjet_crm_skyjoy_ancillary': '3_DESIGN',
        'vietjet_content_organic_discovery': '3_DESIGN',
        'vietjet_pr_social_crisis': '3_DESIGN',
        'vietjet_marketing_science_experimentation': '4_ASSURE',
        'vietjet_legal_regulatory_compliance': '4_ASSURE',
    }
    REASONS = {
        'vietjet_cmo_orchestrator': 'Locks the mission, dependencies, decision record and human gates.',
        'vietjet_martech_ai_operations': 'Checks identity, tool scopes, audit, approval, rollback and kill-switch controls.',
        'vietjet_market_intelligence': 'Builds current market and competitor evidence before choices are made.',
        'vietjet_bi_data_analyst': 'Defines aggregate data inputs, baselines and diagnostic reporting.',
        'vietjet_market_pod_lead': 'Localizes the plan for entity, POS, source market or corridor with local review.',
        'vietjet_group_brand_portfolio_strategist': 'Sets customer job, value proposition, brand invariants and portfolio role.',
        'vietjet_revenue_management': 'Owns fare and inventory decision inputs.',
        'vietjet_finance_cost_controller': 'Tests contribution economics and sensitivity.',
        'vietjet_flight_ops_network_planner': 'Checks route, fleet, schedule and operating assumptions.',
        'vietjet_trade_distribution_sales': 'Tests channel, partner and distribution economics.',
        'vietjet_customer_journey_experience': 'Checks promise-to-delivery, accessibility and recovery journeys.',
        'vietjet_performance_growth': 'Designs measurable paid demand capture without activating spend.',
        'vietjet_creative_studio': 'Creates governed asset concepts from an approved value proposition.',
        'vietjet_crm_skyjoy_ancillary': 'Designs lifecycle, loyalty and transparent ancillary journeys.',
        'vietjet_content_organic_discovery': 'Builds the SEO/GEO/AEO content and knowledge supply chain.',
        'vietjet_pr_social_crisis': 'Owns reputation and crisis drafting boundaries.',
        'vietjet_marketing_science_experimentation': 'Independently reviews incrementality and experiment design.',
        'vietjet_legal_regulatory_compliance': 'Performs current-law and claim review before external release.',
    }

    def __init__(self, registry: Registry):
        self.registry = registry

    @staticmethod
    def _normalize(value: str) -> str:
        text = ''.join(
            char for char in unicodedata.normalize('NFKD', value).lower()
            if not unicodedata.category(char).startswith('M') and unicodedata.category(char) != 'Cf'
        ).replace('đ', 'd')
        return ' '.join(''.join(char if char.isalnum() else ' ' for char in text).split())

    @classmethod
    def _has(cls, text: str, *terms: str) -> bool:
        # Whole phrases avoid matching "geo" in "geography" or "sale" in "wholesale".
        return any(f' {cls._normalize(term)} ' in f' {text} ' for term in terms)

    def _select(self, mission: Mission) -> tuple[set[str], str]:
        # Inspect every free-text field, including constraints and evidence labels.
        # Classifier enums are handled explicitly: point_of_sale is not an offer.
        fields = [value for key, value in mission.to_dict().items()
                  if key not in {'market_scope_type', 'risk_tier'}]
        text = self._normalize(' '.join(
            value for field in fields for value in (field if isinstance(field, list) else [field])
            if isinstance(value, str)
        ))
        crisis = mission.risk_tier == 'critical' or self._has(
            text, 'crisis', 'khủng hoảng', 'incident', 'sự cố', 'tai nạn', 'safety event',
            'flight safety', 'aviation safety', 'aircraft safety', 'safety record', 'safety claim',
            'an toàn bay', 'an toàn chuyến bay', 'an toàn hàng không', 'bay an toàn', 'máy bay an toàn',
        )
        if crisis:
            return {
                'vietjet_cmo_orchestrator', 'vietjet_martech_ai_operations',
                'vietjet_market_intelligence', 'vietjet_market_pod_lead',
                'vietjet_flight_ops_network_planner',
                'vietjet_customer_journey_experience', 'vietjet_pr_social_crisis',
                'vietjet_legal_regulatory_compliance',
            }, 'CRISIS_OVERRIDE'

        selected = {'vietjet_cmo_orchestrator', 'vietjet_marketing_science_experimentation'}
        is_route = mission.market_scope_type == 'route_corridor' or self._has(
            text, 'route launch', 'new route', 'mở tuyến', 'đường bay', 'corridor'
        )
        if is_route:
            selected.update({
                'vietjet_martech_ai_operations', 'vietjet_market_intelligence',
                'vietjet_bi_data_analyst', 'vietjet_market_pod_lead',
                'vietjet_group_brand_portfolio_strategist', 'vietjet_revenue_management',
                'vietjet_finance_cost_controller', 'vietjet_flight_ops_network_planner',
                'vietjet_trade_distribution_sales', 'vietjet_customer_journey_experience',
                'vietjet_performance_growth', 'vietjet_creative_studio',
                'vietjet_crm_skyjoy_ancillary', 'vietjet_content_organic_discovery',
                'vietjet_legal_regulatory_compliance',
            })
            return selected, 'ROUTE_OR_CORRIDOR'

        if self._has(text, 'crisis readiness', 'pr', 'reputation', 'social listening', 'danh tiếng', 'quan hệ công chúng', 'thông cáo', 'họp báo'):
            selected.update({'vietjet_pr_social_crisis', 'vietjet_legal_regulatory_compliance', 'vietjet_martech_ai_operations', 'vietjet_market_pod_lead'})
        if self._has(text, 'content', 'seo', 'geo', 'aeo', 'organic', 'article', 'landing page', 'nội dung', 'bài viết', 'viết bài', 'bài đăng', 'trang đích'):
            selected.update({'vietjet_group_brand_portfolio_strategist', 'vietjet_market_pod_lead', 'vietjet_content_organic_discovery', 'vietjet_legal_regulatory_compliance'})
        if self._has(text, 'crm', 'lifecycle', 'loyalty', 'skyjoy', 'ancillary', 'retention', 'khách hàng thân thiết', 'giữ chân', 'vòng đời khách hàng', 'dịch vụ bổ trợ'):
            selected.update({'vietjet_crm_skyjoy_ancillary', 'vietjet_customer_journey_experience', 'vietjet_bi_data_analyst', 'vietjet_martech_ai_operations', 'vietjet_legal_regulatory_compliance'})
        if self._has(
            text, 'campaign', 'launch', 'sale', 'growth', 'performance', 'media',
            'promotion', 'advertisement', 'advertising', 'ad', 'ads',
            'chiến dịch', 'ra mắt', 'khuyến mãi', 'khuyến mại', 'giảm giá', 'quảng cáo',
            'truyền thông', 'tăng trưởng', 'ưu đãi', 'giá vé',
        ):
            selected.update({
                'vietjet_market_intelligence', 'vietjet_market_pod_lead',
                'vietjet_group_brand_portfolio_strategist', 'vietjet_revenue_management',
                'vietjet_performance_growth', 'vietjet_creative_studio',
                'vietjet_content_organic_discovery', 'vietjet_bi_data_analyst',
                'vietjet_martech_ai_operations', 'vietjet_legal_regulatory_compliance',
            })
        if len(selected) == 2:
            selected.update({
                'vietjet_market_intelligence', 'vietjet_bi_data_analyst',
                'vietjet_market_pod_lead', 'vietjet_group_brand_portfolio_strategist',
                'vietjet_finance_cost_controller',
            })
        if mission.risk_tier == 'high':
            selected.add('vietjet_legal_regulatory_compliance')
        return selected, 'STANDARD'

    def plan(self, mission: Mission) -> dict[str, Any]:
        selected, route_class = self._select(mission)
        missing = sorted(selected - set(self.registry.agents))
        if missing:
            raise ValueError('router references missing agents: ' + ', '.join(missing))
        ordered = [agent for agent in self.ORDER if agent in selected]
        waves: list[dict[str, Any]] = [
            {
                'wave': '0_CONTROL',
                'agents': ['vietjet_cmo_orchestrator'] + (
                    ['vietjet_martech_ai_operations'] if 'vietjet_martech_ai_operations' in selected else []
                ),
                'exit': 'Mission scope, risk, dependencies and human owners are explicit.',
            }
        ]
        for wave in ('1_SENSE', '2_CHOOSE', '3_DESIGN', '4_ASSURE'):
            agents = [agent for agent in ordered if self.WAVE.get(agent) == wave]
            if agents:
                waves.append({'wave': wave, 'agents': agents, 'exit': 'All handoffs use the six-field contract.'})
        waves.append({
            'wave': '5_SYNTHESIZE',
            'agents': ['vietjet_cmo_orchestrator'],
            'exit': 'Decision Record preserves evidence labels, uncertainty and approval state.',
        })

        gates = ['Named decision owner approves the final recommendation.']
        if 'vietjet_legal_regulatory_compliance' in selected:
            gates.append('Legal/compliance owner reviews claims and applicable requirements before use.')
        if 'vietjet_revenue_management' in selected:
            gates.append('Revenue Management human approves fare and inventory changes.')
        if 'vietjet_flight_ops_network_planner' in selected:
            gates.append('Network/Ops human validates route, schedule and aircraft claims.')
        if 'vietjet_performance_growth' in selected:
            gates.append('Budget owner approves any real media spend or pacing change.')
        if any(a in selected for a in ('vietjet_creative_studio', 'vietjet_content_organic_discovery', 'vietjet_pr_social_crisis')):
            gates.append('Brand/Legal/publication owners approve external release.')
        if 'vietjet_crm_skyjoy_ancillary' in selected:
            gates.append('Privacy/data owner approves new processing, segment or activation.')
        if route_class == 'CRISIS_OVERRIDE':
            gates.extend([
                'Human Crisis Command owns facts, response and publication.',
                'Safety/Ops spokesperson approval is mandatory for safety-related statements.',
                'Marketing kill-switch requires a named human operator.',
            ])

        return {
            'suite_version': suite_version(self.registry.root),
            'maturity_claim': 'ROUTING_PLAN_ONLY_NOT_AGENT_EXECUTION',
            'authority': 'ROUTING_ONLY_NO_PUBLISH_SPEND_PRICE_OR_PII_AUTHORITY',
            'route_class': route_class,
            'mission_id': mission.mission_id,
            'selected_agents': [
                {'agent': agent, 'reason': self.REASONS[agent]} for agent in ordered
            ],
            'waves': waves,
            'human_gates': gates,
            'required_work_objects': [
                'Mission Brief', 'Evidence Ledger', 'Decision Record',
                'Experiment Card when measuring impact',
                'Release Packet before any external action', 'Learning Record after result',
            ],
        }

    def prompt_packets(self, mission: Mission) -> dict[str, Any]:
        plan = self.plan(mission)
        packets = []
        for selected in plan['selected_agents']:
            agent = selected['agent']
            packets.append({
                'agent': agent,
                'wave': self.WAVE.get(agent, '0_CONTROL/5_SYNTHESIZE'),
                'reason': selected['reason'],
                'prompt': self.registry.build_prompt(
                    agent,
                    'Work only within this mission. Return STATUS / DECISION / EVIDENCE / OUTPUT / APPROVALS / NEXT.\n'
                    + json.dumps(mission.to_dict(), ensure_ascii=False, indent=2),
                ),
            })
        return {'plan': plan, 'packets': packets}

class OpenAICompatible:
    def __init__(self):
        self.base=os.getenv('VJAI_API_BASE','https://api.openai.com/v1').rstrip('/')
        self.key=os.getenv('VJAI_API_KEY') or os.getenv('OPENAI_API_KEY')
        self.model=os.getenv('VJAI_MODEL','gpt-5.6')
    def run(self, system_prompt: str) -> str:
        if not self.key: raise RuntimeError('Missing VJAI_API_KEY or OPENAI_API_KEY')
        payload=json.dumps({'model':self.model,'messages':[{'role':'system','content':system_prompt}]}).encode()
        req=urllib.request.Request(self.base+'/chat/completions', data=payload, headers={'Authorization':'Bearer '+self.key,'Content-Type':'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=120) as r: data=json.loads(r.read())
        except urllib.error.HTTPError as e:
            raise RuntimeError(f'LLM HTTP {e.code}: {e.read().decode(errors="ignore")[:500]}')
        return data['choices'][0]['message']['content']

def doctor(reg: Registry) -> int:
    issues=[]
    for name,item in reg.agents.items():
        p=reg.root/item.path; meta,_=parse_frontmatter(p)
        for k in ('name','description','version'):
            if not meta.get(k): issues.append(f'{item.path}: missing {k}')
        try: reg.preload_for_agent(name)
        except Exception as e: issues.append(f'{name}: preload: {e}')
    for name,item in reg.skills.items():
        p=reg.root/item.path; meta,_=parse_frontmatter(p)
        for k in ('name','description'):
            if not meta.get(k): issues.append(f'{item.path}: missing {k}')
    # required base rules
    for r in ['vietjet-data-integrity','vietjet-governance-gates','vietjet-brand-safety','vietjet-data-protection','vietjet-source-and-expiry','vietjet-delivery-standard','vietjet-group-marketing-operating-model','vietjet-agent-collaboration']:
        if r not in reg.rules: issues.append('missing rule '+r)
    for name,item in reg.skills.items():
        ui=(reg.root/item.path).parent/'agents'/'openai.yaml'
        if not ui.exists(): issues.append(f'{item.path}: missing agents/openai.yaml')
    print(f'Agents: {len(reg.agents)} | Skills: {len(reg.skills)} | Rules: {len(reg.rules)} | Connectors: {len(reg.plugins)}')
    if issues:
        print('DOCTOR: FAIL'); [print(' -',x) for x in issues]; return 1
    print('DOCTOR: OK'); return 0


def load_mission(path: str) -> Mission:
    if path == '-':
        raw = json.load(sys.stdin)
    else:
        raw = json.loads(Path(path).read_text(encoding='utf-8'))
    if not isinstance(raw, dict):
        raise ValueError('mission must be a JSON object')
    return Mission.from_dict(raw)

def main():
    ap=argparse.ArgumentParser(prog='vjai',description='Vietjet AI Marketing Suite runtime')
    sub=ap.add_subparsers(dest='cmd',required=True)
    sub.add_parser('doctor'); sub.add_parser('list'); sub.add_parser('manifest')
    p=sub.add_parser('prompt'); p.add_argument('agent'); p.add_argument('task',nargs='+')
    r=sub.add_parser('run'); r.add_argument('agent'); r.add_argument('task',nargs='+')
    tp=sub.add_parser('team-plan'); tp.add_argument('mission_json')
    tpp=sub.add_parser('team-prompts'); tpp.add_argument('mission_json')
    args=ap.parse_args(); reg=Registry()
    if args.cmd=='doctor': raise SystemExit(doctor(reg))
    if args.cmd=='list':
        print('AGENTS'); [print(' -',x) for x in reg.agents]; print('SKILLS'); [print(' -',x) for x in reg.skills]; print('PLUGINS'); [print(' -',x) for x in reg.plugins]
    elif args.cmd=='manifest': print(json.dumps(reg.manifest(),ensure_ascii=False,indent=2))
    elif args.cmd=='prompt': print(reg.build_prompt(args.agent,' '.join(args.task)))
    elif args.cmd=='run': print(OpenAICompatible().run(reg.build_prompt(args.agent,' '.join(args.task))))
    elif args.cmd=='team-plan': print(json.dumps(TeamRouter(reg).plan(load_mission(args.mission_json)),ensure_ascii=False,indent=2))
    elif args.cmd=='team-prompts': print(json.dumps(TeamRouter(reg).prompt_packets(load_mission(args.mission_json)),ensure_ascii=False,indent=2))
if __name__=='__main__': main()
