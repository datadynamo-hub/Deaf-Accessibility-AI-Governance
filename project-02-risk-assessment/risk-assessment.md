# AI Risk Assessment - SignalPath Interpret

**System:** SP-AI-001 - SignalPath Interpret
**Version Assessed:** POC v1.0 (pre-production)
**Assessment Date:** May 2026
**Prepared by:** AI Governance Program Office
**Review Status:** Draft - pending Board endorsement

---

## 1. System Overview

SignalPath Interpret is a proprietary AI system under active development by SignalPath Technologies. It processes biometric data, including hand shape, facial expression, and body position, to interpret American Sign Language in real time across Video Relay Service calls.

This is not a productivity tool. It is the communication channel itself for Deaf users. It handles medical appointments, legal proceedings, and emergency relay calls. When it gets a sign wrong, the consequence is not a bad user experience. It is a person who could not communicate something that mattered.

The system is pre-production. This assessment is a pre-deployment governance gate, not a post-deployment audit.

**Operator:** SignalPath Technologies, Product and Engineering
**Affected persons:** Deaf and hard-of-hearing VRS users, their hearing call recipients, and third parties on relay calls including medical providers, legal representatives, and emergency services

---

## 2. Risk Assessment Methodology

Risks are assessed on two dimensions:

**Likelihood (1-5)**

| Score | Definition |
|-------|-----------|
| 1 | Rare - unlikely to occur without deliberate action |
| 2 | Unlikely - plausible but no evidence of occurrence |
| 3 | Possible - could occur; some indicators present |
| 4 | Likely - expected to occur without intervention |
| 5 | Almost certain - evidence suggests it is occurring or will occur at deployment |

**Impact (1-5)**

| Score | Definition |
|-------|-----------|
| 1 | Negligible - no material harm to individuals or organization |
| 2 | Minor - limited harm; recoverable |
| 3 | Moderate - meaningful harm to individuals; reputational damage possible |
| 4 | Significant - serious harm to individuals; regulatory consequence likely |
| 5 | Severe - systemic harm; regulatory sanction; potential loss of life |

**Risk Score = Likelihood x Impact**
**Risk levels:** Low (1-6) - Medium (7-14) - High (15-19) - Critical (20-25)

---

## 3. Risk Register

---

### RISK-001 - Signer Variation and Demographic Bias in Training Data

**Description:**
SignalPath Interpret requires training data representing the full range of how Deaf people actually sign. If the training set skews toward a narrow demographic, the model performs well for signers who look like the training data and fails for everyone else. Known variation factors include regional dialect, age-related signing differences, non-native ASL signers, oral Deaf users, physical limitations, and signer fatigue.

One specific and documentable failure mode: a Deaf user with a broken pinky cannot fully bend that finger. In ASL, a fist with pinky extended represents the letter I. Without the ability to bend the pinky, that user may produce signs a classifier reads as A, M, N, or S instead of I. A human interpreter recognizes this as a physical variation and adjusts. The AI classifier produces a different letter. In a medical or legal context, that is not a trivial error.

Training data composition has not been documented. No bias audit has been conducted. Signer demographic diversity in the training set is unknown.

**Affected groups:** Deaf users with physical limitations, regional dialect variation, non-native ASL signers, oral Deaf users, older signers.

**Likelihood:** 4 - Demographic bias in biometric AI training data is well-documented. No audit has been performed to demonstrate this system is an exception. Physical limitation failure modes are unaddressed in current POC documentation.

**Impact:** 4 - Systematic interpretation failures for specific Deaf user populations constitutes discriminatory service delivery under ADA Title IV functional equivalency standards. In emergency relay contexts, impact escalates to 5.

**Inherent Risk Score: 16 - HIGH**

**Proposed Controls:**
- Commission independent bias audit across signer demographics before production deployment: regional dialect, age, physical limitation, non-native ASL, oral Deaf users
- Document training data provenance: sources, consent basis, signer demographic breakdown
- Define minimum acceptable accuracy thresholds per demographic segment, not just aggregate accuracy
- Implement confidence scoring: low-confidence interpretations trigger automatic human interpreter handoff
- Track interpretation accuracy by user demographic segment on an ongoing basis post-deployment

**Residual Risk Score (with controls): 8 - MEDIUM**

**Control Owner:** Chief Product Officer and AI Governance Program Office

---

### RISK-002 - Emergency Call Failure with No Human Override Architecture

**Description:**
VRS calls include emergency relay calls to 911 and other emergency services. If SignalPath Interpret misinterprets a sign during an emergency call and no human interpreter can override, the result is a failed emergency communication. FCC Part 64 establishes a functional equivalency standard: relay services must provide access substantially equivalent to voice telephone service for hearing users. A 911 caller who cannot be understood is not receiving functional equivalency.

No human-in-the-loop architecture has been defined for emergency calls. No incident response plan exists for interpretation failure during emergency relay. The current POC does not address this scenario.

**Likelihood:** 3 - Emergency calls are a fraction of total VRS volume, but interpretation failures have occurred in POC testing. Without a defined override architecture, a failure during an emergency call is a matter of when, not if.

