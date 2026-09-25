# Bio-Inspired Security Framework Policy — Health Quest

**Approach:** biological-immunity-inspired adaptive security (Detect → Analyse → Validate → Respond → Record → Learn → Adapt).
**Model:** the app, its dependencies, and its consent/privacy boundaries are treated as a living organism with defensive "immune memory".

## 1. Purpose

Health Quest is a student-facing educational web app. It is built by a student
under faculty guidance and is **release-track educational software, not a
research submission**. This policy still keeps its supply chain defensively
adaptive: dependency threats are continuously detected, validated by the
self-check suite, and recorded as immune memory so each cycle starts healthier.

## 2. Trusted attacker flow (immune model)

```
Detect -> Analyse -> Validate (CI) -> Respond (approval gate) -> Record -> Learn -> Adapt
```

- **Detect:** Dependabot watches `pip` (packaging metadata) and `github-actions`.
- **Analyse/Validate:** every change passes `tests/check_site.py` (scoring
  markers, consent flow, license, docs) before merge.
- **Respond:** human approval gate — **no auto-merge**.
- **Record/Learn:** merged updates refresh the baseline (immune memory).

## 3. Roles

| Role | Responsibility |
|------|----------------|
| Maintainer / Reviewer | Approves every change and every consent-flow edit |
| Dependabot | Continuous detection, security updates, weekly cadence |
| CI pipeline | Runs the site self-check on every proposed change |
| GitHub tooling | Code scanning, secret scanning, dependency review |

## 4. Governance

- Version updates: weekly; vulnerability updates: immediate and unbounded.
- Consent and location-privacy behavior is treated as security-sensitive.
- Least-privilege permissions; rollback is a single reverible PR.

## 5. Supported versions

| Version | Supported |
|---------|-----------|
| 3.1.x   | Yes       |

## 6. Reporting a vulnerability

Report through a **private advisory** at
https://github.com/karun99/health-quest/security/advisories/new. Expect a
response within 5 business days; do not disclose publicly until a fix lands.

## 7. Research acknowledgement

This policy is a research prototype of immunity-inspired adaptive security,
applied here to student-facing software. It does not guarantee complete
cybersecurity; it is intended to sit alongside the collaborative cyber-defense
principles of the OpenAI Collective Cyber Defense letter.