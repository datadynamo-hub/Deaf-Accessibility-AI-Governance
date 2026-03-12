# EU AI Act Risk Classification — NorthStar Financial Services

**Classification Date:** March 2026
**Prepared by:** AI Governance Programme Office
**Review Due:** September 2026

---

## Classification Framework

The EU AI Act establishes four risk tiers. Classification determines the compliance obligations that attach to a system. This document records the classification decision and rationale for each AI system in NorthStar's inventory.

### Risk Tier Overview

| Tier | Regulatory Treatment |
|------|---------------------|
| **Unacceptable Risk** | Prohibited. System must not be deployed. |
| **High Risk** | Strict pre-deployment obligations. Conformity assessment required. Ongoing monitoring, logging, human oversight, and documentation mandated. |
| **Limited Risk** | Transparency obligations. Users must be informed they are interacting with an AI. |
| **Minimal Risk** | No specific regulatory obligations under the Act. General GDPR and sector rules still apply. |

---

## Classification Decisions

---

### NS-AI-001 · CreditScore Pro

**Classification: HIGH RISK**

**Legal Basis:** EU AI Act Annex III, Category 5(b) — *"AI systems intended to be used for creditworthiness assessment of natural persons or establish their credit score."*

**Rationale:**

CreditScore Pro generates a numerical score and an approve/decline recommendation that directly determines whether a retail customer receives a loan. The output is not merely advisory — it is operationalised as the primary decisioning input in NorthStar's lending workflow.

The system processes personal data including financial history, employment status, and geographic indicators (postcode). These inputs carry known bias risk; postcode in particular can function as a proxy for protected characteristics.

**Obligations triggered:**

- Conformity assessment before deployment (Article 43)
- Technical documentation (Article 11 + Annex IV)
- Logging and traceability (Article 12)
- Human oversight measures (Article 14)
- Accuracy, robustness, and cybersecurity requirements (Article 15)
- Registration in the EU database (Article 71)

**Current compliance gap:** Explainability tooling (SHAP values) has been partially implemented but is not documented to the standard required by Article 13 (transparency and provision of information to deployers). Full conformity assessment has not been conducted. **Priority: Critical.**

---

### NS-AI-002 · FraudGuard 360

**Classification: LIMITED RISK**

**Legal Basis:** Not listed in Annex III. Does not meet the threshold for high-risk classification.

**Rationale:**

FraudGuard 360 flags potentially fraudulent transactions for human review. It does not autonomously block accounts or apply penalties. All flags are reviewed by a human operator before any consequential action is taken, meaning the system does not make autonomous decisions that significantly affect natural persons.

Fraud detection in isolation is not listed as a high-risk category under Annex III. The system does not assess creditworthiness, access to essential services, or employment. The human-in-the-loop structure is a substantive, not nominal, control.

**Obligations triggered:**

- No high-risk obligations.
- General transparency obligations if outputs are used to inform customer-facing communications (Article 52 — not currently triggered).

**Note:** The vendor contract (FraudTech GmbH) does not contain EU AI Act compliance representations. Vendor management should address this at next contract renewal. Article 28 obligations on deployers apply.

**Current compliance gap:** Vendor contract alignment. **Priority: Medium.**

---

### NS-AI-003 · TalentMatch AI

**Classification: HIGH RISK**

**Legal Basis:** EU AI Act Annex III, Category 4(a) — *"AI systems intended to be used for recruitment or selection of natural persons, notably for advertising vacancies, screening or filtering applications, evaluating candidates..."*

**Rationale:**

TalentMatch AI ranks and shortlists job candidates based on CV content and other data. It directly influences which candidates are considered for roles at NorthStar, creating material consequences for individuals' employment prospects.

The use of NLP on unstructured text (CV content, LinkedIn profiles) introduces risks of proxy discrimination. Skills-based language, educational institution names, and writing style can encode correlations with protected characteristics. Without documented bias auditing, the system cannot be demonstrated to be fair.

**This system is currently the highest governance priority in the inventory.** It has been in production since November 2023 without a conformity assessment.

**Obligations triggered:**

- All high-risk obligations as per NS-AI-001 above
- Specific attention to Article 10 (data and data governance) — training data bias assessment required
- Article 14 (human oversight) — shortlisting decisions must be reviewed by a qualified human before candidate rejection

