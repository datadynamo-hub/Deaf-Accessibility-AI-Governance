# Responsible AI Policy

**Organisation:** NorthStar Financial Services
**Policy Owner:** Chief Risk Officer
**Version:** 1.0
**Effective Date:** March 2026
**Next Review Date:** March 2027
**Classification:** Internal

---

## 1. Purpose

This policy sets out NorthStar Financial Services' commitments and requirements for the responsible development, procurement, deployment, and operation of artificial intelligence systems.

Artificial intelligence creates significant opportunities for NorthStar — to improve customer outcomes, enhance risk management, and operate more efficiently. It also creates risks: to fairness, to customer trust, to regulatory compliance, and to the broader society in which we operate.

This policy exists to ensure that we realise the benefits of AI in a manner that is consistent with our values, our regulatory obligations, and the rights of the individuals our systems affect.

---

## 2. Scope

This policy applies to:

- All AI systems developed internally by NorthStar teams
- All AI systems procured from external vendors and deployed by NorthStar
- All employees, contractors, and third parties involved in the development, procurement, deployment, or operation of AI systems on behalf of NorthStar
- All geographies in which NorthStar operates

For the purposes of this policy, an "AI system" is any machine-based system that can generate outputs — predictions, recommendations, decisions, or content — that influence real or virtual environments, based on objectives defined at design or training time. This includes but is not limited to: machine learning models, large language models, automated decision-making systems, recommendation engines, and computer vision systems.

---

## 3. Principles

NorthStar's responsible AI programme is grounded in five principles. Each principle is accompanied by the process commitments that make it operational.

---

### 3.1 Fairness

**Commitment:** AI systems used by NorthStar will not unlawfully discriminate against individuals on the basis of protected characteristics, and will be designed and monitored to identify and mitigate bias.

**What this means in practice:**
- Before deployment, AI systems that affect individuals must be assessed for potential bias across relevant protected characteristics (age, gender, ethnicity, disability, etc.)
- High-risk AI systems must undergo documented bias evaluation before go-live and at defined intervals thereafter
- Where a system is found to produce discriminatory outcomes, it will be suspended or modified until the issue is resolved
- Shortlisting, scoring, and ranking outputs that affect individuals must be reviewed by a human before being acted upon

---

### 3.2 Transparency

**Commitment:** NorthStar will be open about its use of AI where it affects individuals, and will provide meaningful explanations for AI-influenced decisions.

**What this means in practice:**
- Customers and job applicants will be informed when AI systems play a material role in decisions affecting them
- AI systems that make or inform decisions about individuals must be capable of generating human-interpretable explanations for those decisions
- Internal users of AI systems (employees using AI-generated recommendations) will be informed of the system's limitations and error rates
- NorthStar will maintain an internal AI system inventory that is available to the Board, regulators, and auditors upon request

---

### 3.3 Accountability

**Commitment:** Every AI system used by NorthStar will have a named owner who is accountable for its performance and governance.

**What this means in practice:**
- A system owner must be designated before any AI system is deployed
- System owners are responsible for ensuring the system operates within its approved purpose and within the bounds of this policy
- System owners are responsible for escalating material issues to the AI Governance Committee
- Where AI is procured from vendors, the NorthStar system owner retains accountability for how the system is used and must ensure vendor obligations are contractually captured
- The AI Governance Committee is accountable to the Board for the overall AI governance programme

---

### 3.4 Safety and Robustness

**Commitment:** AI systems will be designed, tested, and monitored to perform reliably and safely, including under adverse or unexpected conditions.

**What this means in practice:**
- AI systems must be tested against adversarial inputs and edge cases before deployment
- Performance thresholds must be defined at deployment and monitored continuously
- Degradation below defined thresholds triggers a formal review
- AI systems must not be deployed in safety-critical contexts without specific Board approval and documented safety analysis
- Human override capability must be maintained for all AI systems that affect individuals

---

### 3.5 Human Oversight

**Commitment:** NorthStar will maintain meaningful human oversight of AI systems, particularly where AI outputs affect individuals' rights, opportunities, or access to services.

**What this means in practice:**
- AI outputs that inform consequential decisions must be reviewed by a qualified human before those decisions are communicated to individuals
- "Rubber-stamp" oversight — where a human nominally reviews but never overrides — is not acceptable oversight. Oversight is only meaningful if the reviewer has the information, training, and authority to override the AI's recommendation
- High-risk AI systems must have documented human oversight procedures, including criteria for when to override
- Employees responsible for human oversight of AI systems must receive appropriate training

---

