# AI Risk Assessment — TalentMatch AI

**System:** NS-AI-003 · TalentMatch AI
**Version Assessed:** v2.3 (as deployed)
**Assessment Date:** March 2026
**Prepared by:** AI Governance Programme Office
**Review Status:** Draft — pending Board endorsement

---

## 1. System Overview

TalentMatch AI is a vendor-supplied NLP-based recruitment tool deployed by NorthStar Financial Services' HR department. It ingests candidate CVs and job descriptions, performs semantic matching, and generates a ranked shortlist of candidates with an individual fit score per applicant.

The tool was deployed in November 2023 and is currently used in all NorthStar hiring processes across all business units and geographies (primarily Germany and the Netherlands).

**Deployer:** NorthStar Financial Services (HR Department)
**Provider:** HireFlow Technologies Ltd
**Affected persons:** External job applicants

---

## 2. Risk Assessment Methodology

Risks are assessed on two dimensions:

**Likelihood (1–5)**

| Score | Definition |
|-------|-----------|
| 1 | Rare — unlikely to occur without deliberate action |
| 2 | Unlikely — plausible but no evidence of occurrence |
| 3 | Possible — could occur; some indicators present |
| 4 | Likely — expected to occur without intervention |
| 5 | Almost certain — evidence suggests it is occurring |

**Impact (1–5)**

| Score | Definition |
|-------|-----------|
| 1 | Negligible — no material harm to individuals or organisation |
| 2 | Minor — limited harm; recoverable |
| 3 | Moderate — meaningful harm to individuals; reputational damage possible |
| 4 | Significant — serious harm to individuals; regulatory consequence likely |
| 5 | Severe — systemic harm; regulatory sanction; major reputational damage |

**Risk Score = Likelihood × Impact**
**Risk levels:** Low (1–6) · Medium (7–14) · High (15–19) · Critical (20–25)

---

## 3. Risk Register

---

### RISK-001 · Proxy Discrimination via Training Data Bias

**Description:**
TalentMatch AI was trained on historical recruitment data from HireFlow's customers. If that historical data reflects past discriminatory hiring patterns (e.g., systematic underrepresentation of women in technical roles, or candidates from certain educational backgrounds), the model will learn and replicate those patterns. The model may use surface features — writing style, school names, gap years, name inference — as proxies for protected characteristics.

**Affected groups:** Applicants from protected groups including women, ethnic minorities, older workers, and those with non-linear career histories.

**Likelihood:** 4 — Historical hiring data routinely reflects discriminatory patterns. This is a well-documented phenomenon in NLP-based recruitment tools. No bias audit has been performed to demonstrate otherwise.

**Impact:** 4 — Systemic exclusion of protected-group candidates from shortlists constitutes indirect discrimination under EU employment law (Equal Treatment Directive). Regulatory and reputational consequences are significant.

**Inherent Risk Score: 16 — HIGH**

**Proposed Controls:**
- Require vendor to supply training data provenance and bias audit documentation
- Commission independent fairness evaluation across protected characteristics (gender, age, ethnicity proxy)
- Track shortlisting rates by demographic segment on an ongoing basis
- Implement mandatory human review of all shortlists before candidate rejection communications are sent

**Residual Risk Score (with controls): 8 — MEDIUM**

**Control Owner:** HR Director + Chief People Officer

---

### RISK-002 · Lack of Explainability for Adverse Decisions

**Description:**
Candidates who are not shortlisted cannot currently receive a meaningful explanation for why they were rejected. The system produces a fit score but does not provide human-interpretable reasoning. Under the EU AI Act Article 13 and Article 86 of the GDPR (right to explanation for automated decisions), affected individuals have the right to understand the basis of decisions that significantly affect them.

**Likelihood:** 5 — The system is currently in production with no explanation capability. Every rejection is currently unexplainable beyond a score.

**Impact:** 3 — Individual harm (applicants cannot appeal or understand rejection); regulatory risk if challenged; reputational risk if publicised.

**Inherent Risk Score: 15 — HIGH**

**Proposed Controls:**
- Require vendor to implement or expose an explanation API that provides plain-language reasons for low scores
- Implement human review as the decision point — the AI shortlist is an input, not the decision
- Update candidate communications to reflect that human judgment, not automated decision-making, determines rejection
- Review candidate-facing privacy notice to ensure it reflects current automated processing practices

**Residual Risk Score (with controls): 6 — LOW**

**Control Owner:** HR Director + Legal/Compliance

---

### RISK-003 · Absence of Human Oversight in Rejection Workflow

**Description:**
Current workflow: HR coordinators upload CVs → TalentMatch generates ranked shortlist → candidates below a defined threshold score receive automated rejection emails. There is no mandatory human review step before rejections are sent. The AI system is effectively making final employment decisions autonomously.

Under EU AI Act Article 14, high-risk AI systems must enable human oversight, including the ability for humans to override outputs and refrain from using outputs. The current workflow does not meet this requirement.

**Likelihood:** 5 — This is the current workflow as documented.

**Impact:** 4 — Autonomous rejection of candidates by AI constitutes a high-risk AI system making binding decisions without human oversight. Direct EU AI Act non-compliance. Potential discrimination and employment law liability.

**Inherent Risk Score: 20 — CRITICAL**

**Proposed Controls:**
- Immediately implement a mandatory human review gate: HR coordinators must review and approve all rejection decisions before they are communicated to candidates
- The AI shortlist should be treated as a recommendation, not a decision
- Define the criteria HR coordinators use to override the AI's ranking
- Log all instances where the human decision diverges from the AI recommendation (provides model feedback data)

