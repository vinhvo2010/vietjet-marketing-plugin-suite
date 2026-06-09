# Human Visual QA Checklist

Campaign: `football-summer-2026`  
Scope: 13 corrected draft still assets  
Current status: `HUMAN_QA_REQUIRED` / `DO_NOT_RELEASE`

Complete this checklist separately for every asset. Record findings and the human decision in `HUMAN_VISUAL_QA_REVIEW_TABLE.md`.

## Technical Checks

- [ ] Correct file opens.
- [ ] Correct aspect ratio.
- [ ] No obvious compression artifacts.
- [ ] No broken crop.
- [ ] Safe zones are usable for manual typography.
- [ ] Visual quality is acceptable for internal review.

## Brand Checks

- [ ] Red-yellow energy feels aligned.
- [ ] No wrong airline, logo, or livery.
- [ ] No generated Vietjet logo.
- [ ] No distorted brand-like text.
- [ ] No uncontrolled typography inside image.

## IP / Sports Checks

- [ ] No FIFA logo.
- [ ] No World Cup or tournament branding.
- [ ] No trophy or trophy-like silhouette.
- [ ] No official mascot.
- [ ] No official slogan.
- [ ] No host city logo.
- [ ] No team crest.
- [ ] No official football kit.
- [ ] No official match ball design.
- [ ] No player likeness.
- [ ] No sponsor badge.
- [ ] No ticket or match-access implication.

## Commercial Checks

- [ ] No fare.
- [ ] No price.
- [ ] No booking period.
- [ ] No 0Đ.
- [ ] No inventory or scarcity claim.
- [ ] No route, schedule, or aircraft claim.
- [ ] No fake boarding pass or fake UI with claims.

## Human / Anatomy Checks

- [ ] No distorted faces.
- [ ] No extra fingers or limbs.
- [ ] No public-figure likeness.
- [ ] No inappropriate pose.
- [ ] No unsafe children/minors issue.
- [ ] No identity-lock issue.

## Human Decision

The human reviewer must choose exactly one:

- `APPROVE_FOR_APPROVED_FOLDER`
- `REJECT_TO_REJECTED_FOLDER`
- `REVISION_REQUIRED`
- `NEEDS_LEGAL_IP_REVIEW`
- `NEEDS_BRAND_REVIEW`

Only a human reviewer may choose `APPROVE_FOR_APPROVED_FOLDER`. Completing this checklist does not grant release approval.
