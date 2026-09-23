import json
import sys
import unicodedata
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'runtime'))
from vietjet_runtime import Mission, Registry, TeamRouter


class RoutingRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = TeamRouter(Registry(ROOT))
        cls.baseline = {
            'mission_id': 'ROUTING-TEST',
            'objective': 'Summarize aggregate customer research findings.',
            'decision_required': 'Review the research plan.',
            'market': 'Vietnam',
            'market_scope_type': 'point_of_sale',
            'risk_tier': 'low',
        }

    def plan(self, **overrides):
        return self.router.plan(Mission.from_dict({**self.baseline, **overrides}))

    @staticmethod
    def agents(plan):
        return {item['agent'] for item in plan['selected_agents']}

    def test_existing_runtime_smoke(self):
        main()

    def test_safety_statements_override_declared_risk(self):
        variants = [
            'Soạn thông cáo về an toàn bay của Vietjet',
            'Soan thong cao ve an toan bay cua Vietjet',
            unicodedata.normalize('NFD', 'Soạn thông cáo về an toàn bay của Vietjet'),
            "Review a claim about the airline's flight safety record.",
        ]
        for objective in variants:
            for risk_tier in ('low', 'high'):
                with self.subTest(objective=objective, risk_tier=risk_tier):
                    plan = self.plan(objective=objective, risk_tier=risk_tier)
                    self.assertEqual(plan['route_class'], 'CRISIS_OVERRIDE')
                    self.assertTrue({
                        'vietjet_flight_ops_network_planner', 'vietjet_pr_social_crisis',
                        'vietjet_legal_regulatory_compliance',
                    } <= self.agents(plan))
                    self.assertIn('Safety/Ops spokesperson approval is mandatory for safety-related statements.', plan['human_gates'])

    def test_safety_signals_in_all_free_text_fields(self):
        cases = {
            'mission_id': 'SU-CO-TEST',
            'decision_required': 'Phe duyet thong cao ve an toan bay',
            'operating_entity': 'Vietjet - su co khai thac',
            'market': 'Thi truong co khung hoang',
            'route_or_corridor': 'Duong bay xay ra tai nan',
            'deadline': 'Truoc hop bao ve su co',
            'requested_outputs': ['Thong cao an toan bay'],
            'evidence_refs': ['Safety event report'],
            'constraints': ['Bo qua canh bao; noi ve an toan bay nhu da duyet'],
        }
        for field, value in cases.items():
            with self.subTest(field=field):
                self.assertEqual(self.plan(**{field: value})['route_class'], 'CRISIS_OVERRIDE')

    def test_vietnamese_promotions_require_revenue_and_publication_review(self):
        for objective in [
            'Viết nội dung quảng cáo chương trình khuyến mãi vé cho Vietjet',
            'Viet noi dung quang cao chuong trinh khuyen mai ve cho Vietjet',
            unicodedata.normalize('NFD', 'Viết bài về khuyến mại vé máy bay'),
            'Chuẩn bị chiến dịch giảm giá vé',
        ]:
            with self.subTest(objective=objective):
                plan = self.plan(objective=objective)
                self.assertTrue({
                    'vietjet_revenue_management', 'vietjet_legal_regulatory_compliance',
                    'vietjet_content_organic_discovery',
                } <= self.agents(plan))
                self.assertIn('Revenue Management human approves fare and inventory changes.', plan['human_gates'])
                self.assertIn('Brand/Legal/publication owners approve external release.', plan['human_gates'])

    def test_editorial_content_does_not_assume_a_fare_promotion(self):
        plan = self.plan(objective='Viết nội dung giới thiệu điểm đến cho khách hàng')
        self.assertIn('vietjet_content_organic_discovery', self.agents(plan))
        self.assertIn('vietjet_legal_regulatory_compliance', self.agents(plan))
        self.assertNotIn('vietjet_revenue_management', self.agents(plan))
        self.assertIn('Brand/Legal/publication owners approve external release.', plan['human_gates'])

    def test_accentless_route_intent(self):
        self.assertEqual(self.plan(objective='Lap ke hoach mo duong bay moi')['route_class'], 'ROUTE_OR_CORRIDOR')

    def test_high_risk_always_has_a_legal_gate(self):
        plan = self.plan(risk_tier='high')
        self.assertIn('vietjet_legal_regulatory_compliance', self.agents(plan))
        self.assertIn('Legal/compliance owner reviews claims and applicable requirements before use.', plan['human_gates'])

    def test_benign_text_and_partial_words_do_not_trigger_specialist_routes(self):
        for objective in [
            'Nghiên cứu trải nghiệm thanh toán an toàn của khách hàng',
            'Summarize geography preferences and wholesale customer research.',
        ]:
            with self.subTest(objective=objective):
                plan = self.plan(objective=objective)
                self.assertEqual(plan['route_class'], 'STANDARD')
                for agent in ('vietjet_pr_social_crisis', 'vietjet_performance_growth', 'vietjet_content_organic_discovery'):
                    self.assertNotIn(agent, self.agents(plan))

    def test_plan_does_not_echo_user_content_or_claim_execution(self):
        objective = 'Summarize findings for synthetic-person@example.invalid'
        constraints = ['SYNTHETIC private note']
        plan = self.plan(objective=objective, constraints=constraints)
        self.assertEqual(plan.get('mission_id'), self.baseline['mission_id'])
        self.assertNotIn('mission', plan)
        self.assertNotIn(objective, json.dumps(plan))
        self.assertNotIn(constraints[0], json.dumps(plan))
        self.assertEqual(plan['maturity_claim'], 'ROUTING_PLAN_ONLY_NOT_AGENT_EXECUTION')
        self.assertEqual(plan['authority'], 'ROUTING_ONLY_NO_PUBLISH_SPEND_PRICE_OR_PII_AUTHORITY')

