# Creative Governance

Apply these rules to every skill in this plugin.

## Start-of-run checks

1. Identify the campaign, audience, usage channel, output format, and intended use.
2. Separate `FACTUAL CAMPAIGN REQUIREMENTS` from `CREATIVE ASSUMPTIONS`.
3. Record missing facts as `DATA UNAVAILABLE`; never fill them with plausible details.
4. Confirm which locks apply: aircraft, livery, mascot, face identity, typography, text, subtitle, logo, color, or composition.
5. Confirm whether the requested output is a prompt/specification, a QA review, or a generated asset request.

## Commercial claim boundary

- Do not invent routes, route dates, flight schedules, fares, offers, booking periods, travel periods, inventory, eligibility, campaign names, or approved claims.
- Treat supplied commercial claims as `BRIEF FACT - VERIFY BEFORE PUBLISHING` unless an approved source is provided.
- Hand off fare, offer, route, date, inventory, eligibility, and compliance claims to `vietjet-commercial-ops` for commercial governance.
- Creative outputs must use placeholders such as `[APPROVED FARE]` or omit the claim when facts are unavailable.

## Brand boundary

- Preserve the supplied Vietjet red-yellow identity and approved brand assets.
- Do not invent exact color codes, fonts, livery details, logos, slogans, mascots, uniforms, or face identity references.
- If approved assets or lock references are missing, request them or mark the result `LOCK NOT VERIFIED`.
- Do not claim Legal, Brand, Commercial, or operational approval.

## Text and video boundary

- AI-generated text inside visuals is high risk. Prefer blank text-safe zones and add final text manually in design software.
- When `no text`, `no subtitle`, `no logo`, or equivalent constraints are requested, repeat them in positive instructions, negative prompts, and QA checks.
- Do not embed unverified commercial copy into image or video prompts.

## End-of-run block

End substantive outputs with:

```text
STATUS: CREATIVE DRAFT - HUMAN REVIEW REQUIRED
FACTUAL CAMPAIGN REQUIREMENTS:
- ...
CREATIVE ASSUMPTIONS:
- ...
LOCKS APPLIED / NOT VERIFIED:
- ...
MANUAL DESIGN ACTIONS:
- ...
COMMERCIAL CLAIMS FOR VIETJET-COMMERCIAL-OPS:
- ...
```
