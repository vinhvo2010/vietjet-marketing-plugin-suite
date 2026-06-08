---
name: brand-voice
description: "Rewrite content into Vietjet's brand voice — energetic, direct, commercial, optimistic, and travel-driven. Adjusts tone for context: punchy for social/campaigns, precise for executive/board, compliant for legal/regulatory. Works on any text input."
---

# brand-voice

Before starting, read and apply [Operating Governance](../../references/operating-governance.md).

## Purpose
Ensure every piece of Vietjet communication sounds like Vietjet — not a generic airline, not a corporate memo, not a translated document. Rewrites content to match the right register for the audience while maintaining factual accuracy and removing any compliance risks introduced by tone.

## Input Required
Provide:
- The content to rewrite (any format: headline, email, social post, brief, report, script, push notification)
- The output channel: social / email / app push / press release / executive / board / internal memo / ad copy
- The audience: consumer-facing / internal team / executive / board / media / regulator
- Any constraints: "keep the facts exactly as stated" / "cannot mention competitors" / "must include this disclaimer"

Optional: What's wrong with the current version ("too corporate", "too vague", "too promotional", "not on-brand").

## Connected Tools Needed
No connector required. Works entirely on pasted input.

## Vietjet Brand Voice Principles

### Core character
Vietjet is energetic, direct, commercial, optimistic, and travel-driven. VJ believes travel changes lives and that price should never stop someone from going somewhere. VJ is not a luxury brand, but it's not cheap — it's smart value for people who know what they want.

### Voice by register

| Context | Tone | Key qualities |
|---|---|---|
| Consumer campaign / social | Punchy, exciting, travel-first | Short sentences. Action verbs. Evoke the destination first, price second. Make the reader feel the trip. |
| Email / CRM | Warm, direct, personal | Address the journey occasion. Lead with benefit. One clear CTA. No waffle. |
| App push notification | Urgent, specific, clear | Max 50 chars headline. Benefit in 10 words or fewer. CTA is the whole message. |
| Press release / PR | Credible, confident, news-led | Lead with the fact. Quote sounds human. Avoid superlatives without evidence. |
| Internal brief / memo | Clear, professional, action-oriented | No jargon without definition. Every document has an ask. Numbers before narrative. |
| Executive / board | Precise, data-grounded, decisive | No hedge words. Every claim is sourced or marked [EST]. Decisions are explicit. |
| Legal / regulatory / compliance | Accurate, complete, unambiguous | No claims that can't be verified. Disclaimers included where required. Tone is neutral. |

### What Vietjet voice is NOT
- Not overly formal or stiff (avoid: "We are pleased to inform you that...")
- Not generic airline speak (avoid: "Your comfort is our priority", "We strive to deliver excellence")
- Not hyperbolic without evidence (avoid: "The best airline in Southeast Asia")
- Not passive (avoid: "A decision has been made to...")
- Not vague (avoid: "We offer competitive pricing")

### Vietjet-specific tone markers
- Travel is an emotion, not a transaction: lead with where, then with how much
- Price is a feature, not the identity: mention the value without making VJ sound cheap
- Energy is in the verbs: "Fly to Phuket from VND 499k" not "Phuket flights are available from VND 499k"
- Direct addresses work: "Your seat. Your route. Your schedule."
- Urgency is honest: "Only 200 seats at this price" (if true) — not fake scarcity

## Step-by-Step Workflow

**Step 1 — Diagnose the original**
What is wrong with the current version?
- Too corporate/formal?
- Too passive?
- Off-brand (generic airline speak)?
- Too promotional / legally risky claims?
- Factually ambiguous?
- Wrong register for audience?

**Step 2 — Identify the register**
Match the output to the channel and audience (see Voice by Register table above).

**Step 3 — Preserve the facts**
Extract the facts from the original. Do not alter: prices, dates, route names, regulatory claims, or figures. Mark any fact that needs verification: [VERIFY BEFORE PUBLISHING].

**Step 4 — Rewrite**
Apply the register and voice principles. Produce 2 variants where possible:
- Variant A: closer to the original structure, tightened and on-brand
- Variant B: more creative reframe, if appropriate for the channel

**Step 5 — Flag compliance risks introduced by the original**
If the original contained claims that are legally risky, ambiguous, or unverifiable, flag them — even if the rewrite removes them.

For promotional copy, explicitly test universal and free-fare language such as `mọi người`, `tất cả đường bay`, `miễn phí`, and `0Đ`. Remove or qualify those claims unless eligibility, inventory, exclusions, taxes, and fees are verified and disclosed. Route the result through `promo-qa` before publication.

## Output Format

```
BRAND VOICE REWRITE — [Channel/Audience] | DRAFT | [Date]
==========================================================

ORIGINAL:
[Paste of original content]

DIAGNOSIS:
[2–3 bullets: what was wrong with the original]

COMPLIANCE FLAGS IN ORIGINAL (if any):
[List — or "None identified"]

REWRITE — VARIANT A:
[Tightened, on-brand version]

REWRITE — VARIANT B (if applicable):
[More creative reframe]

REGISTER: [Social / Email / Push / Executive / etc.]
TONE APPLIED: [Which brand register used and why]

NOTES FOR REVIEWER:
[Any facts that need verification before publishing]
[Any claims that were removed and why]

[DRAFT — HUMAN APPROVAL REQUIRED before publishing or distributing]
```

## Human Approval Checkpoint
> Brand voice rewrites change how Vietjet communicates externally. Before any rewritten content is published, posted, or sent: (1) the original facts must be verified as accurate, (2) a Vietjet Brand/Marketing team member must confirm the rewrite is on-brand, (3) for external/consumer content, a compliance check is recommended for any claim that could attract regulatory scrutiny (price claims, safety claims, destination claims). Codex provides the rewrite; humans approve the content.

## Example Command
```
/brand-voice

Original text:
"Vietjet Air is pleased to announce the launch of new routes connecting
Ho Chi Minh City to Bangkok, providing passengers with convenient and
affordable travel options to Thailand's capital city."

Channel: Press release (media audience)
Constraint: Keep Bangkok and Ho Chi Minh City. Keep the launch announcement framing. Cannot make specific price claims.
What's wrong: Too formal, too generic, passive voice, no energy.
```

## Risks and Guardrails
- **Facts are sacred** — never change a price, date, route name, or regulatory statement in a rewrite. If a fact is unclear, flag it: [FACT UNCLEAR — verify before publishing].
- **Price claims in consumer advertising** — in Vietnam, price advertising is regulated. Flag any rewrite containing a promotional price: [PRICE CLAIM — confirm this fare is currently available before publishing].
- **Free and universal claims** — never preserve `free`, `for everyone`, or equivalent wording when taxes, fees, seat quotas, eligibility, or route/date exclusions may apply. Rewrite to a qualified `from` claim and require `promo-qa`.
- **Safety claims** — never rewrite safety-related content without flagging for Legal/Safety review.
- **"Best", "cheapest", "number one"** — superlatives require evidence. If the original contained an unsupported superlative, remove it in the rewrite and note: [SUPERLATIVE REMOVED — no evidence provided. Add source or remove from final].
- **Translated content** — if the original was translated from Vietnamese, the rewrite may fix translation artifacts but cannot fix cultural nuance errors. Flag: [ORIGINAL MAY HAVE TRANSLATION ISSUES — recommend native speaker review].