**Current compliance gap:** No conformity assessment. No bias audit. No technical documentation. Not registered in EU database. **Priority: Critical — immediate remediation required.**

---

### NS-AI-004 · SupportBot Aria

**Classification: LIMITED RISK**

**Legal Basis:** EU AI Act Article 52(1) — *"Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system."*

**Rationale:**

SupportBot Aria is a customer-facing conversational AI. It handles queries, provides information, and routes complex cases to human agents. It does not make decisions that directly affect access to services, credit, employment, or other consequential outcomes.

The system falls outside Annex III high-risk categories. However, the transparency obligation under Article 52 applies: customers must be clearly and conspicuously informed they are interacting with an automated system, not a human.

**Obligations triggered:**

- AI disclosure to end users (Article 52(1)) — partially implemented
- No high-risk conformity requirements

**Current compliance gap:** Mobile app disclosure is not yet implemented. This is a straightforward remediation. **Priority: Low.**

---

### NS-AI-005 · MarketSense Personaliser

**Classification: MINIMAL RISK**

**Legal Basis:** Not listed in Annex III. Does not trigger transparency obligations under Article 52.

**Rationale:**

The recommendation engine surfaces personalised financial product offers to opted-in customers. It does not make binding decisions. The customer retains full agency — they can accept, ignore, or opt out entirely. No consequential access decisions (credit, employment, insurance) are automated.

GDPR profiling obligations and FCA conduct rules (fair and appropriate customer communications) remain applicable and are addressed separately by the Data Protection and Compliance teams.

**Obligations triggered:** None specific to the EU AI Act.

**Current compliance gap:** None identified under the EU AI Act. Existing GDPR consent mechanism is adequate. **Priority: Monitor.**

---

### NS-AI-006 · DocIntel Underwriting

**Classification: HIGH RISK (provisional — pilot)**

**Legal Basis:** EU AI Act Annex III, Category 5(b) — potentially applicable depending on integration with underwriting decision workflow.

**Rationale:**

DocIntel extracts structured data from insurance applications. At the pilot stage, it feeds into an underwriter's workbench where humans make final decisions. If the system's outputs directly inform accept/decline underwriting decisions on insurance products, Annex III Category 5 may apply.

The classification is confirmed as **provisional** pending legal review of the production deployment architecture. The governance position is: treat as high-risk for governance planning purposes until confirmed otherwise. This is the prudent approach under a proportionality principle.

**Obligations triggered (if high-risk confirmed):** Full high-risk obligations as above. No production deployment before conformity assessment.

**Current compliance gap:** No conformity assessment — however system is pre-production. Governance review must be completed before go-live. **Priority: High (gate condition for production).**

---

### NS-AI-007 · RegulatoryRadar

**Classification: MINIMAL RISK**

**Legal Basis:** Not listed in Annex III. Internal-use system. No direct impact on natural persons outside the organisation.

**Rationale:**

RegulatoryRadar processes public text and surfaces regulatory intelligence to the internal compliance team. All outputs are reviewed by trained compliance staff. The system does not make or recommend decisions affecting any individual outside NorthStar. There is no consequential impact on natural persons.

**Obligations triggered:** None specific to the EU AI Act.

**Current compliance gap:** None identified. **Priority: Monitor.**

---

## Classification Summary

| System | Classification | Compliance Status | Priority |
|--------|---------------|-------------------|---------|
| NS-AI-001 CreditScore Pro | High Risk | Partial — gaps in documentation and conformity | Critical |
| NS-AI-002 FraudGuard 360 | Limited Risk | Adequate — vendor contract gap | Medium |
| NS-AI-003 TalentMatch AI | High Risk | Non-compliant — no conformity assessment | Critical |
| NS-AI-004 SupportBot Aria | Limited Risk | Partial — mobile disclosure outstanding | Low |
| NS-AI-005 MarketSense Personaliser | Minimal Risk | Compliant | Monitor |
| NS-AI-006 DocIntel Underwriting | High Risk (provisional) | Pre-production — gate review required | High |
| NS-AI-007 RegulatoryRadar | Minimal Risk | Compliant | Monitor |

---

*This classification document should be reviewed annually or upon material change to a system's design, purpose, or deployment context. Classification decisions are not static.*