**Residual Risk Score (with controls): 8 — MEDIUM**

**Control Owner:** HR Director
**Timeline:** Immediate — this control must be implemented before next hiring cycle

---

### RISK-004 · Training Data Provenance and Data Quality

**Description:**
HireFlow Technologies Ltd has not supplied documentation of the training data used to build TalentMatch AI's model. NorthStar cannot confirm what data was used, whether it was lawfully obtained, whether it contains NorthStar's own historical candidates (which would raise separate GDPR concerns), or whether it is representative of the applicant pool NorthStar actually receives.

**Likelihood:** 4 — Vendor has not provided this information despite deployment. Gaps are probable.

**Impact:** 3 — Data quality issues may degrade model performance; unlawfully sourced training data creates GDPR liability; non-representative training data compounds bias risk.

**Inherent Risk Score: 12 — MEDIUM**

**Proposed Controls:**
- Issue formal information request to HireFlow: training data sources, processing basis, data subjects, fairness testing methodology, model card
- Include EU AI Act Article 10 compliance requirements in next contract renewal
- If vendor cannot provide adequate documentation, treat as material contract breach and initiate alternative procurement assessment

**Residual Risk Score (with controls): 4 — LOW**

**Control Owner:** Procurement + Legal

---

### RISK-005 · Scope Creep Beyond Intended Purpose

**Description:**
TalentMatch AI was procured for initial CV screening and shortlisting. There is a risk that over time its outputs are used beyond this intended scope — for example, informing interview question selection, influencing salary offer decisions, or being repurposed for internal mobility and promotion decisions. Each expansion of scope may carry different risk profiles and require separate assessment.

**Likelihood:** 3 — Scope creep is common with convenient AI tools. No formal use-case boundary policy exists.

**Impact:** 3 — Expanded use in promotion decisions would constitute a different high-risk use case requiring separate conformity assessment.

**Inherent Risk Score: 9 — MEDIUM**

**Proposed Controls:**
- Document the permitted use scope in the system's governance record
- Require a new governance review and risk assessment before any expansion of the system's use
- HR Director to attest annually to permitted scope adherence

**Residual Risk Score (with controls): 3 — LOW**

**Control Owner:** HR Director

---

### RISK-006 · Vendor Dependency and Continuity Risk

**Description:**
NorthStar's recruitment workflow is dependent on a single vendor (HireFlow Technologies Ltd). If the vendor ceases to operate, withdraws the product, or makes changes to the model that degrade performance, NorthStar has no fallback capability.

**Likelihood:** 2 — Vendor is an established SaaS provider but is a relatively small company.

**Impact:** 2 — Disruption to recruitment workflow; manageable.

**Inherent Risk Score: 4 — LOW**

**Proposed Controls:**
- Ensure contract includes data portability and export rights
- Maintain capability to revert to manual CV screening during any vendor disruption
- Include model change notification requirements in contract

**Residual Risk Score (with controls): 2 — LOW**

**Control Owner:** Procurement

---

## 4. Risk Summary Matrix

| Risk ID | Risk | Inherent Score | Level | Residual Score | Level |
|---------|------|---------------|-------|----------------|-------|
| RISK-001 | Proxy discrimination via training data bias | 16 | High | 8 | Medium |
| RISK-002 | Lack of explainability for adverse decisions | 15 | High | 6 | Low |
| RISK-003 | Absence of human oversight in rejection workflow | 20 | Critical | 8 | Medium |
| RISK-004 | Training data provenance and data quality | 12 | Medium | 4 | Low |
| RISK-005 | Scope creep beyond intended purpose | 9 | Medium | 3 | Low |
| RISK-006 | Vendor dependency and continuity risk | 4 | Low | 2 | Low |

---

## 5. Residual Risk Position

With all proposed controls in place, the residual risk position is assessed as **MEDIUM**. Two risks (RISK-001 and RISK-003) remain at medium residual risk because:

- Bias audit results are not yet known — controls reduce likelihood but cannot eliminate the risk until the audit is complete
- Human oversight controls reduce but do not eliminate the risk of discriminatory outcomes — ongoing monitoring is required

**Acceptance recommendation:** Conditional. The system should not continue in its current configuration. It may continue to operate **only** if the following minimum controls are implemented immediately:

1. Mandatory human review of all shortlisting and rejection decisions (RISK-003)
2. Updated candidate-facing communications removing references to automated decision-making as the basis for rejection (RISK-002)
3. Formal information request to HireFlow Technologies Ltd for training data documentation (RISK-004)

A full conformity assessment and independent bias audit must be completed within 90 days. If controls 1–3 cannot be implemented before the next hiring cycle, the system should be suspended pending remediation.

---

## 6. Recommended Human Oversight Model

Human oversight for TalentMatch AI should be structured as follows:

**Minimum viable oversight (immediate):**
- HR coordinator reviews AI-generated shortlist and approves or modifies it before any candidate communication
- HR coordinator records whether they accepted or modified the AI recommendation and the reason for any modification
- No rejection email is sent without HR coordinator approval

**Enhanced oversight (within 60 days):**
- Hiring manager reviews shortlist in addition to HR coordinator for roles above Grade 5
- Monthly review of shortlisting rate by demographic indicator (where data is available)
- Quarterly report to HR Director on AI recommendation acceptance/override rate and patterns

**Governance oversight (within 90 days):**
- AI Governance Committee receives quarterly summary of TalentMatch AI performance and fairness metrics
- Annual review of system risk assessment by AI Governance Programme Office

---

*This assessment is point-in-time. Risk ratings should be reviewed following any material change to the system, its use, or the regulatory environment.*