## 4. AI Lifecycle Governance Requirements

This section defines the governance requirements at each stage of the AI lifecycle.

### 4.1 Ideation and Use Case Submission

Before any AI system is developed or procured, the business owner must submit an AI Use Case Request (AUCR) to the AI Governance Programme Office. The AUCR captures:

- Business purpose and intended users
- Data sources and processing
- Affected individuals and potential harms
- Proposed oversight mechanism

All AUCRs are triaged within five business days. Triage determines the review pathway (standard or enhanced) based on preliminary risk assessment.

### 4.2 Risk Assessment and Classification

All AI systems are assessed and classified before deployment:

- **EU AI Act risk tier** (Unacceptable / High / Limited / Minimal)
- **NIST AI RMF maturity baseline** (to identify governance gaps)
- **Organisational risk rating** (combining regulatory and business risk factors)

High-risk systems require Enhanced Review, which includes external input where appropriate.

### 4.3 Approval and Go-Live

AI systems may not be deployed in a production environment without formal approval:

| Risk Tier | Approver |
|-----------|---------|
| Minimal Risk | AI Governance Programme Office |
| Limited Risk | AI Governance Programme Office + System Owner |
| High Risk | AI Governance Committee |
| Unacceptable Risk | Prohibited — no approval pathway |

Approval is documented and recorded in the AI System Inventory.

### 4.4 Monitoring and Review

Deployed AI systems are subject to ongoing monitoring:

- Performance metrics (accuracy, fairness indicators, error rates) are tracked at intervals defined at approval
- Material degradation or incident triggers a formal review
- All high-risk systems are reviewed at a minimum annually by the AI Governance Programme Office
- System owners attest annually to continued compliance with approved scope and this policy

### 4.5 Decommissioning

When an AI system is retired, the system owner is responsible for:

- Data retention and deletion in accordance with data governance policy
- Updating the AI System Inventory
- Notifying the AI Governance Programme Office
- Documenting any lessons learned for the governance programme

---

## 5. Vendor and Third-Party AI

Where NorthStar deploys AI systems developed by external vendors:

- The procurement process must include an AI governance assessment
- Contracts must include provisions requiring vendors to comply with applicable AI regulations (including the EU AI Act where applicable), provide technical documentation, notify NorthStar of material model changes, and support NorthStar's audit rights
- NorthStar system owners are accountable for the governance of vendor AI in the same way as internally developed AI
- The AI Governance Programme Office maintains a vendor AI register as part of the AI System Inventory

---

## 6. Roles and Responsibilities

| Role | Responsibility |
|------|--------------|
| **Board Risk & Audit Committee** | Oversight of AI governance programme; approval of high-risk AI systems; annual review of AI governance report |
| **Chief Risk Officer** | Policy owner; chairs AI Governance Committee |
| **AI Governance Committee** | Cross-functional governance body; approves high-risk systems; reviews incidents; oversees compliance |
| **AI Governance Programme Office** | Programme coordination; triage; documentation; training; reporting |
| **System Owners** | Accountability for individual systems; day-to-day oversight; escalation |
| **Data Protection Officer** | GDPR and AI Act data governance interface; co-reviews high-risk assessments |
| **Legal / Compliance** | Regulatory interpretation; contract review; incident escalation advice |
| **Information Security** | Cybersecurity and adversarial robustness assessment |
| **ML Engineering / Data Science** | Technical implementation of governance controls; model documentation |

---

## 7. Training

All employees involved in developing, procuring, deploying, or overseeing AI systems must complete:

- AI Governance Fundamentals (all employees in scope) — annual completion
- Human Oversight of AI Systems (employees responsible for reviewing AI outputs) — at onboarding and annually
- AI Risk Assessment (AI Governance Programme Office, system owners) — at appointment

---

## 8. Policy Breach

Breaches of this policy — including deploying an AI system without approval, failing to implement required human oversight, or misrepresenting a system's risk classification — will be treated as a conduct matter and may result in disciplinary action.

Where a policy breach has caused or risked harm to individuals or regulatory non-compliance, the Chief Compliance Officer must be notified and an incident response initiated under the AI Incident Response Procedure.

---

## 9. Review and Updates

This policy will be reviewed annually or upon material change in:

- Applicable law or regulation (including the EU AI Act or national implementing measures)
- NorthStar's AI portfolio or operating model
- Material AI incidents internally or industry-wide that warrant policy updates

The Chief Risk Officer is responsible for initiating reviews.

---

*Version history available from the AI Governance Programme Office.*
*Queries: ai-governance@northstar-financial.example*
