# AI Governance Operating Model

**Organization:** SignalPath Technologies
**Version:** 1.0
**Effective Date:** May 2026

---

## Overview

This document describes SignalPath's AI governance operating structure: the committees, roles, reporting lines, and interactions that make responsible AI governance operational rather than aspirational.

Governance does not happen in policies. It happens in decisions, conversations, and processes. This model defines who makes which decisions, who advises whom, and how AI oversight connects to SignalPath's existing governance structure.

At a company where AI systems interpret emergency relay calls in real time, governance structure is not an administrative question. It is a question of who is accountable when something goes wrong, and whether that accountability was defined before the failure, not after.

---

## Governance Structure Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                    BOARD RISK & AUDIT COMMITTEE                      │
│                                                                      │
│  • Annual AI governance program review                              │
│  • Approval of high-risk AI systems (escalated)                     │
│  • Oversight of material AI incidents                               │
└─────────────────────────────┬───────────────────────────────────────┘
                              │ Reports to / escalates to
                              │
┌─────────────────────────────▼───────────────────────────────────────┐
│                      AI GOVERNANCE COMMITTEE                         │
│                                                                      │
│  Chair: Chief Risk Officer                                          │
│  Members: CTO · Chief Privacy Officer · General Counsel · CISO      │
│  Observer: CFO                                                       │
│  Meets: Quarterly (+ extraordinary sessions for high-risk approvals) │
│                                                                      │
│  • Approves high-risk AI system deployments                         │
│  • Reviews quarterly AI governance report                           │
│  • Owns Responsible AI Policy                                       │
│  • Reviews material AI incidents                                    │
│  • Escalation point for governance disputes                         │
└──────────┬────────────────────────────────────────┬─────────────────┘
           │                                        │
           │ Directs / resources                    │ Reviews / escalates
           │                                        │
┌──────────▼──────────────────────┐     ┌──────────▼──────────────────┐
│  AI GOVERNANCE PROGRAM OFFICE   │     │   FUNCTIONAL AI CHAMPIONS   │
│                                 │     │                             │
│  • Program coordination         │     │  • One per business unit    │
│  • Use case triage and review   │     │  • First point of contact   │
│  • AI System Inventory          │     │    for AI use case queries  │
│  • Training program             │     │  • Facilitate local AUCR    │
│  • Regulatory monitoring        │     │    submissions              │
│  • Incident coordination        │     │  • Monitor local AI use     │
│  • Reporting to Committee       │     │  • Escalate shadow AI       │
└──────────┬──────────────────────┘     └─────────────────────────────┘
           │
           │ Consults / coordinates review
           │
┌──────────▼──────────────────────────────────────────────────────────┐
│                      REVIEW PANEL (per system)                       │
│                                                                      │
│  Assembled per high-risk review. Drawn from:                        │
│                                                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌───────────┐  │
│  │   Legal /   │  │   Chief     │  │ Information │  │    ML     │  │
│  │ Compliance  │  │  Privacy    │  │  Security   │  │ Engineer- │  │
│  │             │  │  Officer    │  │  (CISO      │  │  ing /    │  │
│  │ • Regulatory│  │             │  │  delegate)  │  │  Data     │  │
│  │   opinion   │  │ • GDPR /    │  │             │  │  Science  │  │
│  │ • FCC /     │  │   CCPA      │  │ • Adversar- │  │           │  │
│  │   ADA       │  │   review    │  │   ial       │  │ • Techni- │  │
│  │   interpret-│  │ • AI Act    │  │   robustness│  │   cal     │  │
│  │   ation     │  │   data      │  │ • VRS       │  │   review  │  │
│  │ • Contract  │  │   governance│  │   security  │  │ • Model   │  │
│  │   review    │  │ • Biometric │  │             │  │   docs    │  │
│  │             │  │   consent   │  │             │  │           │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  └───────────┘  │
│                                                                      │
│  For systems serving Deaf users: Deaf Community Advisory Panel      │
│  is a required participant in Enhanced Review panels.               │
└─────────────────────────────────────────────────────────────────────┘
           │
           │ Accountable for individual systems
           │
┌──────────▼──────────────────────────────────────────────────────────┐
│                         SYSTEM OWNERS                                │
│                                                                      │
│  One per AI system. Named in the AI System Inventory.               │
│                                                                      │
│  • Accountable for system's ongoing governance                      │
│  • Responsible for implementing and maintaining oversight controls   │
│  • Escalates material issues to AI Governance Program Office        │
│  • Attests annually to compliance with Responsible AI Policy        │
│  • Manages vendor relationships for vendor AI systems               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Committee and Role Descriptions

### Board Risk and Audit Committee

**Mandate:** Strategic oversight of SignalPath's risk framework, including AI governance as a material and growing risk category given the company's deployment of AI in real-time relay, captioning, and interpretation services.

**AI governance responsibilities:**
- Annual review of AI Governance Program report, presented by the Chief Risk Officer
- Receives notification of material AI incidents and regulatory actions, including any FCC enforcement actions related to AI system performance
- Approves AI governance program budget and resource plan
- Reviews and endorses the Responsible AI Policy annually
- Receives Board-level reporting on SignalPath Interpret (SP-AI-001) performance and compliance status, per the governance review memo conditions

