# AI Use Case Review and Approval Process

**Owner:** AI Governance Program Office
**Version:** 1.0
**Effective Date:** May 2026

---

## Overview

This document describes how SignalPath reviews and approves AI systems before they go live. It applies to every new AI system and to significant changes to systems already in use.

The process is proportionate: lower-risk systems move through quickly. Higher-risk systems get more scrutiny. The goal is the right level of oversight, not the most paperwork.

At SignalPath, the stakes are higher than at most companies. An AI system deployed without review could be processing sensitive biometric data from Deaf users, routing emergency calls, or making hiring decisions for thousands of people, before anyone in governance knows it exists. This process exists to prevent that.

---

## Glossary

Plain definitions for terms used in this document:

**AI system:** Any software that uses machine learning or similar technology to generate outputs, such as predictions, decisions, captions, or recommendations, based on data it was trained on.

**Biometric data:** Physical characteristics used to identify or analyze a person, such as hand shape, facial expressions, or body movement. SignalPath Interpret processes biometric data.

**EU AI Act:** A European law that classifies AI systems by risk level and sets requirements for how high-risk systems must be built, tested, and monitored. SignalPath applies it globally as its ethical standard, even for US operations.

**GDPR:** A European privacy law governing how personal data is collected, stored, and used. Applies to SignalPath because Deaf users in the US travel internationally and access SignalPath services from EU countries.

**CCPA:** A California privacy law with similar goals to GDPR. Applies to SignalPath's California users and operations.

**FCC Part 64:** The US federal rules governing Video Relay Service, including call confidentiality and service reliability requirements.

**Conformity assessment:** A formal review confirming that a high-risk AI system meets legal requirements before it goes live. Required by the EU AI Act for systems like SignalPath Interpret.

**Data Protection Impact Assessment:** A structured analysis required by European privacy law when a new system is likely to create significant privacy risks. Done before deployment, not after.

**System owner:** The person at SignalPath who is accountable for how an AI system is used and governed. Named at the time of approval.

---

## Process Flow

```
[1] SUBMISSION
      |
      v
[2] INITIAL REVIEW (5 business days)
      |
      +----> [Prohibited] --> REJECTED + Notify Chief Risk Officer
      |
      +----> [Lower Risk] --> STANDARD REVIEW (2 weeks)
      |
      +----> [High Risk] --> FULL REVIEW (4-6 weeks)
      |
      v
[3] REVIEW AND ASSESSMENT
      |
      v
[4] DECISION
      |
      +----> [Approved] --> Proceed to go-live with any conditions
      |
      +----> [Approved with conditions] --> Meet conditions first, then confirm
      |
      +----> [Deferred] --> Fix the gaps, resubmit
      |
      +----> [Rejected] --> Decision documented, submitter notified
      |
      v
[5] GO-LIVE AND REGISTRATION
      |
      v
[6] ONGOING MONITORING
```

---

## Stage 1: Submission

**Who submits:** The person who owns the business need for this AI system and will be accountable for it going forward.

**How:** Complete and submit an AI use case request form to the AI Governance Program Office. A template is available; a dedicated submission tool is planned.

📌 *Note: The submission tool is not yet confirmed. Use the template until further notice.*

**What the form asks:**

| Field | What to include |
|-------|-------------|
| Business purpose | What problem does this AI system solve? |
| Intended users | Who at SignalPath will use it? |
| People affected | Who outside SignalPath will be affected by its outputs? Include Deaf and hard-of-hearing users, customers, and relay call participants where relevant. |
| Data used | What data will the system process? Call out personal information, physical or biometric data, and relay call content specifically. |
| What it produces | Does it make decisions? Generate captions? Score or rank people? Produce recommendations? |
| Human review plan | Who reviews what the AI produces before anyone acts on it? For relay and interpretation systems: what happens when the AI is not confident, and what happens on emergency calls? |
| Build or buy | Is this built in-house or from a vendor? If vendor, name them. |
| Target go-live date | When does the business need this live? |
| System owner | Who is accepting accountability for this system? |
| Community impact | Does this system directly affect Deaf or hard-of-hearing users? If yes, describe how. |

**Important:** Submitting this form is not approval. No development or purchasing should begin based on an assumption that approval will be granted.

---

## Stage 2: Initial Review

**Owner:** AI Governance Program Office
**Timeline:** 5 business days from receipt

The AI Governance Program Office reads the submission to:

1. Check that it is complete. Incomplete submissions are returned.
2. Assign a risk level using established AI risk frameworks.
3. Decide which review path to take: standard or full.
4. Catch any immediate problems, such as a prohibited use case or an unaddressed emergency call risk.

**What happens next:**

| Finding | Action |
|---------|--------|
| Prohibited use | Rejected. Chief Risk Officer notified. Decision documented. |
| Lower risk | Routed to Standard Review. |
| High risk | Routed to Full Review. System owner briefed on what is needed. |
| Directly affects Deaf users | Deaf Community Advisory Panel participation required, regardless of risk level. |
| Risk level unclear | Legal and Chief Privacy Officer consulted before routing. |

The system owner is notified of the outcome and expected timeline within 5 business days.

---

## Stage 3A: Standard Review (Lower Risk Systems)

**Timeline:** Up to 2 weeks
**Owner:** AI Governance Program Office

Covers:

- Confirming the risk level assigned at intake
- Checking that the data being used follows US and European privacy law and FCC rules on relay call confidentiality
- Confirming that humans will review AI outputs where appropriate
- Checking that users are told when AI is involved in decisions that affect them. For systems affecting Deaf users, this notice must be accessible, including an ASL summary where applicable
- Reviewing the vendor's data and AI practices, if this is a purchased system

