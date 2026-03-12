# Document 2: Risk Management Summary

**System:** HireAssist Pro (NS-AI-008)
**EU AI Act Reference:** Article 9 (Risk Management System)
**Document Type:** Deployer (NorthStar) — with provider inputs
**Version:** 1.0 — March 2026

---

## 1. Risk Management System Overview

Article 9 of the EU AI Act requires that high-risk AI systems be subject to a risk management system that is a continuous, iterative process across the system's entire lifecycle. This document summarises the risk management approach for HireAssist Pro at NorthStar Financial Services.

The risk management system covers:

- Identification and analysis of known and foreseeable risks
- Estimation and evaluation of risks in the deployment context
- Implementation of risk mitigation measures
- Residual risk assessment
- Testing against intended purpose and foreseeable misuse scenarios
- Review and update obligations

---

## 2. Risk Identification

The following risk categories have been identified for HireAssist Pro in NorthStar's deployment context:

### R1 — Discriminatory Shortlisting Outcomes

**Description:** The model may produce shortlists that systematically disadvantage candidates from protected groups (gender, age, ethnicity, disability) due to proxy discrimination, training data bias, or feature encoding.

**Likelihood:** Medium (bias risk is inherent in NLP-based CV processing; vendor has conducted bias testing — see Section 3)
**Impact:** High (employment access denied; legal and regulatory consequence)
**Risk level:** High

**Mitigation measures:**
- Vendor-supplied bias audit against EU protected characteristics (pre-deployment)
- NorthStar independent validation on a representative candidate dataset
- Ongoing monitoring of shortlisting rates by demographic proxy indicators
- Human oversight of all shortlisting decisions (see Document 4)

**Residual risk:** Medium (mitigations reduce but do not eliminate bias risk; ongoing monitoring is essential)

---

### R2 — Over-reliance by HR Users

**Description:** HR coordinators may defer to AI recommendations without exercising genuine independent judgement, effectively making the system's output the decision rather than a recommendation.

**Likelihood:** Medium (documented phenomenon in human-AI teaming)
**Impact:** Medium (undermines human oversight; increases downstream risk of R1 harm)
**Risk level:** Medium

**Mitigation measures:**
- Mandatory oversight training before system access is granted
- UI design: shortlist presented with explanation text requiring active review, not just approval
- Override rate monitoring — unusually low override rates trigger coaching
- Annual oversight effectiveness assessment

**Residual risk:** Low

---

### R3 — Scope Creep Beyond Intended Purpose

**Description:** System used beyond the approved CV screening and shortlisting function (e.g., interview scoring, internal mobility decisions).

**Likelihood:** Low (strong access controls; clear policy prohibition)
**Impact:** Medium (different use cases may carry different risk profiles requiring separate assessment)
**Risk level:** Low

**Mitigation measures:**
- Technical access controls limiting available functions to approved use case
- Policy prohibition documented and communicated
- Annual scope attestation by system owner

**Residual risk:** Low

---

### R4 — Data Minimisation Failure

**Description:** System processes more candidate personal data than is necessary for the stated purpose.

**Likelihood:** Low (system designed to process CV content only)
**Impact:** Medium (GDPR compliance; candidate trust)
**Risk level:** Low

**Mitigation measures:**
- Data flows documented and validated against GDPR minimisation principle
- Vendor data processing agreement in place
- DPO review completed

**Residual risk:** Low

---

### R5 — Vendor Model Changes Without Notification

**Description:** HireFlow Technologies Ltd updates the model without adequate notification to NorthStar, introducing changes that affect performance, fairness, or compliance.

**Likelihood:** Medium (SaaS vendors update models regularly)
**Impact:** High (material model change could re-introduce risks)
**Risk level:** High

**Mitigation measures:**
- Contract requires minimum 60 days' notice of material model changes
- Material change defined in contract: any update affecting model architecture, training data, or feature set
- NorthStar right to conduct validation testing before accepting update
- Right to delay model update to production pending NorthStar validation

**Residual risk:** Low

---

### R6 — Candidate Rights and Transparency Failure

**Description:** Candidates are not informed that AI is used in the recruitment process, or cannot exercise rights to explanation or challenge under GDPR Article 22.

**Likelihood:** Low (controls designed in from outset)
**Impact:** Medium–High (legal non-compliance; regulatory consequence; candidate harm)
**Risk level:** Medium

**Mitigation measures:**
- Candidate-facing disclosure in job application process: AI is used for initial CV screening
- Explanation capability: system provides human-readable score rationale
- Challenge mechanism: candidates who receive rejection decisions can request human review
- Legal review of candidate communications completed

**Residual risk:** Low

---

## 3. Pre-Deployment Risk Evaluation

Before deployment, the following evaluations must be completed and documented:

| Evaluation | Owner | Standard | Status |
|-----------|-------|---------|--------|
| Vendor bias audit (EU protected characteristics) | HireFlow Technologies Ltd | Demographic parity across gender, age, ethnicity proxies | Completed — results reviewed ✓ |
| NorthStar independent fairness validation | AGPO + external evaluator | Demographic parity ≤ 0.8 disparate impact ratio | In progress |
| Data protection impact assessment | DPO | GDPR Article 35 | Completed ✓ |
| Technical documentation review | AGPO + Legal | Annex IV completeness | In progress |
| Penetration and adversarial testing | Information Security | Adversarial input testing protocol | Scheduled — April 2026 |
| User acceptance testing with oversight training | HR Director + AGPO | 100% of system users trained and UAT complete | Scheduled — May 2026 |

**Go-live gate:** All evaluations must be completed and sign-off from AGPO, DPO, Legal, and HR Director received before production deployment.

---

## 4. Foreseeable Misuse Scenarios

The following reasonably foreseeable misuse scenarios have been considered and mitigated:

| Scenario | Risk | Mitigation |
|----------|------|-----------|
| HR coordinator accepts all AI recommendations without review | Autonomous AI decision-making | Training, UI friction, override rate monitoring |
| System used to screen internal transfer candidates | Out-of-scope use | Access controls, policy, scope attestation |
| Manager requests score for a specific candidate before CV submission | Gaming / bias | System does not accept individual queries outside standard batch process |
| Candidate submits CV crafted to game the AI (adversarial CV) | Model gaming | Low risk given human review; adversarial input testing planned |

---

## 5. Residual Risk Acceptance

Following implementation of all mitigation measures, the overall residual risk position is assessed as **Medium**.

The residual Medium rating reflects that:
- AI-based CV processing carries inherent bias risk that monitoring can detect but not entirely eliminate
- Human oversight remains a dependency — if oversight quality degrades, residual risk increases

The AI Governance Committee has reviewed and accepted this residual risk position as consistent with:
- NorthStar's risk appetite for operational AI risk
- The requirements of Article 9(4) (ensuring risks are reduced to an acceptable level)
- The understanding that ongoing monitoring will detect emerging issues

**Acceptance recorded:** AI Governance Committee, [pending approval date]

---

*Risk management is a continuous process. This document will be updated following any material incident, material system change, or at the annual review.*
