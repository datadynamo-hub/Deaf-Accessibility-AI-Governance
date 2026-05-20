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

## Governance Structure

<!-- GOVERNANCE_DIAGRAM -->

---

## Committee and Role Descriptions

### Board Risk and Audit Committee

**Mandate:** Strategic oversight of SignalPath's risk framework, including AI governance as a material and growing risk category given the company's deployment of AI in real-time relay, captioning, and interpretation services.

**AI governance responsibilities:**
- Annual review of AI Governance Program report, presented by the Chief Risk Officer
- Receives notification of material AI incidents and regulatory actions, including any FCC (Federal Communications Commission) enforcement actions related to AI system performance
- Approves AI governance program budget and resource plan
- Reviews and endorses the Responsible AI Policy annually
- Receives Board-level reporting on SignalPath Interpret (SP-AI-001) performance and compliance status, per the governance review memo conditions

**Meeting frequency:** Quarterly. AI governance is a standing agenda item at a minimum of one meeting per year. Material incidents and high-risk deployment decisions are escalated as needed.

---

### AI Governance Committee

**Mandate:** Operational oversight of SignalPath's AI governance program. The primary decision-making body for AI governance matters below Board level.

**Members:**
- **Chair:** Chief Risk Officer
- **Chief Technology Officer:** Technology, engineering, and product AI perspective
- **Chief Privacy Officer:** GDPR (General Data Protection Regulation), CCPA (California Consumer Privacy Act), EU AI Act data obligations, biometric consent framework
- **General Counsel:** Legal interpretation, FCC regulatory matters, contract review for vendor AI
- **Chief Information Security Officer (CISO):** Cybersecurity and adversarial robustness for AI systems

**Quorum:** Chair plus any two members.

**AI governance responsibilities:**
- Approves high-risk AI system deployments, with power to delegate limited-risk approvals to the Proposed AI Governance Program Office (AGPO)
- Reviews and acts on quarterly AI Governance Dashboard presented by the Proposed AGPO
- Reviews material AI incidents within 30 days of closure
- Approves updates to the Responsible AI Policy
- Escalation point for disputes between system owners and the Proposed AGPO
- Provides direction on emerging governance issues: new FCC rulemaking, EU AI Act implementing measures, new AI capabilities in VRS (Video Relay Service) or interpretation technology

**Meeting frequency:** Quarterly scheduled plus extraordinary sessions as needed, typically within five business days for high-risk approval requests or material incidents.

---

### Proposed AI Governance Program Office (AGPO)

**Mandate:** Coordinate and operationalize SignalPath's AI governance program.

**Responsibilities:**
- Maintain the AI System Inventory (currently 16 systems across five categories)
- Receive, triage, and coordinate review of all AI Use Case Requests (AUCRs)
- Produce risk assessments for Standard Review use cases
- Coordinate Enhanced Review panels for high-risk use cases, including mandatory Deaf Community Advisory Panel participation for systems affecting Deaf users
- Monitor regulatory developments: EU AI Act implementation measures, FCC AI-related rulemaking, ADA (Americans with Disabilities Act) Title IV guidance, and state privacy law enforcement actions
- Deliver AI governance training program
- Maintain incident log and coordinate AI incident response
- Produce quarterly AI Governance Dashboard for the Committee
- Produce annual AI Governance Program Report for the Board

**Staffing:** AI Governance Lead (full-time) plus 0.5 analyst (initial). Review after 12 months based on program volume and inventory growth.

**Reports to:** Chief Risk Officer

---

### Deaf Community Advisory Panel

**Mandate:** Structured Deaf community input into governance decisions about AI systems that directly affect Deaf and hard-of-hearing users. This is not a focus group. It is a named governance participant with documented influence on design decisions.

**Responsibilities:**
- Participates in Enhanced Review panels for systems affecting Deaf users, including SignalPath Interpret (SP-AI-001)
- Reviews and provides input on accuracy thresholds, acceptable failure rates, and failure mode priorities for AI interpretation and captioning systems
- Reviews user-facing consent disclosures and plain-language summaries for clarity and accessibility
- Documents community input provided; the Proposed AGPO documents decisions made as a result, or explicit rationale for decisions made against community input
- Provides Deaf community perspective in Board-level risk reporting on SP-AI-001

**Appointment:** Panel members nominated in consultation with the Chief Executive. Composition must include active Deaf VRS users. Panel structure and composition documented in Proposed AGPO records.

**Activation:** Required participant in any Enhanced Review for systems that: process biometric data from Deaf users; operate in real-time relay or interpretation contexts; set accuracy thresholds or failure mode priorities for ASL (American Sign Language) AI systems; or affect emergency call handling.

---

### Functional AI Champions

**Mandate:** Embedded governance contacts within each business unit, facilitating local compliance with the AI governance program.