**Who reviews:** The AI Governance Program Office, with the Chief Privacy Officer consulted when the system handles personal, biometric, or relay call data.

**Documents needed:**
- Completed submission form
- A privacy review, if the system handles personal data. This may include a formal Data Protection Impact Assessment if European privacy law requires one.
- A vendor practices questionnaire, if purchased from a vendor

---

## Stage 3B: Full Review (High Risk Systems)

**Timeline:** 4 to 6 weeks
**Owner:** AI Governance Program Office coordinates; AI Governance Committee approves

Covers everything in Standard Review, plus:

- A full structured risk assessment using the Project 2 format
- A review of how the system was built: what data it was trained on, how the model works, and whether the training data represents the people who will actually use it
- A plan for testing whether the system treats all users fairly. For systems affecting Deaf users, this must specifically address: variation in how different people sign, regional ASL differences, signers with physical limitations, and the difference between native ASL signers and oral Deaf users
- A documented human review plan: who checks the AI's outputs, when they can override it, and how that is logged. For relay and interpretation systems, this must include what happens on emergency calls.
- A plan for the formal legal compliance review required before high-risk AI systems go live
- A monitoring plan that tracks accuracy by user group, not just as a single overall number
- A plan for what to do when something goes wrong, including a specific plan for an AI interpretation failure during an emergency relay call

**Who reviews:**

| Reviewer | What they contribute |
|----------|-------------|
| AI Governance Program Office | Coordinates the review; produces the risk assessment |
| Chief Privacy Officer | Reviews privacy law compliance and the biometric data consent process |
| Legal / General Counsel | Reviews regulatory obligations under FCC, ADA, and AI law; reviews vendor contracts |
| Information Security | Reviews cybersecurity risks and whether the system can be manipulated or attacked |
| ML Engineering | Reviews whether the proposed technical controls are actually buildable |
| Independent auditor | Reviews whether the system treats all users fairly, for high-risk systems where bias is a concern |
| Deaf Community Advisory Panel | Required for any system that processes biometric data from Deaf users, operates in real-time relay or interpretation, sets accuracy standards for ASL AI, or affects emergency calls. This participation is not optional and cannot be skipped because of timeline pressure. |

**Documents needed:**
- Completed submission form
- Full risk assessment
- Technical documentation on how the system was built
- Vendor due diligence package, if purchased
- Fairness evaluation plan or completed fairness audit
- Human review procedure
- Monitoring plan
- Plain-language user disclosures in English, plus an ASL summary for systems affecting Deaf users

---

## Stage 4: Decision

**Standard Review:** The AI Governance Program Office and the system owner both sign off.

**Full Review:** The AI Governance Committee votes. A majority is required; the Chief Risk Officer plus at least two other members must be present.

**Conditional approval:** Approval can come with requirements that must be met before or after go-live. Every condition gets a named owner and a deadline. The system cannot go live if pre-launch conditions are not met.

SignalPath Interpret is the clearest example of what this looks like in practice. The Project 2 governance memo defined five conditions that must all be confirmed before any deployment date can be set.

**Rejection:** Documented and communicated to the system owner. The system can be resubmitted if the underlying concerns are addressed.

**When there is no consensus:** The decision moves up to the Chief Risk Officer. If that is contested, it goes to the Board Risk and Audit Committee. If conditions are not met and someone tries to set a deployment date anyway, the AI Governance Program Office escalates to the Chief Compliance Officer and the Board with a recommendation to block the launch.

---

## Stage 5: Go-Live and Registration

Before the system goes live, the system owner must:

1. Add the system to the AI System Inventory. The AI Governance Program Office records the approval date, any conditions, the risk level, and the next review date.
2. Complete all pre-launch conditions.
3. Confirm that monitoring is running before go-live.
4. Confirm that the people responsible for human review are trained and procedures are in place.
5. For high-risk systems: confirm that any required legal registrations are complete.
6. For systems affecting Deaf users: confirm that plain-language disclosures are live and that users have a way to flag errors directly in the product.

The AI Governance Program Office gives final go-live clearance before the system enters production.

---

## Stage 6: Ongoing Monitoring

**System owner responsibilities, ongoing:**
- Track performance against the thresholds set at approval
- For interpretation and captioning systems: track accuracy by user group. An overall accuracy number that hides poor performance for a specific group, such as oral Deaf users or signers with limited hand mobility, is not enough.
- Watch for the model performing worse over time or becoming less fair
- Keep human review procedures active and log every instance where a human overrides the AI
- Report significant problems to the AI Governance Program Office

**Scheduled reviews by the AI Governance Program Office:**

| Risk Level | How Often |
|-----------|------------------------|
| High Risk | At least once a year, plus any time a triggering event occurs |
| Limited Risk | Check-in with system owner once a year |
| Minimal Risk | Every two years, or when something significant changes |

**What triggers an unscheduled review:**
- A significant change to the system: new model version, expanded use, or new data
- An AI incident involving the system
- A change in laws or regulations that affects how the system must operate
- The system owner changes
- Performance drops below the defined threshold

---

## Significant Changes

Significant changes to an approved system require either a new submission form or a formal change request to the AI Governance Program Office. What counts as significant:

- The system's purpose or scope changes
- The system starts processing a new type of personal, biometric, or relay call data
- The underlying model is substantially updated: retrained on new data, rebuilt, or changed in a way that affects who it works well for
- The vendor changes
- The system is deployed in a new country or region, including expansion to UK operations or other international markets
- The system owner changes

Small changes, such as interface updates or bug fixes that do not affect how the model makes decisions, can be documented without a new review at the AI Governance Program Office's discretion.

---

*Process questions: ai-governance@signalpath.example*