**Impact:** 5 - Failure to relay an emergency call correctly is a life-safety event. FCC Part 64 regulatory consequence is severe. Legal liability is extreme. If an AI interpreter misunderstands the sign for "fire" or "unconscious" and someone dies, that family will want answers. That is not a hypothetical.

**Inherent Risk Score: 15 - HIGH**

**Proposed Controls:**
- All calls to 911 and designated emergency numbers route to a human interpreter by default until AI accuracy benchmarks for emergency vocabulary are independently verified
- Implement mandatory human interpreter standby for any call where AI confidence score falls below a defined threshold
- Build and test an incident response playbook for interpretation failure during emergency relay before production deployment
- Log all interpretation sessions with confidence scores and human override events for audit and model feedback

**Residual Risk Score (with controls): 6 - LOW**

**Control Owner:** Chief Product Officer and Head of VRS Operations
**Timeline:** This control must be implemented and tested before any production deployment. It is a non-negotiable gate condition.

---

### RISK-003 - No Conformity Assessment Before Production Deployment

**Description:**
SignalPath Interpret is classified as High Risk under EU AI Act Annex III. High-risk AI systems require a mandatory conformity assessment before deployment under Article 43. No conformity assessment has been initiated. The system is being evaluated for a production deployment timeline that does not account for this requirement.

Technical documentation under Article 11 and Annex IV has not been prepared. Logging and traceability architecture under Article 12 has not been defined. A formal human oversight model under Article 14 has not been documented.

**Likelihood:** 5 - The system is pre-production and none of these requirements have been initiated. Without intervention, the system will deploy non-compliant.

**Impact:** 4 - Deploying a high-risk AI system without conformity assessment is direct EU AI Act non-compliance. Regulatory sanction, reputational damage, and deployment suspension are all real consequences. SignalPath's EU-adjacent operations, GDPR biometric data obligations, and the reality that US Deaf users travel internationally make the regulatory surface area real, not theoretical.

**Inherent Risk Score: 20 - CRITICAL**

**Proposed Controls:**
- Initiate conformity assessment immediately. Do not set a production deployment date until this process is underway.
- Prepare technical documentation package per Article 11 and Annex IV
- Define and implement logging architecture for all interpretation sessions per Article 12
- Document human oversight model per Article 14 before deployment
- Establish a formal governance gate: production deployment requires AI Governance Program Office sign-off confirming conformity requirements are met

**Residual Risk Score (with controls): 8 - MEDIUM**

**Control Owner:** AI Governance Program Office and General Counsel
**Timeline:** Immediate. No production deployment date should be set until conformity assessment is initiated.

---

### RISK-004 - Biometric Data Processing Without a Consent Framework

**Description:**
SignalPath Interpret processes biometric data: hand shape, facial expression, and body position. Under GDPR Article 9, biometric data used to identify individuals is a special category requiring explicit consent. VRS users currently receive no explicit disclosure that their biometric data is being processed by an AI system. No opt-out mechanism exists.

Deaf users traveling to EU countries while using SignalPath services add additional GDPR surface area. An American Deaf user making a VRS call from France is subject to GDPR protections regardless of where their account was created.

**Likelihood:** 4 - No biometric consent framework exists for this system. Every POC session has processed biometric data without a proper consent structure.

**Impact:** 4 - GDPR Article 9 violations carry fines up to 4% of global annual turnover. The reputational harm to a company whose core market is the Deaf community would be compounded by the nature of the violation: collecting biometric data from Deaf users without their knowledge or consent.

**Inherent Risk Score: 16 - HIGH**

**Proposed Controls:**
- Develop an explicit consent framework before any expanded POC or production deployment: clear disclosure that AI processes biometric data, an opt-out mechanism, and plain-language explanation available in ASL video format, not English text only
- Update the privacy notice to reflect biometric data processing
- Confirm legal basis for biometric data processing under GDPR Article 9(2)
- Conduct a GDPR Data Protection Impact Assessment per Article 35: processing biometric data at scale triggers a mandatory DPIA
- Apply the consent framework to all current POC participants immediately

**Residual Risk Score (with controls): 6 - LOW**

**Control Owner:** Chief Privacy Officer and Legal
**Timeline:** Consent framework required before any expansion of POC testing beyond internal users.

---

### RISK-005 - Deaf Community Excluded from Governance and Design Decisions

**Description:**
SignalPath Interpret is built to serve the Deaf community. No Deaf person currently holds a seat in the governance structure where decisions about this system are made. The AI Governance Program Office, the product team, and the Board do not include Deaf representation. Accuracy thresholds, failure mode priorities, and acceptable error rates are being decided by people who have never experienced a failed interpretation in a medical appointment or a 911 call.

This is not a diversity statement. It is a governance risk. Decisions made without community input produce systems that fail the community in ways the decision-makers never anticipated and cannot detect from the outside.

**Likelihood:** 5 - This is the current organizational state. No Deaf community advisory structure exists for this system.

**Impact:** 3 - Design failures caused by community exclusion compound over time and are often attributed to technical limitations rather than governance gaps. Reputational risk to SignalPath is significant given the company's market position in the Deaf community.

