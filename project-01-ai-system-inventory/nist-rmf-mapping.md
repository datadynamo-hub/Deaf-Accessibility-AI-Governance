# NIST AI RMF Mapping — NorthStar Financial Services

**Framework Reference:** NIST AI Risk Management Framework (AI RMF 1.0)
**Mapping Date:** March 2026

---

## Purpose

This document maps each AI system in NorthStar's inventory against the four core functions of the NIST AI RMF. It identifies which practices are in place, which are absent, and where the most significant governance gaps exist.

The four functions are:

| Function | Core Question |
|----------|--------------|
| **GOVERN** | Are the right accountability structures, policies, and culture in place? |
| **MAP** | Have we identified and contextualised the risks associated with this system? |
| **MEASURE** | Have we analysed and assessed those risks in a rigorous, documented way? |
| **MANAGE** | Are we actively treating risks, monitoring systems, and ready to respond? |

Maturity is rated 1–4:

| Level | Description |
|-------|-------------|
| 1 | Initial — ad hoc or absent |
| 2 | Developing — some practices exist but inconsistently applied |
| 3 | Defined — documented and repeatable processes in place |
| 4 | Optimised — continuously improved with feedback loops |

---

## System Mappings

---

### NS-AI-001 · CreditScore Pro (High Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | System has a named owner (Head of Credit Risk). No formal AI governance policy references this system. No AI-specific accountability framework in place. | No AI governance charter. No defined escalation path for model risk decisions. | 2 |
| **MAP** | Risk identification has been performed informally by the data science team at build time. Use case context is understood. | No formal risk mapping document. Affected population (loan applicants) not formally documented with demographic breakdown. | 2 |
| **MEASURE** | SHAP explainability tooling partially implemented. No structured bias evaluation against protected groups has been conducted. No performance degradation thresholds defined. | Bias audit required. Accuracy/fairness metrics not formally tracked post-deployment. | 2 |
| **MANAGE** | Model performance is monitored informally. No defined response procedure if model drift is detected. No incident classification for AI failures. | Model governance plan needed. Incident response playbook required. | 1 |

**Overall Maturity: 1.75 (Developing)**
**Priority Actions:** Conduct bias audit; document risk mapping; define model monitoring thresholds; create incident response procedure.

---

### NS-AI-002 · FraudGuard 360 (Limited Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | Named owner in Payment Operations. Vendor relationship managed through procurement. No AI-specific governance oversight. | Vendor AI Act compliance not contractually required. No AI policy reference. | 3 |
| **MAP** | Use case and risk context well understood by operations team. Human review process documented in operational runbook. | Risk mapping not formalised in AI governance terms. Affected population data not captured. | 3 |
| **MEASURE** | Vendor provides quarterly performance reports (precision/recall on flagged transactions). False positive rate tracked. | No independent validation of vendor metrics. No fairness assessment. | 3 |
| **MANAGE** | Human review workflow in place. Escalation path for disputed blocks exists. | No documented AI-specific incident classification. Vendor SLA covers uptime — not model quality degradation. | 3 |

**Overall Maturity: 3.0 (Defined)**
**Priority Actions:** Update vendor contract with AI Act compliance clauses; formalise risk mapping document.

---

### NS-AI-003 · TalentMatch AI (High Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | HR Director listed as system owner but has not received AI governance training. No formal accountability structure for AI-assisted recruitment decisions. | No AI governance policy. No training for HR staff using AI outputs. No Board-level visibility of this system's risk classification. | 1 |
| **MAP** | System purpose is documented in procurement records. Risk context has not been formally assessed. | No risk identification exercise has been conducted. Potential for proxy discrimination not assessed. Affected population (job applicants) not documented. | 1 |
| **MEASURE** | No bias evaluation has been performed on the vendor's model. Shortlisting outcomes are not tracked by demographic group. | No fairness metrics. No accuracy benchmarks. No documentation of training data provenance from vendor. | 1 |
| **MANAGE** | No AI monitoring in place. No defined procedure if discriminatory outcomes are identified. | No incident response capability for this system. No model monitoring. | 1 |

**Overall Maturity: 1.0 (Initial)**
**Priority Actions:** Immediate: suspend use or implement manual override for all shortlisting decisions. Near-term: conduct full risk assessment, require vendor to supply training data and bias audit documentation, implement structured human review before any candidate rejection.

---