**Meeting frequency:** Quarterly. AI governance is a standing agenda item at a minimum of one meeting per year. Material incidents and high-risk deployment decisions are escalated as needed.

---

### AI Governance Committee

**Mandate:** Operational oversight of SignalPath's AI governance program. The primary decision-making body for AI governance matters below Board level.

**Members:**
- **Chair:** Chief Risk Officer
- **CTO:** technology, engineering, and product AI perspective
- **Chief Privacy Officer:** GDPR, CCPA, EU AI Act data obligations, biometric consent framework
- **General Counsel:** legal interpretation, FCC regulatory matters, contract review for vendor AI
- **CISO:** cybersecurity and adversarial robustness for AI systems
- **CFO (observer):** commercial and financial impact of governance decisions

📌 *Note: CFO observer role is a structural inference. Not explicitly named in prior SignalPath governance artifacts. Include or remove based on actual organizational structure.*

**Quorum:** Chair plus any two members.

**AI governance responsibilities:**
- Approves high-risk AI system deployments, with power to delegate limited-risk approvals to the AI Governance Program Office
- Reviews and acts on quarterly AI Governance Dashboard presented by the Program Office
- Reviews material AI incidents within 30 days of closure
- Approves updates to the Responsible AI Policy
- Escalation point for disputes between system owners and the Program Office
- Provides direction on emerging governance issues: new FCC rulemaking, EU AI Act implementing measures, new AI capabilities in VRS or interpretation technology

**Meeting frequency:** Quarterly scheduled plus extraordinary sessions as needed, typically within five business days for high-risk approval requests or material incidents.

---

### AI Governance Program Office (AGPO)

**Mandate:** Coordinate and operationalize SignalPath's AI governance program.

**Responsibilities:**
- Maintain the AI System Inventory (currently 16 systems across five categories)
- Receive, triage, and coordinate review of all AI Use Case Requests (AUCRs)
- Produce risk assessments for Standard Review use cases
- Coordinate Enhanced Review panels for high-risk use cases, including mandatory Deaf Community Advisory Panel participation for systems affecting Deaf users
- Monitor regulatory developments: EU AI Act implementation measures, FCC AI-related rulemaking, ADA Title IV guidance, and state privacy law enforcement actions
- Deliver AI governance training program
- Maintain incident log and coordinate AI incident response
- Produce quarterly AI Governance Dashboard for the Committee
- Produce annual AI Governance Program Report for the Board

**Staffing:** AI Governance Lead (FTE) plus 0.5 FTE analyst (initial). Review after 12 months based on program volume and inventory growth.

**Reports to:** Chief Risk Officer

---

### Deaf Community Advisory Panel

**Mandate:** Structured Deaf community input into governance decisions about AI systems that directly affect Deaf and hard-of-hearing users. This is not a focus group. It is a named governance participant with documented influence on design decisions.

**Responsibilities:**
- Participates in Enhanced Review panels for systems affecting Deaf users, including SignalPath Interpret (SP-AI-001)
- Reviews and provides input on accuracy thresholds, acceptable failure rates, and failure mode priorities for AI interpretation and captioning systems
- Reviews user-facing consent disclosures and ASL plain-language summaries for clarity and accessibility
- Documents community input provided; AGPO documents decisions made as a result, or explicit rationale for decisions made against community input
- Provides Deaf community perspective in Board-level risk reporting on SP-AI-001

**Appointment:** Panel members nominated in consultation with the Chief Executive. Composition must include active Deaf VRS users. Panel structure and composition documented in AGPO records.

**Activation:** Required participant in any Enhanced Review for systems that: process biometric data from Deaf users; operate in real-time relay or interpretation contexts; set accuracy thresholds or failure mode priorities for ASL AI systems; or affect emergency call handling.

---

### Functional AI Champions

**Mandate:** Embedded governance contacts within each business unit, facilitating local compliance with the AI governance program.

**Responsibilities:**
- First point of contact for AI use case queries in their business unit
- Facilitate AUCR submissions: help business owners complete the form correctly before submission
- Maintain awareness of AI systems deployed in their business unit
- Escalate shadow AI use to the AGPO, including employees using AI tools that have not gone through the governance process
- Attend quarterly AI Champions forum run by the AGPO

**Appointment:** One per business unit, nominated by business unit head, confirmed by the Chief Risk Officer. Typically 10-20% of role alongside main function.

**Currently required in:**
- VRS Operations
- Product (Interpret / Forum / Express / CaptionLine)
- ML Engineering and Data Science
- Human Resources
- Information Technology
- Legal and Compliance
- Customer Experience
- Enterprise Sales and Marketing

📌 *Note: Business unit list is inferred from SignalPath's known operational structure and AI system inventory. Confirm against actual organizational chart before finalizing.*

---

### System Owners

**Mandate:** Accountability for the governance and performance of an individual AI system throughout its lifecycle.