**Inherent Risk Score: 15 - HIGH**

**Proposed Controls:**
- Establish a Deaf Community Advisory Panel as a named role in the governance structure before production deployment. This is not a focus group. It is a structured input mechanism with documented influence on design decisions.
- Require Deaf user testing at each model evaluation checkpoint
- Document community input received and decisions made as a result, or explicit rationale for decisions made against community input
- Include Deaf community representation in Board-level risk reporting on this system

**Residual Risk Score (with controls): 6 - LOW**

**Control Owner:** Chief Executive and AI Governance Program Office

---

### RISK-006 - Model Accuracy Degradation After Deployment

**Description:**
ASL is a living language. Slang evolves. Regional signing shifts over time. A model trained on 2024 signing data will encounter signing patterns in 2026 and beyond that were not in its training set. Without ongoing monitoring, retraining, and accuracy validation, model performance degrades while the organization assumes it is still performing at deployment-level accuracy.

The risk is not whether degradation happens. It is whether it gets detected before users are harmed.

**Likelihood:** 3 - Linguistic drift is inevitable. The question is whether a monitoring system exists to catch it before it affects users.

**Impact:** 3 - Accuracy degradation that goes undetected harms users without the organization's knowledge. When detected through complaints or regulatory review, the failure to monitor compounds the consequences.

**Inherent Risk Score: 9 - MEDIUM**

**Proposed Controls:**
- Define a production monitoring framework before deployment: accuracy tracked against defined thresholds continuously
- Establish a retraining cadence with governance approval required for model updates that materially change performance characteristics
- Build a user feedback mechanism into the VRS interface so Deaf users can flag interpretation errors directly
- Quarterly accuracy report reviewed by the AI Governance Program Office

**Residual Risk Score (with controls): 3 - LOW**

**Control Owner:** Chief Product Officer and Engineering Lead

---

## 4. Risk Summary Matrix

| Risk ID | Risk | Inherent Score | Level | Residual Score | Level |
|---------|------|---------------|-------|----------------|-------|
| RISK-001 | Signer variation and demographic bias in training data | 16 | High | 8 | Medium |
| RISK-002 | Emergency call failure with no human override architecture | 15 | High | 6 | Low |
| RISK-003 | No conformity assessment before production deployment | 20 | Critical | 8 | Medium |
| RISK-004 | Biometric data processing without a consent framework | 16 | High | 6 | Low |
| RISK-005 | Deaf community excluded from governance and design decisions | 15 | High | 6 | Low |
| RISK-006 | Model accuracy degradation after deployment | 9 | Medium | 3 | Low |

---

## 5. Residual Risk Position

With all proposed controls in place, the residual risk position is assessed as **MEDIUM**. Two risks remain at medium after controls are applied:

- RISK-001 (signer variation bias) remains medium because bias audit results are not yet known. Controls reduce likelihood but cannot eliminate the risk until the audit is complete and results reviewed.
- RISK-003 (conformity assessment) remains medium because initiating the process does not complete it. The system cannot be treated as compliant until the assessment is finished, regardless of intent.

**Acceptance recommendation:** Conditional. SignalPath Interpret must not proceed to production in its current state. It may proceed to expanded POC testing only if the following minimum controls are in place first:

1. Biometric data consent framework applied to all POC participants (RISK-004)
2. Emergency calls route to human interpreters only during POC. AI is not used for emergency relay until accuracy benchmarks are independently verified. (RISK-002)
3. Conformity assessment formally initiated with a documented owner and timeline (RISK-003)

Full production deployment requires: completed conformity assessment, bias audit results reviewed and acted on, human oversight architecture documented and tested, and AI Governance Program Office sign-off. No production deployment date should be set until all four conditions are met.

---

## 6. Recommended Human Oversight Model

Human oversight for SignalPath Interpret must be built into the architecture. Procedural assumptions are not enough for a system at this risk level.

**Minimum viable oversight (required before any production deployment):**
- Confidence scoring active on all interpretations. Every output carries a score.
- Low-confidence threshold defined: interpretations below the threshold trigger automatic handoff to a human interpreter. The user is not notified of a failure. The system handles it.
- Emergency call routing: all calls to 911 and designated emergency numbers go to a human interpreter, no exceptions, regardless of AI confidence score
- Session logging: all interpretation sessions logged with confidence scores, human override events, and outcome flags

**Enhanced oversight (within 60 days of production deployment):**
- User feedback mechanism active. Deaf users can flag interpretation errors in real time.
- Human interpreter review of all flagged sessions within 24 hours
- Monthly accuracy report by signer demographic segment reviewed by the AI Governance Program Office

**Governance oversight (within 90 days of production deployment):**
- Deaf Community Advisory Panel receives quarterly accuracy and incident summary
- Board-level report on SignalPath Interpret performance, compliance status, and open risk items
- Annual full risk assessment review by the AI Governance Program Office

---

*This assessment reflects pre-production status as of May 2026. Risk ratings must be reviewed before production deployment, after any material change to the system or its training data, and upon new regulatory guidance from the FCC, NIST, or EU AI Act implementing authorities.*