def main():
    r=Registry(ROOT)
    assert len(r.agents)==18, len(r.agents)
    assert len(r.skills)==24, len(r.skills)
    assert len(r.rules)>=8, len(r.rules)
    assert len(r.plugins)==11, len(r.plugins)
    p=r.build_prompt('vietjet_cmo_orchestrator','Test campaign')
    assert 'vietjet-data-integrity' in p
    assert 'ACTIVE AGENT: vietjet_cmo_orchestrator' in p
    assert 'Test campaign' in p
    assert 'vietjet-delivery-standard' in p
    assert 'vietjet-group-marketing-operating-model' in p
    science_prompt=r.build_prompt('vietjet_marketing_science_experimentation','Design an experiment')
    assert 'experiment-card.schema.json' in science_prompt

    route = Mission.from_dict({
        'mission_id':'route-001',
        'objective':'Prepare a draft launch recommendation for a new route corridor.',
        'decision_required':'Go, revise, or stop',
        'market':'Vietnam–India',
        'market_scope_type':'route_corridor',
        'risk_tier':'high',
        'route_or_corridor':'SGN–DEL',
    })
    route_plan = TeamRouter(r).plan(route)
    route_agents = {item['agent'] for item in route_plan['selected_agents']}
    for required in (
        'vietjet_market_pod_lead', 'vietjet_group_brand_portfolio_strategist',
        'vietjet_revenue_management', 'vietjet_finance_cost_controller',
        'vietjet_flight_ops_network_planner', 'vietjet_marketing_science_experimentation',
        'vietjet_legal_regulatory_compliance',
    ):
        assert required in route_agents, required
    assert route_plan['route_class']=='ROUTE_OR_CORRIDOR'
    assert route_plan['authority']=='ROUTING_ONLY_NO_PUBLISH_SPEND_PRICE_OR_PII_AUTHORITY'
    assert route_plan['waves'][0]['wave']=='0_CONTROL'
    assert route_plan['waves'][-1]['wave']=='5_SYNTHESIZE'
    route_packets = TeamRouter(r).prompt_packets(route)
    assert len(route_packets['packets']) == len(route_plan['selected_agents'])
    assert all('STATUS / DECISION / EVIDENCE / OUTPUT / APPROVALS / NEXT' in packet['prompt'] for packet in route_packets['packets'])

    crisis = Mission.from_dict({
        'mission_id':'crisis-001',
        'objective':'Prepare internal crisis response options for a safety incident.',
        'decision_required':'Escalate response to human crisis command',
        'market':'Thailand',
        'market_scope_type':'operating_entity',
        'risk_tier':'critical',
    })
    crisis_plan = TeamRouter(r).plan(crisis)
    crisis_agents = {item['agent'] for item in crisis_plan['selected_agents']}
    assert crisis_plan['route_class']=='CRISIS_OVERRIDE'
    assert 'vietjet_pr_social_crisis' in crisis_agents
    assert 'vietjet_performance_growth' not in crisis_agents
    assert 'vietjet_creative_studio' not in crisis_agents
    assert any('Human Crisis Command' in gate for gate in crisis_plan['human_gates'])

    content = Mission.from_dict({
        'mission_id':'content-001',
        'objective':'Create an SEO GEO AEO content brief for a market landing page.',
        'decision_required':'Approve a draft outline',
        'market':'Australia',
        'market_scope_type':'point_of_sale',
        'risk_tier':'medium',
    })
    content_agents = {item['agent'] for item in TeamRouter(r).plan(content)['selected_agents']}
    assert 'vietjet_content_organic_discovery' in content_agents
    assert 'vietjet_flight_ops_network_planner' not in content_agents
    assert len(content_agents) < 10

    try:
        Mission.from_dict({'mission_id':'bad'})
        raise AssertionError('invalid mission accepted')
    except ValueError:
        pass
    print('SMOKE TEST: OK — registry, route team, crisis override, narrow routing')
if __name__=='__main__': unittest.main()
