# Project 2: AI Risk Assessment and Governance Review Pack

## Scenario

**System Under Review:** SignalPath Interpret (SP-AI-001)
**Organization:** SignalPath Technologies
**Use Case:** AI-assisted real-time interpretation for Deaf and hard-of-hearing users in Video Relay Service calls

Following the classification exercise in Project 1, SignalPath Interpret was identified as a high-risk system under Annex III of the EU AI Act, currently operating without a completed conformity assessment. It processes biometric data, including hand shape, facial expression, and body movement, to interpret American Sign Language in real time across legally protected communications: emergency calls, medical appointments, legal proceedings, and everyday relay service.

The Chief Risk Officer has requested a formal governance review before a Board-level decision on the system's production deployment. The review covers:

1. A structured risk assessment identifying harms, likelihood, and impact specific to ASL interpretation failures
2. Proposed mitigation measures and residual risk position
3. A governance review memo addressed to the Chief Executive and Board

---

## What This Project Demonstrates

- Ability to move from classification to structured risk analysis on a high-stakes AI system
- Understanding of AI-specific harms in a community context: signer variation, Deaf accent, physical limitation, regional dialect, and emergency call failure modes
- Capacity to define what meaningful human oversight looks like when the end user is Deaf and the interpreter is AI
- Ability to communicate governance analysis to senior non-technical audiences who may have no direct experience with the Deaf community
- Knowledge of the NIST AI RMF Map and Measure functions applied to a real use case

---

## Artifacts

| File | Description |
|------|-------------|
| [`risk-assessment.md`](./risk-assessment.md) | Full structured risk assessment with likelihood and impact matrix |
| [`governance-review-memo.md`](./governance-review-memo.md) | Executive memo to Board recommending a governance decision |

---

## How the Artifacts Connect

The risk assessment is the analytical foundation. It identifies risks specific to AI interpretation in VRS contexts, assesses them on a consistent scale, applies mitigation measures, and arrives at a residual risk position. This is technical governance work.

The governance review memo translates that analysis into the format executives need: clear summary, business implications, a defined recommendation, and an actionable decision request. It is written for a Board that understands liability but may not understand what a Deaf accent is or why a broken pinky changes everything an AI classifier thinks it sees.

Together they reflect how governance actually works: rigorous analysis feeding clear decisions, not analysis as a substitute for decisions.

---

## Frameworks Applied

- **NIST AI RMF** — Map (risk identification and contextualization) and Measure (risk analysis) functions
- **EU AI Act** — Article 9 (risk management system), Article 10 (data governance), Article 13 (transparency), Article 14 (human oversight)
- **FCC Part 64** — VRS service reliability obligations and functional equivalency standard
- **ADA Title IV** — Telecommunications accessibility obligations for relay service providers
- **ISO 31000** — Risk assessment structure and terminology
