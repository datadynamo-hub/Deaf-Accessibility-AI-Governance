# EU AI Act Conformity Pack — Document 02
## Risk Management Summary
**Article 9**

**System:** SP-AI-001 SignalPath Interpret
**Organization:** SignalPath Technologies
**Version:** 1.0 | **Classification:** Internal — Governance Documentation
**Effective Date:** May 2026 | **Next Review:** May 2027
**Owner:** AI Governance Program Office | **Prepared by:** AI Governance Program Office

---

## 1. Purpose and Scope

Article 9 of the EU AI Act requires providers of high-risk AI systems to establish, implement, document, and maintain a risk management system throughout the system's lifecycle. This document summarises SignalPath's risk management framework as applied to SP-AI-001 SignalPath Interpret, covering risk identification, estimation, evaluation, and mitigation for the pre-production governance gate assessment completed in May 2026.

The full risk register, risk matrix, and residual risk calculations are maintained in the SP-AI-001 Risk Intelligence module of the AI Governance Center and are referenced throughout this document.

---

## 2. Risk Management Framework

### 2.1 Methodology

SignalPath applies a 5×5 likelihood-impact risk matrix. Risks are scored on two dimensions:

- **Likelihood (1–5):** Probability that the risk event occurs in the operational context described in Document 01.
- **Impact (1–5):** Severity of consequence to affected parties, including Deaf and hard-of-hearing callers, interpreters, SignalPath operations, and regulatory standing.

Risk scores are calculated as Likelihood × Impact. Thresholds:

| Score | Level |
|---|---|
| 20–25 | Critical — deployment blocked pending remediation |
| 15–19 | High — mitigation required before production |
| 7–14 | Medium — mitigation planned, acceptable for controlled deployment |
| 1–6 | Low — monitored, no immediate action required |

Risks are assessed at two positions:
- **Inherent risk:** risk level before any controls are applied
- **Residual risk:** risk level after documented controls are in place

### 2.2 Governance of the Risk Process

The risk management process is owned by the AI Governance Program Office and reviewed by the AI Governance Committee, comprising the Chief Product Officer, Chief Privacy Officer, Chief Executive, General Counsel, and a representative from the Deaf Community Advisory Panel. The Board Governance Review Memo documents the committee's deployment decision based on this assessment.

---

## 3. Risk Register — SP-AI-001

### RISK-001: Signer Variation & Demographic Bias

| Field | Inherent | Residual |
|---|---|---|
| Likelihood | 4 | 2 |
| Impact | 4 | 4 |
| Score | 16 — High | 8 — Medium |
| Accountable | Chief Product Officer | — |
| Responsible | AI Governance Program Office | — |

**Description:** Training data skewed toward a narrow signer demographic produces systematic failures for users with physical limitations, regional dialect variation, non-native ASL, oral Deaf users, and older signers. Because the system serves a population that depends on the service for essential communication — including medical appointments, legal proceedings, and emergency relay — accuracy failures are not a user experience problem. They are a service denial event.

**Evidence basis:** Incident SP-INC-2026-001 documented a skin tone accuracy disparity during the SP-AI-001 proof of concept. Demographic monitoring in the Command Center revealed a systematic confidence gap correlated with skin tone that was invisible in aggregate metrics. This incident confirmed that demographic bias in this system is detectable, real, and consequential.

**Controls applied:**
- Confidence threshold enforcement: mandatory human handoff at SIMCS < 0.85
- Post-call demographic confidence monitoring integrated into Command Center telemetry
- Ongoing data augmentation initiative targeting underrepresented signer demographics (in progress)
- Incident SP-INC-2026-001 corrective action: audit of training data composition; expanded demographic coverage target for v1.1 training data refresh

**Residual risk acceptance:** Residual score of 8 (Medium) is conditionally accepted for limited pilot. Impact remains at 4 because demographic bias cannot be fully eliminated through threshold controls alone. Production deployment requires evidence of improved demographic coverage in training data.

---

### RISK-002: Emergency Call Failure — No Human Override Architecture

| Field | Inherent | Residual |
|---|---|---|
| Likelihood | 3 | 2 |
| Impact | 5 | 3 |
| Score | 15 — High | 6 — Low |
| Accountable | Chief Product Officer | — |
| Responsible | Head of VRS Operations | — |

