# Document 4: Human Oversight Mechanisms

**System:** HireAssist Pro (NS-AI-008)
**EU AI Act Reference:** Article 14 (Human Oversight)
**Document Type:** Deployer (NorthStar)
**Version:** 1.0 — March 2026

---

## 1. Purpose

Article 14 of the EU AI Act requires that high-risk AI systems be designed to enable effective human oversight. For deployers, this means implementing oversight measures that allow humans to:

- Understand the capabilities and limitations of the AI system
- Monitor the AI system's operation
- Detect and address failures, unexpected performance, or outputs causing harm
- Intervene and override AI outputs
- Decide not to use the AI output in a particular case

This document describes how NorthStar implements these requirements for HireAssist Pro.

---

## 2. Oversight Design Principles

NorthStar's human oversight model for HireAssist Pro is built on three principles:

**1. The AI recommends; the human decides.**
HireAssist Pro's output is a recommendation. No candidate communication — invitation to interview, rejection, or otherwise — may be sent based on AI output alone. A human must review, consider, and actively approve the decision.

**2. Oversight must be meaningful, not nominal.**
A reviewer who never overrides, or who approves recommendations without reading them, is not providing oversight. Oversight is meaningful when the reviewer has the knowledge, tools, and authority to challenge the AI. The oversight design includes training, UI features, and monitoring to make meaningful oversight the path of least resistance.

**3. Override is normal, not exceptional.**
Overriding the AI's recommendation is not a failure. It is the expected exercise of human judgment. The system and the culture around it must make override feel routine and supported.

---

## 3. Oversight Roles and Responsibilities

### HR Coordinator (Primary Reviewer)

**Who:** Trained HR coordinators assigned to each hiring process

**Oversight responsibilities:**
- Review the AI-generated shortlist and per-candidate fit assessment before any candidate communication
- Read the explanation text provided for each candidate's score
- Confirm, modify, or reject the shortlist based on independent judgment
- Record the decision and the reason for any modification to the AI recommendation
- Escalate any concerns about system behaviour to the Functional AI Champion (HR)

**Authority:** HR coordinators have full authority to override the AI shortlist for any reason. They are not required to justify overrides upward — only to document them.

**Training required:** HireAssist Pro Oversight Training (2 hours, mandatory before system access)

---

### Hiring Manager (Secondary Review — Roles Grade 5+)

**Who:** The manager who has raised the hiring request

**Oversight responsibilities:**
- Review and approve the shortlist produced by the HR coordinator (post-AI-review) for all roles at Grade 5 and above
- May request further modification before candidate invitations are sent
- Is informed that the shortlist passed through AI-assisted initial screening

**Training required:** AI-Assisted Recruitment Awareness Briefing (30 minutes)

---

### HR Director (Governance Oversight)

**Oversight responsibilities:**
- Monthly review of override rates across hiring processes
- Quarterly review of shortlisting statistics by demographic proxy (where data is available)
- Escalation point if a coordinator believes the system is producing biased or inconsistent results
- Annual attestation of system compliance with Responsible AI Policy and this oversight procedure

---

## 4. Oversight Workflow

```
[1] CANDIDATE APPLIES
     |
     v
[2] CV ingested by HireAssist Pro
     |
     v
[3] AI generates ranked shortlist + fit scores + explanation text
     |
     v
[4] HR COORDINATOR REVIEW
     |
     |--- Reviews shortlist (all candidates, not just top-ranked)
     |--- Reads explanation text for each candidate
     |--- Considers additional context not captured in CV
     |--- May: accept shortlist as-is / modify / expand / override entirely
     |--- Records decision and any modification reason in review log
     |
     v
[5] For roles Grade 5+: HIRING MANAGER REVIEW
     |--- Reviews coordinator-approved shortlist
     |--- May request further modification
     |
     v
[6] CANDIDATE COMMUNICATIONS
     |--- Invitations to interview sent to shortlisted candidates
     |--- Rejection communications sent to non-shortlisted candidates
     |--- Rejection communications include GDPR rights notice and challenge mechanism
     |
     v
[7] OUTCOME LOGGING
     - AI recommendation, coordinator decision, and any divergence recorded
     - Retained for 36 months
```

---

## 5. Override and Challenge Mechanism

### Internal override (HR Coordinator)

HR coordinators override the AI recommendation by:
1. Selecting "Modify shortlist" in the system interface
2. Documenting the reason for modification (free text, minimum 20 characters)
3. Confirming the modified shortlist

The system does not permit sending candidate communications until the review step is completed and the HR coordinator has made an active decision.

### Candidate challenge mechanism

Candidates who receive a rejection have the right to request human review under GDPR Article 22. The rejection communication includes:

> "Your application was reviewed by a member of our HR team. If you would like to understand the basis for this decision or request a further review, please contact [recruitment@northstar-financial.example] within 30 days."

Candidate challenges are triaged by the HR Director. Material challenges — where there is reason to suspect the AI recommendation was erroneous or biased — are reviewed by a senior HR manager who did not make the original decision.

---

## 6. System Features Supporting Oversight

HireAssist Pro v3.1 includes the following features specifically designed to support meaningful human oversight:

| Feature | Purpose |
|---------|---------|
| Explanation text per candidate | Enables reviewers to understand why the AI ranked a candidate as it did |
| Full candidate display | All candidates are shown, not just those above a threshold — reviewers can consider candidates the AI ranked low |
| Active confirmation required | System requires the reviewer to click "Confirm shortlist" — no passive acceptance |
| Override logging | All modifications to AI recommendations are automatically logged with timestamp and user ID |
| Confidence indicators | Where the AI's confidence in a score is low (high model uncertainty), this is flagged to the reviewer |
| Override rate dashboard | HR Director can view override rates by coordinator, role type, and time period |

---

## 7. Training Programme

### HireAssist Pro Oversight Training (HR Coordinators — 2 hours)

Module 1: How HireAssist Pro works (30 min)
- What the AI does and does not do
- How scores are generated
- What the explanation text represents and its limitations

Module 2: Your role as an overseer (30 min)
- What meaningful oversight looks like
- When and why to override
- What to do if you notice something wrong

Module 3: Practical exercises (45 min)
- Scenario-based exercises: when should you override?
- Practice using the interface
- Documenting your decisions

Module 4: Rights and responsibilities (15 min)
- Candidate rights and how to handle challenges
- Escalation paths
- Annual refresher requirements

**Completion requirement:** 100% of HR coordinators must complete training before system access is granted. New coordinators complete training during onboarding before joining any live hiring process.

---

## 8. Oversight Effectiveness Monitoring

| Metric | Measurement Method | Frequency | Threshold for Investigation |
|--------|------------------|-----------|--------------------------|
| Override rate (shortlist modifications) | System logs | Monthly | <5% triggers review (potential nominal oversight) |
| Time spent on review (average per application) | System logs | Monthly | <30 seconds per candidate triggers training review |
| Candidate challenge rate | HR records | Quarterly | >1% of rejections triggers fairness review |
| Training completion rate | LMS records | Ongoing | <100% triggers access suspension for non-compliant users |
| Coordinator confidence score (self-reported in review) | Survey module | Quarterly | — |

---

*This oversight procedure is a live document. Material changes to the workflow require AGPO review and approval.*