### NS-AI-004 · SupportBot Aria (Limited Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | Head of Customer Experience is accountable. Vendor managed through Customer Experience team. | No formal AI governance policy. Chatbot performance not reviewed at governance level. | 3 |
| **MAP** | Use case context clear. Customer interaction risks understood (misinformation, inappropriate responses). Low-stakes — no consequential decisions made. | Risk mapping is informal. | 3 |
| **MEASURE** | Customer satisfaction scores and escalation rates tracked. AI disclosure compliance monitored on web channel. | Mobile channel disclosure not implemented — not yet measured. | 3 |
| **MANAGE** | Escalation to human agent on low-confidence responses is automated. Customer complaints process covers chatbot interactions. | No formal AI incident classification. | 3 |

**Overall Maturity: 3.0 (Defined)**
**Priority Actions:** Implement mobile disclosure; add formal AI incident category to complaints framework.

---

### NS-AI-005 · MarketSense Personaliser (Minimal Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | CMO accountable. GDPR consent framework in place. Marketing governance review cycle established. | No AI-specific governance layer — adequate given risk level. | 3 |
| **MAP** | Low risk profile documented informally. Customer data use governed by privacy notices. | Minimal gaps given risk classification. | 3 |
| **MEASURE** | Recommendation performance tracked (click-through, conversion). GDPR opt-out rates monitored. | No fairness assessment — appropriate given minimal risk tier. | 3 |
| **MANAGE** | Opt-out mechanism functional. Customer data deletion requests processed under GDPR workflow. | No specific AI management gaps at this risk tier. | 3 |

**Overall Maturity: 3.0 (Defined)**
**Priority Actions:** None immediate. Maintain annual review.

---

### NS-AI-006 · DocIntel Underwriting (High Risk — provisional, pilot)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | Underwriting Head accountable for pilot. ML Engineering team responsible for model. No formal AI governance review conducted pre-pilot. | No governance sign-off on pilot scope. No defined criteria for production go/no-go decision. | 1 |
| **MAP** | Pilot risk assessment in progress. System purpose and data flows being documented. | Risk mapping incomplete. Human oversight in pilot workflow needs formal documentation. | 1 |
| **MEASURE** | Extraction accuracy tracked during pilot (field-level precision/recall). No bias assessment yet. | Performance thresholds for production readiness not defined. | 1 |
| **MANAGE** | Pilot monitored by ML Engineering. No production monitoring framework in place. | Production monitoring plan required before go-live. | 1 |

**Overall Maturity: 1.0 (Initial)**
**Priority Actions:** Establish governance gate criteria for production deployment. Complete risk mapping. Define accuracy and fairness thresholds. Conduct legal review to confirm high-risk classification before production go-live.

---

### NS-AI-007 · RegulatoryRadar (Minimal Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | CCO accountable. Vendor managed through procurement. | No AI-specific governance — adequate at this risk level. | 3 |
| **MAP** | Internal use, low stakes. Compliance team validates all outputs. | No gaps at this risk level. | 3 |
| **MEASURE** | Alert relevance and false positive rate tracked informally by compliance team. | Informal tracking is adequate given risk profile. | 3 |
| **MANAGE** | Compliance team reviews all outputs. Vendor SLA in place. | No AI-specific gaps. | 3 |

**Overall Maturity: 3.0 (Defined)**
**Priority Actions:** None. Annual review sufficient.

---

## Portfolio-Level Summary

| System | EU AI Act Tier | RMF Maturity | Action Priority |
|--------|---------------|-------------|----------------|
| NS-AI-001 CreditScore Pro | High Risk | 1.75 | Critical |
| NS-AI-002 FraudGuard 360 | Limited Risk | 3.0 | Medium |
| NS-AI-003 TalentMatch AI | High Risk | 1.0 | Critical — immediate |
| NS-AI-004 SupportBot Aria | Limited Risk | 3.0 | Low |
| NS-AI-005 MarketSense Personaliser | Minimal Risk | 3.0 | Monitor |
| NS-AI-006 DocIntel Underwriting | High Risk (provisional) | 1.0 | High (pre-production gate) |
| NS-AI-007 RegulatoryRadar | Minimal Risk | 3.0 | Monitor |

**Portfolio risk concentration:** Three of NorthStar's seven AI systems are high-risk under the EU AI Act. Two of these (TalentMatch AI and CreditScore Pro) are in production with insufficient governance controls. This represents material regulatory exposure. A remediation programme should be initiated immediately.

---

*Next review: September 2026, or upon any new AI system deployment.*