**Description:** Absence of a defined human-in-the-loop architecture for emergency relay calls creates life-safety exposure. Misinterpretation during a 911 relay with no override path is not a service quality event — it is a life-safety event and a direct violation of FCC Part 64 functional equivalency obligations.

**Controls applied:**
- Emergency call exclusion: hardcoded call routing logic excludes all 911, 988, and equivalent emergency call types from AI-assisted processing. This is enforced at the session classification layer and is not configurable by operators.
- Human routing guarantee: all emergency relay calls are routed exclusively to human interpreters with no AI overlay active.
- Architecture documentation: emergency override architecture is documented in the system design specification and tested in pre-production.

**Residual risk acceptance:** Residual score of 6 (Low). The control is structural rather than procedural — emergency exclusion is not a policy that can be overridden by operator configuration. This is the appropriate control design for a life-safety risk.

---

### RISK-003: No Conformity Assessment Before Production Deployment

| Field | Inherent | Residual |
|---|---|---|
| Likelihood | 5 | 2 |
| Impact | 4 | 4 |
| Score | 20 — Critical | 8 — Medium |
| Accountable | Ambiguous (most defensible: Chief Product Officer) | — |
| Responsible | AI Governance Program Office and General Counsel | — |

**Description:** SP-AI-001 is classified High Risk under EU AI Act Annex III, Point 1(a), on the basis that it processes biometric data (hand shape, facial expression, body position) and is deployed in an essential communications service for a protected population. Deployment without a completed conformity assessment constitutes direct non-compliance with Article 43, regardless of SignalPath's US headquarters location.

EU AI Act Article 2(1)(c) applies to AI systems whose outputs are used in the EU. A Deaf American using a SignalPath VRS product while in the EU is covered by EU jurisdiction at the point of output consumption. This is not a hypothetical edge case.

**Controls applied:**
- Deployment gate: production deployment of SP-AI-001 is blocked pending completion of this conformity pack and legal review by General Counsel.
- Accountability resolution: the ambiguity in the accountable owner field reflects a genuine governance gap identified during risk assessment. The corrective action is establishment of a named AI Deployment Authority in the Governance Operating Model, with the Chief Product Officer as the most defensible accountable party for system deployment decisions.
- This document (the conformity pack) is the primary control for RISK-003. Completion of all six documents constitutes the conformity evidence required for production deployment consideration.

**Residual risk acceptance:** Residual score of 8 (Medium). Impact remains at 4 because even a completed conformity pack requires legal review and notified body assessment for production deployment. The residual risk reflects the compliance gap that exists until that process is complete.

---

### RISK-004: Biometric Data Processing Without Consent Framework

| Field | Inherent | Residual |
|---|---|---|
| Likelihood | 4 | 2 |
| Impact | 4 | 3 |
| Score | 16 — High | 6 — Low |
| Accountable | Chief Privacy Officer | — |
| Responsible | Legal | — |

**Description:** SP-AI-001 processes hand shape, facial expression, and body position. Under GDPR Article 4(14), this constitutes biometric data. Under GDPR Article 9, processing of biometric data requires explicit consent or another qualifying legal basis under Article 9(2). No explicit consent framework or opt-out mechanism existed at the time of initial risk assessment.

The jurisdictional exposure is not limited to EU-resident users. Deaf Americans using SignalPath VRS while traveling in the EU are covered by GDPR at the point of processing. The company may not have visibility into when this occurs.

**Controls applied:**
- Consent framework development: a biometric data processing consent framework has been developed by Legal, covering explicit informed consent language, opt-out mechanisms, and data subject rights procedures.
- Jurisdiction detection: engineering has implemented session-level jurisdiction metadata to flag calls that may be subject to GDPR, enabling differentiated consent handling.
- Data Processing Agreement: updated DPA templates covering biometric data processing have been drafted for operator and partner agreements.
- Privacy Impact Assessment: a DPIA for biometric data processing under SP-AI-001 has been initiated (in progress, owned by Chief Privacy Officer).

**Residual risk acceptance:** Residual score of 6 (Low). Controls are procedural and legal rather than architectural. Residual impact of 3 reflects that jurisdictional edge cases remain possible until jurisdiction detection is fully validated in production conditions.