**Responsibilities:**
- First point of contact for AI use case queries in their business unit
- Facilitate AI Use Case Request (AUCR) submissions: help business owners complete the form correctly before submission
- Maintain awareness of AI systems deployed in their business unit
- Escalate shadow AI use to the Proposed AGPO, including employees using AI tools that have not gone through the governance process
- Attend quarterly AI Champions forum run by the Proposed AGPO

**Appointment:** One per business unit, nominated by business unit head, confirmed by the Chief Risk Officer. Typically 10–20% of role alongside main function.

**Currently required in:**
- Interpreting Services
- Product Management (Interpret / Forum / Express / CaptionLine)
- Advanced Sign Technology (AST)
- Human Resources
- Information Technology
- Legal
- Customer Experience
- Enterprise Sales

---

### System Owners

**Mandate:** Accountability for the governance and performance of an individual AI system throughout its lifecycle.

**Responsibilities:**
- Ensure the system operates within its approved scope and in compliance with the Responsible AI Policy
- Maintain and enforce human oversight procedures, including emergency call routing architecture for systems operating in relay contexts
- Monitor system performance against approved thresholds
- Escalate material issues, incidents, or changes to the Proposed AGPO
- Manage vendor relationships and ensure contractual AI governance obligations are met
- Complete annual attestation of policy compliance
- Ensure relevant staff are trained on oversight procedures for their system

**Current system owners by priority tier:**

| System | ID | Owner |
|--------|-----|-------|
| SignalPath Interpret | SP-AI-001 | Chief Product Officer |
| Workday AI | SP-AI-006 | Head of Human Resources |
| Outside Counsel Harvey AI | SP-AI-013 | General Counsel |
| Shadow AI (pending discovery) | SP-AI-016 | Chief Information Security Officer (discovery owner) |
| Microsoft Copilot M365 | SP-AI-005 | Chief Technology Officer |

---

## Decision Authority Matrix

| Decision | System Owner | Proposed AGPO | AI Governance Committee | Board R&A |
|----------|-------------|------|------------------------|-----------|
| Approve minimal-risk system | Recommends | **Approves** | Notified | N/A |
| Approve limited-risk system | Recommends | **Approves** (with Legal and Chief Privacy Officer sign-off) | Notified | N/A |
| Approve high-risk system | Recommends | Coordinates review | **Approves** | Notified |
| Approve high-risk system: SP-AI-001 | Recommends | Confirms gate conditions met | **Approves** | **Notified** |
| Suspend system due to incident | **Immediate suspension authority** | Notified immediately | Informed within 24h | N/A |
| Reject use case | N/A | **Decides** (with Committee endorsement for High Risk) | **Endorses** rejection of High Risk | N/A |
| Update Responsible AI Policy | N/A | Drafts | **Approves** | **Endorses** |
| Escalate to regulator (FCC / state AG) | N/A | Recommends | **Decides** | Informed |
| Set SP-AI-001 production deployment date | N/A | Confirms all gate conditions | **Authorizes** | Informed |

---

## Interaction with Existing Governance Structures

AI governance at SignalPath integrates with existing structures. It does not duplicate them.

| Existing Function | AI Governance Interface |
|------------------|------------------------|
| **Data Governance** | Chief Privacy Officer sits on the AI Governance Committee. All AI Use Case Requests (AUCRs) involving personal data, biometric data, or relay call content are co-reviewed by the Chief Privacy Officer. Data Protection Impact Assessments (DPIAs) and AI risk assessments are coordinated as a combined exercise where both are required under GDPR Article 35. |
| **Information Security** | The Chief Information Security Officer (CISO) or delegate sits on all high-risk review panels. Adversarial robustness and cybersecurity requirements for AI systems are owned by Information Security with AI Governance oversight. VRS-specific security requirements, including relay call data protection, are part of every high-risk panel review. |
| **Legal and Compliance** | Legal provides regulatory interpretation for classification decisions, FCC compliance questions, and ADA Title IV obligations. General Counsel owns contract review for vendor AI, including AI clause requirements for outside counsel. Compliance monitors EU AI Act and FCC regulatory developments. |
| **Procurement** | The Proposed AGPO provides an AI governance assessment checklist for use in vendor procurement. Procurement notifies the Proposed AGPO of AI-related vendor selections before contract signature. Vendor AI is not approved for use until an AUCR has been completed and the vendor AI governance assessment is on file. |
| **Internal Audit** | Internal Audit includes AI governance program effectiveness in its annual plan. The Proposed AGPO provides audit access to the AI System Inventory, risk assessments, and approval documentation. |

---

## Reporting Calendar

| Report | Frequency | Owner | Audience |
|--------|-----------|-------|---------|
| AI Governance Dashboard | Quarterly | Proposed AGPO | AI Governance Committee |
| AI Incident Summary | Quarterly (or ad hoc for Severity 1) | Proposed AGPO | AI Governance Committee |
| High-Risk System Review | Annual per system | Proposed AGPO | AI Governance Committee |
| SP-AI-001 Performance and Compliance Report | Within 90 days of production deployment, then quarterly | Proposed AGPO | Board Risk and