**Responsibilities:**
- Ensure the system operates within its approved scope and in compliance with the Responsible AI Policy
- Maintain and enforce human oversight procedures, including emergency call routing architecture for systems operating in relay contexts
- Monitor system performance against approved thresholds
- Escalate material issues, incidents, or changes to the AGPO
- Manage vendor relationships and ensure contractual AI governance obligations are met
- Complete annual attestation of policy compliance
- Ensure relevant staff are trained on oversight procedures for their system

**Nomination:** System owner is proposed by the business owner at AUCR submission and confirmed at approval. Must be a senior manager or above with operational responsibility for the system.

**Current system owners by priority tier:**

| System | ID | Owner |
|--------|-----|-------|
| SignalPath Interpret | SP-AI-001 | Chief Product Officer |
| Workday AI | SP-AI-006 | Head of Human Resources |
| Outside Counsel Harvey AI | SP-AI-013 | General Counsel |
| Shadow AI (pending discovery) | SP-AI-016 | CISO (discovery owner) |
| Microsoft Copilot M365 | SP-AI-005 | CTO |

📌 *Remaining 11 system owners not explicitly confirmed in project knowledge. Assign at AUCR triage based on operational responsibility.*

---

## Decision Authority Matrix

| Decision | System Owner | AGPO | AI Governance Committee | Board R&A |
|----------|-------------|------|------------------------|-----------|
| Approve minimal-risk system | Recommends | **Approves** | Notified | — |
| Approve limited-risk system | Recommends | **Approves** (with Legal and CPO sign-off) | Notified | — |
| Approve high-risk system | Recommends | Coordinates review | **Approves** | Notified |
| Approve high-risk system: SP-AI-001 | Recommends | Confirms gate conditions met | **Approves** | **Notified** |
| Suspend system due to incident | **Immediate suspension authority** | Notified immediately | Informed within 24h | — |
| Reject use case | — | **Decides** (with Committee endorsement for High Risk) | **Endorses** rejection of High Risk | — |
| Update Responsible AI Policy | — | Drafts | **Approves** | **Endorses** |
| Escalate to regulator (FCC / state AG) | — | Recommends | **Decides** | Informed |
| Set SP-AI-001 production deployment date | — | Confirms all gate conditions | **Authorizes** | Informed |

---

## Interaction with Existing Governance Structures

AI governance at SignalPath integrates with existing structures. It does not duplicate them.

| Existing Function | AI Governance Interface |
|------------------|------------------------|
| **Enterprise Risk Management** | AI risk is a sub-category of operational and compliance risk. The AI Governance Committee reports into the enterprise risk framework. The AI System Inventory feeds the enterprise risk register for material AI risks. 📌 *ERM as a named function not confirmed in SignalPath project knowledge. Include if the function exists; remove if risk is managed directly through the Board Risk and Audit Committee.* |
| **Data Governance** | Chief Privacy Officer sits on the AI Governance Committee. All AUCRs involving personal data, biometric data, or relay call content are co-reviewed by the Chief Privacy Officer. DPIA and AI risk assessment are coordinated as a combined exercise where both are required under GDPR Article 35. |
| **Information Security / CISO** | CISO or delegate sits on all high-risk review panels. Adversarial robustness and cybersecurity requirements for AI systems are owned by Information Security with AI Governance oversight. VRS-specific security requirements, including relay call data protection, are part of every high-risk panel review. |
| **Legal and Compliance** | Legal provides regulatory interpretation for classification decisions, FCC compliance questions, and ADA Title IV obligations. General Counsel owns contract review for vendor AI, including AI clause requirements for outside counsel. Compliance monitors EU AI Act and FCC regulatory developments. |
| **Procurement** | AGPO provides an AI governance assessment checklist for use in vendor procurement. Procurement notifies AGPO of AI-related vendor selections before contract signature. Vendor AI is not approved for use until an AUCR has been completed and the vendor AI governance assessment is on file. |
| **Internal Audit** | Internal Audit includes AI governance program effectiveness in its annual plan. AGPO provides audit access to the AI System Inventory, risk assessments, and approval documentation. 📌 *Internal Audit as a named function not confirmed in SignalPath project knowledge. Include if the function exists.* |

---

## Reporting Calendar

| Report | Frequency | Owner | Audience |
|--------|-----------|-------|---------|
| AI Governance Dashboard | Quarterly | AGPO | AI Governance Committee |
| AI Incident Summary | Quarterly (or ad hoc for severity 1) | AGPO | AI Governance Committee |
| High-Risk System Review | Annual per system | AGPO | AI Governance Committee |
| SP-AI-001 Performance and Compliance Report | Within 90 days of production deployment, then quarterly | AGPO | Board Risk and Audit Committee |
| AI Governance Program Report | Annual | Chief Risk Officer | Board Risk and Audit Committee |

---

> **REVIEW FLAG:** The governance structure diagram is rendered in plain text. A visual diagram is required before this document is presented in a Loom walkthrough or interview. Build the visual as a separate deliverable using the structure above as the source.

> **REVIEW FLAG:** Four items above are flagged with the 📌 symbol. Each represents a structural element inferred from project knowledge rather than confirmed. Resolve against actual organizational context before finalizing.

*Questions about this operating model: ai-governance@signalpath.example*
