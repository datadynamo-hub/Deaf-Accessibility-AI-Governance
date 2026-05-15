# Responsible AI Policy

**Organization:** SignalPath Technologies
**Policy Owner:** Chief Risk Officer
**Version:** 1.0
**Effective Date:** May 2026
**Next Review Date:** May 2027
**Classification:** Internal

---

## 1. Purpose

This policy sets out SignalPath Technologies' commitments and requirements for the responsible development, procurement, deployment, and operation of artificial intelligence systems.

AI creates real opportunities for SignalPath: better accessibility outcomes for Deaf and hard-of-hearing users, more reliable relay services, and more accurate captioning and interpretation. It also creates risks that do not exist in most industries. Our users depend on our systems to communicate things they cannot communicate any other way: emergency calls, medical appointments, legal proceedings, personal conversations. When an AI system fails at SignalPath, the consequence is not a bad customer experience. It is a person who could not be understood when it mattered most.

This policy exists to ensure that SignalPath realizes the benefits of AI in a manner consistent with our values, our regulatory obligations, and the rights of the Deaf and hard-of-hearing individuals our systems serve.

Governance at SignalPath is a service to our users, not a constraint on our engineers.

---

## 2. Scope

This policy applies to:

- All AI systems developed internally by SignalPath teams
- All AI systems procured from external vendors and deployed by SignalPath
- All employees, contractors, and third parties involved in the development, procurement, deployment, or operation of AI systems on behalf of SignalPath
- All geographies in which SignalPath operates, including US, Canadian, and UK operations

For the purposes of this policy, an "AI system" is any machine-based system that can generate outputs, including predictions, recommendations, decisions, or content, that influence real or virtual environments based on objectives defined at design or training time. This includes but is not limited to: machine learning models, large language models, automated decision-making systems, recommendation engines, and computer vision systems.

SignalPath operates AI systems across four categories: core product AI (SignalPath Interpret, SignalPath Forum, Express Call Routing ML, SignalPath CaptionLine), enterprise-embedded AI (tools used internally across business functions), compliance and regulatory monitoring AI, and third-party vendor AI deployed in connection with SignalPath operations. This policy applies to all four categories.

---

## 3. Principles

SignalPath's responsible AI program is grounded in five principles. Each principle is accompanied by the process commitments that make it operational. Principles without process are decoration.

---

### 3.1 Fairness

**Commitment:** AI systems used by SignalPath will not unlawfully discriminate against individuals on the basis of protected characteristics, and will be designed and monitored to identify and mitigate bias.

**What this means in practice:**

- Before deployment, AI systems that affect individuals must be assessed for potential bias across relevant protected characteristics, including disability status, age, signing style, regional ASL dialect, and physical mobility
- "Deaf users" is not a homogenous population. An AI system trained primarily on native ASL signers may systematically fail oral Deaf users, signers with physical limitations affecting hand movement, or signers using regional variants. Bias assessment must account for variation within the Deaf community, not only across demographic categories used in general population assessments
- High-risk AI systems must undergo documented bias evaluation before go-live and at defined intervals thereafter. For SignalPath Interpret (SP-AI-001), bias evaluation must cover signer variation, regional dialect, physical limitation, and the oral/ASL distinction before any production deployment
- Where a system is found to produce discriminatory outputs, it will be suspended or modified until the issue is resolved
- AI outputs that score, rank, or screen individuals must be reviewed by a qualified human before those outputs are acted upon

---

### 3.2 Transparency

**Commitment:** SignalPath will be open about its use of AI where it affects individuals, and will provide meaningful explanations for AI-influenced decisions.

**What this means in practice:**

