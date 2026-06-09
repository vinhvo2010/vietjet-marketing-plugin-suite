---
description: Run a blocking visual QA review covering brand, IP, text, identity locks, artifacts, channel fit, and commercial claims.
argument-hint: [asset or prompt, intended channel, campaign facts, and approved references]
---

# Governed Visual QA

## Arguments

The asset or prompt, intended channel, supplied campaign facts, and approved references are in
`$ARGUMENTS`.

## Workflow

1. Read `skills/visual-qa/SKILL.md`, `references/creative-governance.md`,
   `references/generated-asset-qa-standard.md`, and the applicable lock references.
2. State what can and cannot be verified from the supplied references.
3. Review brand identity, IP/sports objects, generated text and logos, fake UI, anatomy, artifacts,
   continuity, crop, safe zones, channel fit, and applicable locks.
4. Treat malformed or unverified text, fake logos, prohibited objects, and unsupported commercial
   claims as blockers for external use.
5. Hand fares, offers, dates, inventory, eligibility, terms, and other commercial claims to
   `vietjet-commercial-ops`.
6. Recommend reject, revise, or proceed to human review. Do not approve the asset.

## Required Output

- Verification boundary
- Prioritized visual, IP, brand, and commercial findings
- Blocking fixes and manual design actions
- Commercial handoff
- Human review needs

End with the creative-governance end-of-run block. Do not label the asset approved or ready for
external use.
