# Document 5: Logging and Traceability

**System:** HireAssist Pro (NS-AI-008)
**EU AI Act Reference:** Article 12 (Record-Keeping)
**Document Type:** Provider (HireFlow) + Deployer (NorthStar)
**Version:** 1.0 — March 2026

---

## 1. Purpose

Article 12 of the EU AI Act requires that high-risk AI systems have logging capabilities that enable traceability of the system's operation. Logs must enable, at a minimum:

- Post-hoc verification that the system operated as intended
- Identification of the circumstances under which the system was used (Article 12(1))
- Detection and investigation of incidents
- Evidence for compliance audits and regulatory investigation

This document describes the logging architecture and traceability approach for HireAssist Pro as deployed at NorthStar.

---

## 2. What Must Be Logged

For a recruitment AI system, the following events must be logged to satisfy Article 12 and enable meaningful incident investigation:

| Event Category | Specific Events | Rationale |
|---|---|---|
| **System inputs** | Job description submitted; CV ingested; candidate ID; submission timestamp | Enables reconstruction of what data the model processed |
| **Model outputs** | Fit score per candidate; ranking; explanation text generated; model version; inference timestamp | Enables review of what the AI recommended and why |
| **Reviewer actions** | Review initiated; reviewer ID; shortlist confirmed or modified; modification details; decision timestamp; time spent on review | Creates accountability record and enables oversight effectiveness monitoring |
| **Candidate communications** | Communication type (invitation/rejection); sent timestamp; communication ID | Links AI recommendation chain to actual decision communicated to candidate |
| **Overrides** | Override initiated; reason text; new shortlist; reviewer ID | Key evidence for fairness investigation and oversight quality monitoring |
| **Model version** | Version number at time of each inference | Enables correlation of issues to specific model versions |
| **System exceptions** | Special category data flag triggered; low-confidence flag triggered; system errors | Enables investigation of anomalous cases |
| **Access and authentication** | User login/logout; role; session duration | Standard access audit trail |

---

## 3. Logging Architecture

### 3.1 Provider Logging (HireFlow)

HireFlow Technologies Ltd maintains the following logs at the model/API layer:

| Log Type | Retention | Location | Access |
|----------|-----------|---------|--------|
| API request logs (input hash, timestamp, model version) | 36 months | HireFlow secure infrastructure (EU region) | Available to NorthStar on request; regulatory access within 72h |
| Model output logs (score, explanation, timestamp) | 36 months | HireFlow secure infrastructure | Available to NorthStar on request |
| Model version history | Indefinite | HireFlow system records | Available on request |

**NorthStar's contractual log access rights:** NorthStar has the right to request logs for any application processed through the API within the retention period. Requests are fulfilled within 5 business days for standard requests, within 24 hours for incident investigation requests.

### 3.2 Deployer Logging (NorthStar)

NorthStar maintains the following logs in its own infrastructure (Workday ATS integration + SIEM):

| Log Type | Retention | Location |
|----------|-----------|---------|
| Full application audit trail (all events above) | 36 months | NorthStar secure infrastructure (EU) |
| Reviewer action log | 36 months | NorthStar HR systems |
| Candidate communication record | 36 months | NorthStar HR systems |
| Override log | 36 months | NorthStar HR systems |
| Model output copy (for each inference used) | 36 months | NorthStar data warehouse |

**Why 36 months?** This retention period is set to cover:
- EU employment law dispute limitation periods (typically 3 years for discrimination claims in NL and DE)
- EU AI Act audit and investigation timelines
- NorthStar's internal governance review cycle

---

## 4. Traceability by Use Case

### Tracing a specific candidate decision

For any candidate who applies and receives a decision, the full decision chain can be reconstructed:

```
Candidate X applies for Role Y
  → CV ingested at [timestamp]
  → Model v3.1.2 generates score 72/100 with explanation [text] at [timestamp]
  → HR Coordinator A reviews at [timestamp], spends 4 minutes
  → Coordinator modifies shortlist: removes candidate X (override reason: "Insufficient financial services experience for this specific role")
  → Rejection communication sent to Candidate X at [timestamp]
  → Log entry: override recorded, reason stored, reviewer ID recorded
```

This chain provides:
- Evidence of human oversight (review and override)
- Basis for explanation to the candidate if challenged
- Evidence for regulatory audit

### Tracing a potential bias pattern

For a bias investigation examining whether candidates from a specific demographic group were systematically ranked lower:

```
Query: All applications for Role Type = Analyst, Period = Q1 2026
  → Extract: scores by candidate, model version, reviewer decision
  → Cross-reference: candidate demographic proxy indicators (where available)
  → Analyse: distribution of scores and final decisions by group
  → Examine: override patterns — were lower-scoring group candidates recovered through override?
```

The log structure enables this analysis. The availability of demographic data for cross-referencing depends on what candidates disclosed — NorthStar does not require demographic disclosure as a condition of application.

---

## 5. Log Integrity and Security

| Control | Implementation |
|---------|--------------|
| Log immutability | Logs written to append-only storage; modification requires CISO-level approval and creates audit entry |
| Encryption at rest | AES-256 encryption for all stored logs |
| Access controls | Role-based access: AGPO, DPO, Legal, and Information Security have read access; only automated processes have write access |
| Log tampering detection | Hash-chaining on critical log entries (model output, reviewer decision) |
| Backup | Daily backup to geographically separate EU region |
| Regulatory access | Logs are producible for regulatory inspection within 24 hours of formal request |

---

## 6. Log Review and Monitoring

Logs are actively monitored (not just stored) as part of the ongoing governance of the system:

| Log Review Activity | Frequency | Owner |
|--------------------|-----------|-------|
| Override rate monitoring | Monthly | HR Director |
| Review time analysis (oversight effectiveness) | Monthly | AGPO |
| Score distribution analysis by job type | Quarterly | AGPO + ML Engineering |
| Demographic parity analysis (where proxy data available) | Quarterly | AGPO |
| Access audit review | Quarterly | Information Security |
| Full log audit | Annual | Internal Audit |

Anomalies detected through log monitoring trigger escalation to AGPO and, if material, initiation of an AI incident review.

---

## 7. Limitations and Known Gaps

| Limitation | Mitigation |
|-----------|-----------|
| Demographic data availability | Candidates are not required to disclose protected characteristics. Demographic parity analysis relies on proxy indicators, which are imperfect. | Monitoring is conducted on available data; limitations are documented in each monitoring report. |
| Provider log access is request-based, not real-time | For real-time incident investigation, NorthStar relies on its own logs. Provider logs provide deeper model-layer detail but require a request process. | Incident response procedure accounts for this; provider logs are requested within 24h of a severity 1 incident. |

---

*Log architecture and retention schedules are reviewed annually as part of the system governance review. Changes to log scope require AGPO approval.*