- Users will be informed when AI systems play a material role in services affecting them. Disclosure must be available in plain English and, for services directed at Deaf users, in ASL summary format
- If we cannot explain a data or AI practice to a Deaf user in their primary language, we should not be doing it
- AI systems that make or inform decisions about individuals must be capable of generating human-interpretable explanations for those decisions
- Internal users of AI systems, employees using AI-generated recommendations, will be informed of the system's limitations and known error rates
- SignalPath will maintain an internal AI system inventory that is available to the Board, regulators, and auditors upon request. As of May 2026, that inventory documents 16 AI systems across five categories

---

### 3.3 Accountability

**Commitment:** Every AI system used by SignalPath will have a named owner who is accountable for its performance and governance.

**What this means in practice:**

- A system owner must be designated before any AI system is deployed
- System owners are responsible for ensuring the system operates within its approved purpose and within the bounds of this policy
- System owners are responsible for escalating material issues to the AI Governance Committee
- Where AI is procured from vendors, the SignalPath system owner retains accountability for how the system is used and must ensure vendor obligations are contractually captured. Vendor AI is not ungoverned AI
- The AI Governance Committee is accountable to the Board Risk and Audit Committee for the overall AI governance program

---

### 3.4 Safety and Robustness

**Commitment:** AI systems will be designed, tested, and monitored to perform reliably and safely, including under adverse or unexpected conditions.

**What this means in practice:**

- AI systems must be tested against adversarial inputs and edge cases before deployment
- Performance thresholds must be defined at deployment and monitored continuously. Degradation below defined thresholds triggers a formal review
- AI systems must not be deployed in safety-critical contexts without specific Board approval and documented safety analysis. VRS emergency relay calls are a safety-critical context. Any AI system operating in the 911 relay pathway requires Board-level approval and a documented human interpreter failover architecture before deployment
- Human override capability must be maintained for all AI systems that affect individuals. For SignalPath Interpret operating in relay contexts, this means a human interpreter must be available to take over any call where AI confidence falls below defined thresholds or where the user requests it

---

### 3.5 Human Oversight

**Commitment:** SignalPath will maintain meaningful human oversight of AI systems, particularly where AI outputs affect the ability of Deaf and hard-of-hearing users to access communications services.

**What this means in practice:**

- AI outputs that inform consequential decisions must be reviewed by a qualified human before those decisions are communicated to individuals
- Rubber-stamp oversight is not acceptable oversight. A human who nominally reviews but never overrides is not providing oversight. Oversight is only meaningful if the reviewer has the information, training, and authority to override the AI's output
- High-risk AI systems must have documented human oversight procedures, including explicit criteria for when to override and how that override is logged
- Employees responsible for human oversight of AI systems must receive appropriate training before taking on that responsibility
- The right to human oversight extends to SignalPath's users. A Deaf user who believes an AI interpretation is incorrect must have an accessible mechanism to flag the error and request human review. This mechanism must be available in the VRS interface, not only in written documentation

---

### 3.6 Community Accountability

**Commitment:** SignalPath will maintain structured Deaf community input into governance decisions about AI systems that directly affect Deaf and hard-of-hearing users.

**What this means in practice:**

- The Deaf Community Advisory Panel is a named participant in the AI governance structure with documented influence on design decisions. It is not a focus group, and its participation cannot be deferred when timelines are tight
- Accuracy thresholds, acceptable failure rates, and failure mode priorities for systems like SignalPath Interpret must not be set exclusively by people who have not experienced a failed interpretation in a medical appointment or a 911 relay call
- Community input received and decisions made as a result, or explicit rationale for decisions made against community input, must be documented and available to the Board
- Deaf community representation is required in Board-level risk reporting on high-risk AI systems serving the Deaf community

---

## 4. AI Lifecycle Governance Requirements

This section defines the governance requirements at each stage of the AI lifecycle.

### 4.1 Ideation and Use Case Submission

Before any AI system is developed or procured, the business owner must submit an AI Use Case Request (AUCR) to the AI Governance Program Office. The AUCR captures:

- Business purpose and intended users
- Data sources and processing activities
- Affected individuals and potential harms, including harms specific to Deaf and hard-of-hearing users
- Proposed human oversight mechanism

