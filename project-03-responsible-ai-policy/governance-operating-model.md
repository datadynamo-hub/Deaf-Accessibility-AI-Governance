# AI Governance Operating Model

**Organisation:** NorthStar Financial Services
**Version:** 1.0
**Effective Date:** March 2026

---

## Overview

This document describes NorthStar's AI governance operating structure: the committees, roles, reporting lines, and interactions that make responsible AI governance operational rather than aspirational.

Governance does not happen in policies. It happens in decisions, conversations, and processes. This model defines who makes which decisions, who advises whom, and how AI oversight connects to the organisation's existing governance structure.

---

## Governance Structure Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                    BOARD RISK & AUDIT COMMITTEE                      │
│                                                                      │
│  • Annual AI governance programme review                            │
│  • Approval of high-risk AI systems (escalated)                     │
│  • Oversight of material AI incidents                               │
└─────────────────────────────┬───────────────────────────────────────┘
                              │ Reports to / escalates to
                              │
┌─────────────────────────────▼───────────────────────────────────────┐
│                      AI GOVERNANCE COMMITTEE                         │
│                                                                      │
│  Chair: Chief Risk Officer                                          │
│  Members: CTO · DPO · General Counsel · CISO · CFO (observer)       │
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
│  AI GOVERNANCE PROGRAMME OFFICE │     │   FUNCTIONAL AI CHAMPIONS   │
│                                 │     │                             │
│  • Programme coordination       │     │  • One per business unit    │
│  • Use case triage & review     │     │  • First point of contact   │
│  • AI System Inventory          │     │    for AI use case queries  │
│  • Training programme           │     │  • Facilitate local AUCR    │
│  • Regulatory monitoring        │     │    submissions              │
│  • Incident coordination        │     │  • Monitor local AI use     │
│  • Reporting to Committee       │     │                             │
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
│  │   Legal /   │  │  Data       │  │ Information │  │    ML     │  │
│  │ Compliance  │  │  Protection │  │  Security   │  │ Engineer- │  │
│  │             │  │  Officer    │  │  (CISO      │  │  ing /    │  │
│  │ • Regulatory│  │             │  │  delegate)  │  │  Data     │  │
│  │   opinion   │  │ • GDPR      │  │             │  │  Science  │  │
│  │ • Contract  │  │   review    │  │ • Adversar- │  │           │  │
│  │   review    │  │ • AI Act    │  │   ial       │  │ • Techni- │  │
│  │             │  │   data      │  │   robustness│  │   cal     │  │
│  │             │  │   governance│  │             │  │   review  │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  └───────────┘  │
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
│  • Escalates material issues to AI Governance Programme Office      │
│  • Attests annually to compliance with Responsible AI Policy        │
│  • Manages vendor relationships for vendor AI systems               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Committee and Role Descriptions

### Board Risk & Audit Committee

**Mandate:** Strategic oversight of NorthStar's risk framework, including AI governance as a material and emerging risk category.

**AI Governance responsibilities:**
- Annual review of AI Governance Programme report, presented by the CRO
- Receives notification of material AI incidents and regulatory actions
- Approves AI governance programme budget and resource plan
- Reviews and endorses the Responsible AI Policy annually

**Meeting frequency:** Quarterly (AI governance typically a standing agenda item at one meeting per year; material incidents or decisions escalated as needed)

---

### AI Governance Committee

**Mandate:** Operational oversight of NorthStar's AI governance programme. The primary decision-making body for AI governance matters below Board level.

**Members:**
- **Chair:** Chief Risk Officer
- **CTO** — technology and engineering perspective
- **Data Protection Officer** — GDPR, EU AI Act data obligations
- **General Counsel** — legal and regulatory interpretation
- **CISO** — cybersecurity and information security
- **CFO (observer)** — commercial and financial impact

**Quorum:** Chair + any two members

**AI Governance responsibilities:**
- Approves high-risk AI system deployments (with power to delegate limited-risk approvals to AGPO)
- Reviews and acts on quarterly AI Governance Dashboard presented by AGPO
- Reviews material AI incidents (severity 1 and 2) within 30 days of closure
- Approves updates to the Responsible AI Policy
- Escalation point for disputes between system owners and AGPO
- Provides direction on emerging governance issues (new regulation, new AI capabilities)

**Meeting frequency:** Quarterly scheduled + extraordinary sessions as needed (typically within 5 days for high-risk approval requests or material incidents)

---

### AI Governance Programme Office (AGPO)

**Mandate:** Coordinate and operationalise NorthStar's AI governance programme.

