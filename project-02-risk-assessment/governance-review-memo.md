# Governance Review Memo

**To:** Chief Executive Officer, Board Risk and Audit Committee
**From:** AI Governance Program Office
**Subject:** SignalPath Interpret (SP-AI-001) - Governance Review and Production Deployment Decision
**Classification:** Confidential
**Date:** May 2026

---

## Purpose

This memo presents the outcome of a governance review of SignalPath Interpret (SP-AI-001), SignalPath's proprietary AI system for real-time American Sign Language interpretation in Video Relay Service calls. The review was triggered by the EU AI Act classification exercise completed in Project 1, which identified this system as high-risk with no conformity assessment initiated and no governance gate defined for production deployment.

The Board is asked to review the findings, approve the recommended conditions for production deployment, and confirm that no deployment date will be set until those conditions are met.

---

## Executive Summary

SignalPath Interpret is under active development and is being evaluated for production deployment across SignalPath's VRS operations. It would replace or supplement human interpreters for real-time ASL interpretation in calls that include medical appointments, legal proceedings, and emergency relay to 911.

The governance review has identified that the system is not ready for production deployment in its current state. Specifically:

- No conformity assessment has been initiated, which is a mandatory pre-deployment requirement for high-risk AI systems under EU AI Act Article 43
- No human oversight architecture has been defined or tested for low-confidence interpretations or emergency calls
- No bias audit has been conducted across the signer variation factors most likely to produce failures: physical limitations, regional dialect, age, and oral Deaf users
- No biometric data consent framework exists for users whose hand shape, facial expression, and body position are processed by the system
- No Deaf community input has been incorporated into design decisions, accuracy thresholds, or acceptable failure rate definitions

These are not minor documentation gaps. They represent legal exposure under the EU AI Act and FCC Part 64, direct risk of harm to the Deaf community SignalPath serves, and an organizational posture that puts product timeline ahead of community safety.

**The recommended Board decision: approve production deployment only after all five conditions in this memo are met and confirmed by the AI Governance Program Office. No deployment date should be set before that confirmation.**

---

## Findings in Detail

### 1. Classification and Regulatory Exposure

SignalPath Interpret is classified as High Risk under EU AI Act Annex III. It processes biometric data, including hand shape, facial expression, and body position, to produce outputs that directly affect access to essential communications services for a protected population. This is not a borderline classification. The obligations that follow are mandatory, not optional.

SignalPath operates as both developer and deployer of this system. That means the full weight of EU AI Act high-risk obligations applies: conformity assessment before deployment, technical documentation, session logging, human oversight architecture, accuracy and bias testing, and registration in the EU database.

None of these have been initiated.

FCC Part 64 applies independently of the EU AI Act. The functional equivalency standard requires that VRS provide access substantially equivalent to voice telephone service for hearing users. A Deaf person whose AI interpreter produces a wrong sign in a 911 call is not receiving functional equivalency. The FCC does not recognize "we were still in development" as a defense after deployment.

### 2. The Emergency Call Gap

The most urgent finding is not a documentation problem. It is a life-safety architecture problem.

SignalPath Interpret has no defined human override architecture for emergency calls. No escalation path exists when the system produces a low-confidence interpretation. No incident response plan has been built for interpretation failure during a 911 relay call.

If the system is deployed in its current state and a Deaf user places a 911 call, the AI interpreter is the only line of communication between that user and emergency services. If it gets the sign wrong and no human interpreter can take over, the call fails. That family will want to know what happened, and SignalPath will not have an answer.

This is fixable before deployment. It is not acceptable to deploy before it is fixed.

### 3. Bias Risk - Unquantified and Therefore Unacceptable

ASL interpretation AI trained on a narrow signer demographic will perform well for signers who resemble the training set and fail for everyone else. The failure modes are specific and documentable.

A Deaf user with a broken pinky cannot fully bend that finger. In ASL, a fist with pinky extended represents the letter I. That user's signs may be read by the classifier as A, M, N, or S. A human interpreter adjusts for this automatically. The AI does not, unless it was trained on signers with this variation.

We do not know whether SignalPath Interpret's training data includes this variation. We do not know the demographic composition of the training set. No bias audit has been conducted. The uncertainty is the risk. We cannot defend the system's fairness to the Deaf community, to the FCC, or to a court, because we have not tested it.

### 4. Biometric Consent Is Not Optional

