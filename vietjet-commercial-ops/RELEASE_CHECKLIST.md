# Internal v0.1.0 Release Checklist

## Package

- [x] Plugin manifest version is `0.1.0`
- [x] README documents purpose, users, skills, governance, boundaries, fallback behavior, prohibitions, and limitations
- [x] Skill index covers all eight skills
- [x] Test prompts cover all eight skills
- [x] Changelog records the initial internal release

## Validation

- [x] Plugin validator passed
- [x] All eight skill validators passed
- [x] Acceptance tests passed: 8/8
- [x] Every skill links to shared operating governance
- [x] No external or connected data was used during acceptance testing
- [x] Final code review found no blocking issues

## Governance Readiness

- [x] Human approval remains mandatory
- [x] Connector fallback rules are documented
- [x] Data-boundary rules are documented
- [x] Missing facts, policies, and approvals must be marked explicitly
- [x] The plugin cannot authorize publishing, activation, or execution

## Release Decision

- [x] Ready for controlled internal pilot

**Known rollout conditions:** Vietjet should supply the approved authority matrix, connector scopes, data-source ownership, legal terms templates, and current fare-family definitions before operational use.
