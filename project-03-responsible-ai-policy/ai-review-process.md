# AI Use Case Review and Approval Process

**Owner:** AI Governance Programme Office
**Version:** 1.0
**Effective Date:** March 2026

---

## Overview

This document describes the end-to-end process for submitting, reviewing, and approving AI use cases at NorthStar Financial Services. It applies to all new AI systems and to material changes to existing systems.

The process is designed to be **proportionate**: simpler, lower-risk use cases move quickly. Higher-risk systems receive more rigorous scrutiny. The goal is appropriate governance, not maximum friction.

---

## Process Flow

```
[1] USE CASE SUBMISSION
      |
      v
[2] INTAKE TRIAGE (5 business days)
      |
      +----> [Prohibited] --> REJECT + Notify CRO
      |
      +----> [Minimal/Limited Risk] --> STANDARD REVIEW (2 weeks)
      |
      +----> [High Risk] --> ENHANCED REVIEW (4-6 weeks)
      |
      v
[3] REVIEW AND ASSESSMENT
      |
      v
[4] APPROVAL DECISION
      |
      +----> [Approved] --> Proceed to deployment with conditions
      |
      +----> [Approved with conditions] --> Implement conditions, re-confirm
      |
      +----> [Deferred] --> Address gaps, resubmit
      |
      +----> [Rejected] --> Document rationale, notify submitter
      |
      v
[5] DEPLOYMENT AND REGISTRATION
      |
      v
[6] ONGOING MONITORING AND REVIEW
```

---

## Stage 1: Use Case Submission

**Who submits:** The business owner (future system owner) of the proposed AI system.

**How:** Submit an AI Use Case Request (AUCR) via the AI Governance Portal (or the AUCR template in the interim).

**Required information:**

| Field | Description |
|-------|-------------|
| Business purpose | What problem does this AI system solve? |
| Intended users | Who within NorthStar will use this system? |
| Affected individuals | Which external parties (customers, applicants, etc.) will be affected by AI outputs? |
| Data sources | What data will the system process? Identify personal data explicitly. |
| Output type | What does the system produce — recommendations, decisions, scores, generated content? |
| Human oversight plan | How will human oversight be implemented? Who will review AI outputs before action is taken? |
| Vendor or internal | Is this a vendor solution or internally developed? If vendor, who? |
| Proposed go-live date | Requested production date |
| System owner | Named individual accepting accountability for governance |

**Important:** Submission does not imply approval. Systems must not begin development or procurement activity that assumes approval before intake triage is complete.

---

## Stage 2: Intake Triage

**Owner:** AI Governance Programme Office
**Timeline:** 5 business days from receipt

The AI Governance Programme Office reviews the AUCR to:

1. Confirm completeness — incomplete AUCRs are returned for completion
2. Apply preliminary EU AI Act risk classification
3. Determine review pathway (Standard or Enhanced)
4. Identify immediate red flags (e.g., prohibited use case)

**Triage Outcomes:**

| Outcome | Action |
|---------|--------|
| Prohibited use case | Reject. Notify Chief Risk Officer. Document decision. |
| Minimal or Limited Risk | Route to Standard Review. |
| High Risk (confirmed or probable) | Route to Enhanced Review. Brief system owner on requirements. |
| Unclear classification | Engage Legal and DPO for classification opinion before routing. |

The system owner is notified of the triage outcome and expected timeline within 5 business days.

---

## Stage 3A: Standard Review (Minimal / Limited Risk)

**Timeline:** Up to 2 weeks
**Owner:** AI Governance Programme Office

Standard Review covers:

- Confirmation of EU AI Act risk classification
- Review of data sources against GDPR lawful basis
- Confirmation of human oversight arrangements (if applicable)
- For Limited Risk: confirmation of AI disclosure mechanism for affected individuals
- Check of vendor AI governance practices (if vendor system)

**Reviewers:** AI Governance Programme Office. DPO consulted where personal data processing is material.

**Documentation required:**
- Completed AUCR
- Privacy impact assessment (if personal data involved — may be combined with DPIA if required)
- Vendor AI governance questionnaire (if vendor system)