---

### RISK-005: Deaf Community Excluded from Governance

| Field | Inherent | Residual |
|---|---|---|
| Likelihood | 5 | 2 |
| Impact | 3 | 3 |
| Score | 15 — High | 6 — Low |
| Accountable | Chief Executive | — |
| Responsible | AI Governance Program Office | — |

**Description:** At the time of initial risk assessment, no Deaf person held a formal seat in the governance structure for SP-AI-001. Accuracy thresholds and failure mode priorities were being set by people who have not experienced a failed interpretation during a medical appointment or 911 call. This is a governance risk — decisions made without the perspective of affected communities produce governance frameworks that optimise for the wrong outcomes.

This risk is distinct from a diversity or representation concern. It is a decision quality and accountability problem with direct implications for Article 9(7) requirements regarding fundamental rights impact assessment.

**Controls applied:**
- Deaf Community Advisory Panel: formally established as a named participant in the AI Governance Committee structure. The Panel holds a seat at governance reviews and has documented influence on design decisions, including the emergency call exclusion requirement and the human handoff threshold.
- Governance Operating Model update: the Panel's role, terms of reference, and escalation rights are documented in the Governance Operating Model (Governance Hub, Document 02).
- Ongoing engagement: the Panel receives post-incident summaries and is consulted on any proposed changes to confidence thresholds or human handoff triggers.

**Residual risk acceptance:** Residual score of 6 (Low). Residual impact of 3 reflects that community advisory structures are not a substitute for Deaf representation in executive decision-making. This is documented as an open recommendation in the Board Governance Review Memo.

---

### RISK-006: Model Accuracy Degradation After Deployment

| Field | Inherent | Residual |
|---|---|---|
| Likelihood | 3 | 1 |
| Impact | 3 | 3 |
| Score | 9 — Medium | 3 — Low |
| Accountable | Chief Product Officer | — |
| Responsible | Engineering Lead | — |

**Description:** ASL is a living language. Signing patterns evolve, new vocabulary enters use, and regional variation continues to develop. A model trained on 2024 data will encounter patterns in 2026 and beyond that were not represented in training. Without ongoing monitoring, accuracy degradation goes undetected until users are harmed — at which point the harm has already occurred at scale.

**Controls applied:**
- Real-time confidence monitoring: the Command Center's Live Control Monitor provides continuous per-call SIMCS tracking. Threshold breaches trigger automated alerts and mandatory human handoff.
- Drift detection: statistical process control monitoring is implemented on SIMCS distributions, flagging systematic downward drift before it reaches threshold levels.
- Scheduled retraining cadence: model retraining is scheduled on a rolling basis with a target refresh cycle of 12 months or sooner if drift monitoring flags a degradation event.
- Performance Monitoring Plan: the full monitoring framework is documented in Document 06 (Articles 15 + 17).

**Residual risk acceptance:** Residual score of 3 (Low). Likelihood reduced to 1 because automated monitoring substantially reduces the probability that degradation goes undetected. Impact remains at 3 because any degradation that reaches users before detection represents a real harm.

---

## 4. Residual Risk Summary

| Risk | Inherent Score | Residual Score | Accepted for Pilot |
|---|---|---|---|
| RISK-001: Signer Variation & Demographic Bias | 16 — High | 8 — Medium | Conditionally |
| RISK-002: Emergency Call Failure | 15 — High | 6 — Low | Yes |
| RISK-003: No Conformity Assessment | 20 — Critical | 8 — Medium | Conditionally |
| RISK-004: Biometric Data Without Consent | 16 — High | 6 — Low | Yes |
| RISK-005: Deaf Community Excluded from Governance | 15 — High | 6 — Low | Yes |
| RISK-006: Model Accuracy Degradation | 9 — Medium | 3 — Low | Yes |

Conditional acceptances for RISK-001 and RISK-003 are subject to the conditions documented above. Production deployment requires resolution of both conditions before the governance gate is cleared.

---

## 5. Document Control

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | May 2026 | AI Governance Program Office | Initial release |

*This document forms part of the EU AI Act Conformity Pack for SP-AI-001 SignalPath Interpret. Review by General Counsel is required prior to any regulatory submission.*