Every session of SignalPath Interpret processes biometric data: hand shape, facial expression, body position. GDPR Article 9 requires explicit consent for biometric data processing. No consent framework exists. No disclosure has been provided to POC participants. No opt-out mechanism is available.

Deaf users traveling internationally from the US to EU countries while using SignalPath services are subject to GDPR protections regardless of where their account was created. Compliance is being broken accidentally, at scale, every time a Deaf traveler uses the service abroad. This is not a future risk. It is a current one.

### 5. The Deaf Community Is Not in the Room

The Board should be aware of one governance gap that does not appear in standard AI risk frameworks: the people this system is built to serve have no seat in the governance structure that decides how it is built.

Accuracy thresholds, acceptable failure rates, and escalation criteria are being defined by people who have never experienced a failed interpretation in a medical appointment or a legal proceeding. That is not how you build a system the Deaf community can trust. It is also not how you avoid the failures that produce regulatory consequences and reputational damage.

A Deaf Community Advisory Panel with documented influence on design decisions is a governance control, not a public relations gesture. It belongs in the deployment conditions.

### 6. Residual Risk After Controls

The formal risk assessment estimates that with all proposed controls in place, residual risk reduces from Critical and High to Medium across all risk categories. The residual Medium rating is driven by two factors: the bias audit results are pending and cannot confirm fairness until complete, and conformity assessment takes time even after it is initiated.

Medium residual risk is an acceptable level for a system of this kind, provided monitoring is active and controls are properly implemented from day one of production.

---

## Recommended Deployment Conditions

### Gate Conditions - No Production Deployment Until All Five Are Met

| Condition | Owner | Required By |
|-----------|-------|-------------|
| Conformity assessment formally initiated with documented owner and timeline | AI Governance Program Office and General Counsel | Before deployment date is set |
| Emergency call routing to human interpreters only, architecture documented and tested | Chief Product Officer and Head of VRS Operations | Before deployment date is set |
| Biometric data consent framework active for all users, including POC participants | Chief Privacy Officer and Legal | Before deployment date is set |
| Bias audit commissioned with independent auditor and scope defined | AI Governance Program Office | Before deployment date is set |
| Deaf Community Advisory Panel established with documented governance role | Chief Executive and AI Governance Program Office | Before deployment date is set |

### Within 60 Days of Production Deployment

| Action | Owner | Timeline |
|--------|-------|---------|
| Bias audit completed and results reviewed by AI Governance Program Office | AI Governance Program Office | 60 days |
| User feedback mechanism active in VRS interface for interpretation error flagging | Engineering Lead | 60 days |
| Monthly accuracy report by signer demographic segment established | Chief Product Officer | 60 days |

### Within 90 Days of Production Deployment

| Action | Owner | Timeline |
|--------|-------|---------|
| Conformity assessment completed | AI Governance Program Office | 90 days |
| Board-level report on SignalPath Interpret performance, compliance status, and open risk items | AI Governance Program Office | 90 days |
| Full production monitoring framework active with defined accuracy thresholds | Chief Product Officer and Engineering Lead | 90 days |

---

## Decision Requested

The Board is asked to approve one of the following:

**Option A - Conditional Deployment Approval (Recommended)**
Approve production deployment of SignalPath Interpret subject to all five gate conditions being met and confirmed by the AI Governance Program Office before a deployment date is set. This option allows the product timeline to proceed while ensuring the community is protected before the system goes live.

**Option B - Pause Development Pending Governance**
Pause production deployment planning until the governance program catches up to the development timeline. Use this period to complete the conformity assessment, bias audit, and consent framework before any deployment date is discussed. This option eliminates regulatory exposure entirely but delays the product roadmap.

**The AI Governance Program Office recommends Option A**, on the basis that the five gate conditions are achievable in parallel with ongoing development, and that a hard stop on deployment without those conditions is more protective of the Deaf community than a flexible timeline that treats governance as optional.

---

## Escalation if Gate Conditions Are Not Met

If a production deployment date is set before the AI Governance Program Office confirms all five gate conditions are met, the AI Governance Program Office will escalate to the Chief Compliance Officer and the Board Risk and Audit Committee with a recommendation to block deployment.

The Deaf community that SignalPath serves cannot be the variable that gets cut when the product timeline runs short. That is the point of a governance gate.

---

*Attachments: AI Risk Assessment - SignalPath Interpret, SP-AI-001 (May 2026)*

*Prepared by: AI Governance Program Office, SignalPath Technologies*