All AUCRs are triaged within five business days. Triage determines the review pathway based on preliminary risk assessment.

### 4.2 Risk Assessment and Classification

All AI systems are assessed and classified before deployment:

- **EU AI Act risk tier** (Unacceptable / High / Limited / Minimal): SignalPath applies the EU AI Act as its ethical benchmark globally, not only where legally mandated
- **NIST AI RMF maturity baseline**: to identify governance gaps across Govern, Map, Measure, and Manage functions
- **Organizational risk rating**: combining regulatory and business risk factors specific to VRS and accessibility technology operations

High-risk systems require Enhanced Review, which includes external input where appropriate and Deaf Community Advisory Panel consultation for systems affecting Deaf users.

### 4.3 Approval and Go-Live

AI systems may not be deployed in a production environment without formal approval:

| Risk Tier | Approver |
|-----------|---------|
| Minimal Risk | AI Governance Program Office |
| Limited Risk | AI Governance Program Office and System Owner |
| High Risk | AI Governance Committee |
| Unacceptable Risk | Prohibited. No approval pathway. |

Approval is documented and recorded in the AI System Inventory. For high-risk systems, approval requires confirmation that all gate conditions defined during Enhanced Review have been met. No production deployment date for a high-risk system may be set before the AI Governance Program Office confirms gate conditions are satisfied.

### 4.4 Monitoring and Review

Deployed AI systems are subject to ongoing monitoring:

- Performance metrics, including accuracy, fairness indicators, and error rates, are tracked at intervals defined at approval
- For SignalPath Interpret and other systems operating in real-time relay contexts, accuracy must be tracked by signer demographic segment, not only as an aggregate figure. An overall accuracy rate that masks failure concentration among oral Deaf users or signers with physical limitations is not an adequate monitoring signal
- Material degradation or incident triggers a formal review
- All high-risk systems are reviewed at a minimum annually by the AI Governance Program Office
- System owners attest annually to continued compliance with approved scope and this policy

### 4.5 Decommissioning

When an AI system is retired, the system owner is responsible for:

- Data retention and deletion consistent with the SignalPath Data Governance Policy, including Tier 4 auto-deletion requirements for relay call content and biometric data
- Updating the AI System Inventory
- Notifying the AI Governance Program Office
- Documenting lessons learned for the governance program

---

## 5. Vendor and Third-Party AI

Where SignalPath deploys AI systems developed by external vendors:

- The procurement process must include an AI governance assessment before contract execution
- Contracts must include provisions requiring vendors to: comply with applicable AI regulations including the EU AI Act where applicable; provide technical documentation on model design and training data; notify SignalPath of material model changes before implementation; and support SignalPath's audit rights
- SignalPath system owners are accountable for the governance of vendor AI in the same way as internally developed AI. Procuring an AI system from a vendor does not transfer accountability for how that system is used
- The AI Governance Program Office maintains a vendor AI register as part of the AI System Inventory. As of May 2026, high-priority vendor AI systems requiring governance remediation include SP-AI-006 (Workday AI, high-risk employment decisions), SP-AI-013 (Outside Counsel Harvey AI, no AI governance clause in engagement agreement), and SP-AI-016 (Shadow AI, unclassified and undiscovered instances of AI tools in use without organizational knowledge or approval)

---

## 6. ASL Plain-Language Requirement

Every policy, procedure, and user-facing disclosure that governs how SignalPath builds or deploys AI systems must be translatable into plain English accessible to lay audiences.

Key governance policies, including this policy, the AI Use Case Review Process, and user consent disclosures for biometric data processing, must have ASL summary content available. The standard is not whether a document could theoretically be translated. The standard is whether a Deaf user interacting with SignalPath's AI systems can access a plain-language explanation of how those systems work and what rights they have, in their primary language.

If a governance policy cannot be explained in ASL, that is a signal the policy is not well enough understood to be enforced.