---

## Stage 3B: Enhanced Review (High Risk)

**Timeline:** 4–6 weeks
**Owner:** AI Governance Programme Office (coordinates); AI Governance Committee (approves)

Enhanced Review covers all Standard Review elements plus:

- Full structured risk assessment (as per Project 2 template)
- Technical documentation review (system description, training data, model architecture summary)
- Bias and fairness evaluation plan — how will fairness be assessed, by whom, against which metrics?
- Human oversight procedure — documented, role-specific, and testable
- Conformity assessment plan (for EU AI Act Article 43 compliance)
- Monitoring and performance management plan
- Incident response procedure (AI-specific)

**Reviewers:**

| Reviewer | Contribution |
|----------|-------------|
| AI Governance Programme Office | Coordinates; produces risk assessment |
| Data Protection Officer | GDPR and AI Act data governance |
| Legal / Compliance | Regulatory classification opinion; contractual requirements |
| Information Security | Cybersecurity and adversarial robustness |
| ML Engineering | Technical feasibility of proposed controls |
| External auditor / assessor | Independent bias evaluation (for high-risk systems with fairness implications) |

**Documentation required:**
- Full AUCR
- Structured risk assessment
- Technical documentation pack (aligned to EU AI Act Annex IV)
- Vendor AI due diligence pack (if vendor system)
- Bias evaluation plan or completed bias audit
- Human oversight procedure
- Monitoring plan

---

## Stage 4: Approval Decision

**Standard Review approval:** AI Governance Programme Office + System Owner sign-off

**Enhanced Review approval:** AI Governance Committee formal decision (majority vote; quorum = CRO + at least two other Committee members)

**Approval Conditions:** Approval may be granted conditionally, requiring specific controls to be implemented before or after go-live. Conditions must be documented, assigned to named owners, and have defined completion dates. Deployment cannot proceed if pre-go-live conditions are not met.

**Rejection:** If a system is rejected, the decision and rationale are documented and the system owner is notified. Rejected systems may be resubmitted following material changes to the use case or proposed controls.

**Escalation:** If the AI Governance Committee cannot reach consensus, the decision escalates to the Chief Risk Officer. If the CRO decision is contested, it escalates to the Board Risk & Audit Committee.

---

## Stage 5: Deployment and Registration

Upon approval, the system owner must:

1. Register the system in the AI System Inventory (AI Governance Programme Office records approval date, conditions, classification, and review date)
2. Complete any pre-go-live conditions before deployment
3. Ensure monitoring is in place before go-live
4. Confirm human oversight procedures are operational and relevant staff are trained
5. For high-risk systems: confirm EU AI Act registration requirements are met before go-live

The AI Governance Programme Office will confirm go-live readiness before the system enters production.

---

## Stage 6: Ongoing Monitoring and Review

**Continuous monitoring (system owner responsibility):**
- Track performance metrics against thresholds defined at approval
- Monitor for data drift, performance degradation, or emerging fairness issues
- Ensure human oversight procedures are maintained
- Report material issues to the AI Governance Programme Office

**Periodic review (AI Governance Programme Office):**

| Risk Tier | Minimum Review Frequency |
|-----------|------------------------|
| High Risk | Annual formal review + event-driven review |
| Limited Risk | Annual check-in with system owner |
| Minimal Risk | Biennial review or upon material change |

**Trigger for out-of-cycle review:**
- Material change to the system (new model version, expanded scope, new data source)
- AI incident involving the system
- Regulatory change that affects the system's classification or obligations
- System owner change

---

## Material Changes

Material changes to approved systems require a new AUCR or a change request to the AI Governance Programme Office. What constitutes a material change:

- Change of system purpose or scope
- New category of personal data processed
- Significant model update (retraining on new data, architecture change)
- Change of vendor
- Deployment to a new geography
- Change of system owner

Minor changes (e.g., UI updates, bug fixes that do not affect model behaviour) may be documented without a new review, at the discretion of the AI Governance Programme Office.

---

*Process queries: ai-governance@northstar-financial.example*