**Responsibilities:**
- Maintain the AI System Inventory
- Receive, triage, and coordinate review of all AI Use Case Requests (AUCRs)
- Produce risk assessments for Standard Review use cases
- Coordinate Enhanced Review panels for high-risk use cases
- Monitor regulatory developments (EU AI Act implementation measures, guidance, enforcement actions)
- Deliver AI governance training programme
- Maintain incident log and coordinate AI incident response
- Produce quarterly AI Governance Dashboard for Committee
- Produce annual AI Governance Report for Board

**Staffing:** AI Governance Lead (FTE) + 0.5 FTE analyst (initial). Review after 12 months based on programme volume.

**Reports to:** Chief Risk Officer

---

### Functional AI Champions

**Mandate:** Embedded governance contacts within each business unit, facilitating local compliance with the AI governance programme.

**Responsibilities:**
- First point of contact for AI use case queries in their business unit
- Facilitate AUCR submissions — help business owners complete the form correctly
- Maintain awareness of AI systems deployed in their business unit
- Escalate informal AI use to AGPO (i.e., where employees are using AI tools that have not gone through the governance process)
- Attend quarterly AI Champions forum run by AGPO

**Appointment:** One per business unit, nominated by business unit head, confirmed by CRO. Role is typically part-time (10–20% of role) alongside main function.

**Currently required in:** Retail Lending · Payment Operations · Human Resources · Customer Experience · Marketing · Insurance · IT / ML Engineering · Compliance

---

### System Owners

**Mandate:** Accountability for the governance and performance of an individual AI system throughout its lifecycle.

**Responsibilities:**
- Ensure the system operates within its approved scope and in compliance with this policy
- Maintain and enforce human oversight procedures
- Monitor system performance against approved thresholds
- Escalate material issues, incidents, or changes to AGPO
- Manage vendor relationships and ensure contractual AI governance obligations are met
- Complete annual attestation of policy compliance
- Ensure relevant staff are trained

**Nomination:** System owner is proposed by the business owner at AUCR submission and confirmed at approval. Must be a senior manager or above with operational responsibility for the system.

---

## Decision Authority Matrix

| Decision | System Owner | AGPO | AI Governance Committee | Board R&A |
|----------|-------------|------|------------------------|-----------|
| Approve minimal-risk system | Recommends | **Approves** | Notified | — |
| Approve limited-risk system | Recommends | **Approves** (with Legal and DPO sign-off) | Notified | — |
| Approve high-risk system | Recommends | Coordinates review | **Approves** | Notified |
| Suspend system due to incident | **Immediate suspension authority** | Notified immediately | Informed within 24h | — |
| Reject use case | — | **Decides** (with Committee endorsement for High Risk) | **Endorses** rejection of High Risk | — |
| Update Responsible AI Policy | — | Drafts | **Approves** | **Endorses** |
| Escalate to regulator | — | Recommends | **Decides** | Informed |

---

## Interaction with Existing Governance Structures

AI governance at NorthStar is designed to integrate with, not duplicate, existing structures:

| Existing Function | AI Governance Interface |
|------------------|------------------------|
| **Enterprise Risk Management** | AI risk is a sub-category of operational and conduct risk. AI Governance Committee reports into ERM framework. AI System Inventory feeds enterprise risk register for material AI risks. |
| **Data Governance / DPO** | DPO is a member of AI Governance Committee. All AUCRs involving personal data are co-reviewed by DPO. DPIA and AI risk assessment are coordinated as a combined exercise where both are required. |
| **Information Security / CISO** | CISO (or delegate) sits on high-risk review panels. Adversarial robustness and cybersecurity requirements for AI systems are owned by Information Security with AI Governance oversight. |
| **Legal and Compliance** | Legal provides regulatory interpretation for classification decisions and contract review for vendor AI. Compliance monitors EU AI Act and sector-specific regulatory developments. |
| **Procurement** | AGPO provides an AI governance assessment checklist for use in vendor procurement processes. Procurement notifies AGPO of AI-related vendor selections before contract signature. |
| **Internal Audit** | Internal Audit will include AI governance programme effectiveness in its annual plan. AGPO provides audit access to AI System Inventory, risk assessments, and approval documentation. |

---

## Reporting Calendar

| Report | Frequency | Owner | Audience |
|--------|-----------|-------|---------|
| AI Governance Dashboard | Quarterly | AGPO | AI Governance Committee |
| AI Incident Summary | Quarterly (or ad hoc for severity 1) | AGPO | AI Governance Committee |
| High-Risk System Review | Annual per system | AGPO | AI Governance Committee |
| AI Governance Programme Report | Annual | CRO | Board Risk & Audit Committee |

---

*Questions about this operating model: ai-governance@northstar-financial.example*