---

## 7. Roles and Responsibilities

| Role | Responsibility |
|------|--------------|
| **Board Risk and Audit Committee** | Oversight of AI governance program; approval of high-risk AI systems; annual review of AI governance report |
| **Chief Executive** | Accountable for organizational AI governance posture; chairs or delegates AI Governance Committee; approves Deaf Community Advisory Panel structure |
| **Chief Risk Officer** | Policy owner; co-chairs AI Governance Committee; escalation point for material AI risk events |
| **Chief Compliance Officer** | Regulatory compliance interface; escalation point when gate conditions are not met before deployment; incident response coordination |
| **Chief Privacy Officer** | GDPR, CCPA, and AI Act data governance interface; co-reviews high-risk assessments; biometric consent framework owner |
| **General Counsel** | Regulatory interpretation; contract review for vendor AI provisions; conformity assessment coordination |
| **AI Governance Committee** | Cross-functional governance body; approves high-risk systems; reviews incidents; oversees compliance with this policy |
| **AI Governance Program Office** | Program coordination; use case triage; AI System Inventory maintenance; training; reporting to the Committee and Board |
| **System Owners** | Accountability for individual AI systems; day-to-day oversight; escalation to the Program Office |
| **Chief Product Officer** | Accountable for product AI system performance; gate condition owner for production deployment decisions |
| **Head of VRS Operations** | Accountable for emergency call routing architecture and human interpreter failover |
| **Engineering Lead** | Technical implementation of governance controls; model documentation; monitoring infrastructure |
| **Information Security** | Cybersecurity and adversarial robustness assessment for AI systems |
| **Deaf Community Advisory Panel** | Structured community input on design decisions, accuracy thresholds, and acceptable failure rates for AI systems serving Deaf users; documented governance role, not advisory only |

---

## 8. Training

All employees involved in developing, procuring, deploying, or overseeing AI systems must complete:

- **AI Governance Fundamentals** (all employees in scope): annual completion required
- **Human Oversight of AI Systems** (employees responsible for reviewing AI outputs): at onboarding and annually; must include VRS-specific scenarios for employees overseeing relay AI systems
- **AI Risk Assessment** (AI Governance Program Office and system owners): at appointment and when material changes to the regulatory framework occur

Training materials must be available in accessible formats. For training directed at Deaf employees in governance or oversight roles, ASL-accessible versions are required, not optional.

---

## 9. Policy Breach

Breaches of this policy, including deploying an AI system without approval, failing to implement required human oversight, misrepresenting a system's risk classification, or setting a production deployment date for a high-risk system before gate conditions are confirmed, will be treated as a conduct matter and may result in disciplinary action.

Where a policy breach has caused or risked harm to individuals or regulatory non-compliance, the Chief Compliance Officer must be notified and an incident response initiated under the AI Incident Response Procedure.

The Deaf community that SignalPath serves cannot be the variable that gets cut when a product timeline runs short. A governance breach that puts that community at risk is not a documentation failure. It is a failure of organizational accountability.

---

## 10. Review and Updates

This policy will be reviewed annually or upon material change in:

- Applicable law or regulation, including the EU AI Act, FCC Part 64, ADA Title IV, GDPR, or state privacy law developments in California, Texas, or Illinois
- SignalPath's AI portfolio or operating model, including deployment of new AI systems or material changes to existing systems
- Material AI incidents internally or industry-wide that warrant policy updates, including AI interpretation failures at other VRS providers

The Chief Risk Officer is responsible for initiating reviews.

---

> **REVIEW FLAG:** Section 3.1 references accuracy benchmarks and bias evaluation requirements for SignalPath Interpret. Specific accuracy thresholds are not included in this policy document because they require verification against real VRS operational context before any public presentation. Thresholds are defined in the system-level governance documentation for SP-AI-001.

*Version history available from the AI Governance Program Office.*
*Queries: ai-governance@signalpath.example*
