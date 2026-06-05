# EU AI Act Conformity Pack — Document 04
## Human Oversight Mechanisms
**Article 14**

**System:** SP-AI-001 SignalPath Interpret
**Organization:** SignalPath Technologies
**Version:** 1.0 | **Classification:** Internal — Governance Documentation
**Effective Date:** May 2026 | **Next Review:** May 2027
**Owner:** Chief Product Officer | **Prepared by:** AI Governance Program Office

---

## 1. Purpose and Scope

Article 14 of the EU AI Act requires that high-risk AI systems be designed and developed to allow effective human oversight during the period of use. Human oversight must be such that natural persons to whom oversight is assigned are able to understand the system's capabilities and limitations, detect and prevent system failures, and intervene or interrupt the system as necessary.

This document describes the human oversight architecture for SP-AI-001 SignalPath Interpret. SP-AI-001 operates in a domain where failure has direct consequences for essential communications for Deaf and hard-of-hearing users. Human oversight is therefore not a compliance checkbox — it is the primary safety control that makes controlled deployment of the system defensible.

---

## 2. Oversight Architecture Overview

SP-AI-001's oversight architecture operates at three levels:

| Level | Oversight Actor | Scope | Trigger |
|---|---|---|---|
| Call-level | Human VRS interpreter | Per-call, real-time | Always active |
| Operational | VRS Operations Manager | Aggregate session monitoring | Threshold breach or pattern alert |
| Governance | AI Governance Program Office | System-wide compliance and audit | Scheduled review and incident escalation |

Each level has defined responsibilities, tools, and escalation paths. None of these levels are optional in the current deployment configuration.

---

## 3. Call-Level Oversight: Human VRS Interpreter

### 3.1 Role and Authority

The human VRS interpreter is the primary oversight actor for every call processed with SP-AI-001 assistance. The interpreter:

- Receives the AI system's natural language output as an overlay in the interpreter interface
- Retains full authority over all interpreted output delivered to the hearing party
- Is not required to use, relay, or accept any AI-generated segment
- Can override the system output at any point during a call without any system-side restriction

The interpreter's authority over system output is absolute. There is no configuration, operator setting, or system state in which interpreter override is unavailable or restricted.

### 3.2 Confidence Threshold and Mandatory Handoff

The Simulated Ingestion Model Confidence Score (SIMCS) is displayed to the interpreter in real time. The system enforces the following threshold behaviours:

| SIMCS Level | System Behaviour | Interpreter Action Required |
|---|---|---|
| ≥ 85% | Normal operation; overlay provided | Interpreter exercises judgment on each segment |
| 80–84% | Elevated monitoring state; alert displayed | Interpreter actively reviews each segment before relay |
| < 80% | Threshold breach; mandatory escalation triggered | System flags for immediate human review; interpreter notified |
| < 75% | Critical exception; automated guardrail fires | System suspends AI overlay; interpreter operates without AI assistance; operations manager notified |

The mandatory handoff at SIMCS < 80% is not configurable by operators. It is a hardcoded system behaviour that cannot be disabled, adjusted, or bypassed through any user-facing or administrative interface.

### 3.3 Emergency Call Exclusion

All emergency relay calls — defined as calls to 911, 988, and equivalent emergency services — are excluded from AI-assisted processing at the session classification layer. When a session is classified as an emergency call:

- The AI overlay is not activated
- No AI-generated output is presented to the interpreter
- The interpreter operates under human-only protocols
- The session is flagged in telemetry for compliance audit

This exclusion is enforced before any AI processing begins. It is not dependent on confidence scoring or real-time performance metrics. It cannot be overridden by the interpreter, operator, or any system configuration.

### 3.4 Interpreter Training

VRS interpreters authorised to use SP-AI-001 must complete a training programme covering:

- System capabilities and documented limitations (including the demographic bias limitation documented in RISK-001)
- How to interpret the confidence score display and threshold alerts
- Override procedures and when to use them
- Escalation procedures for anomalous behaviour
- Emergency call routing procedures

Training completion is recorded and is a prerequisite for access to the AI-assisted interpreter interface.

---

## 4. Operational Oversight: VRS Operations Manager

### 4.1 Role and Authority

The VRS Operations Manager has aggregate-level oversight responsibility for SP-AI-001 performance across all active sessions. The Operations Manager:

- Monitors the Command Center dashboard for session-level and aggregate SIMCS metrics
- Receives automated alerts for threshold breaches and critical exceptions
- Has authority to suspend AI-assisted processing for any interpreter, any session type, or system-wide
- Is responsible for escalating anomalous patterns to the AI Governance Program Office

### 4.2 Command Center Telemetry

The Operations Manager's primary oversight tool is the AI Governance Center Command Center, which provides:

- **Live Control Monitor:** per-session SIMCS tracking for the active system target, with real-time threshold breach indicators
- **Aggregate metrics:** centralised oversight count, audit prep efficiency, high-critical risk vector count, and NIST maturity level
- **Automated alerts:** critical exception notifications when SIMCS drops below the 75% guardrail threshold, including automated guardrail action logs

The Command Center is designed to make anomalies visible at the aggregate level. The demographic monitoring that detected the SP-INC-2026-001 skin tone disparity was implemented at this level — a systematic confidence gap that was invisible in call-level metrics became detectable in aggregate demographic monitoring.

### 4.3 Automated Guardrail Actions

When SIMCS drops below the 75% critical exception threshold, the following automated actions fire without requiring human initiation:

1. AI overlay suspended for the affected session
2. Interpreter notified of suspension via interface alert
3. Operations Manager notified via dashboard alert
4. Incident escalation log created, including: timestamp, session ID, SIMCS value, guardrail action taken, response SLA (4 hours for P2 events)
5. Audit log entry created for compliance record

These actions are logged and cannot be suppressed. The audit trail generated by automated guardrails is the primary evidence base for compliance reporting.

---

## 5. Governance-Level Oversight: AI Governance Program Office

### 5.1 Role and Authority

The AI Governance Program Office (AGPO) has system-wide compliance and audit oversight responsibility for SP-AI-001. The AGPO:

- Reviews aggregate performance data and incident logs on a scheduled basis
- Owns the risk register and updates residual risk assessments based on operational evidence
- Escalates material findings to the AI Governance Committee, which includes C-suite accountability
- Maintains the conformity pack and ensures it reflects current system state
- Coordinates with the Deaf Community Advisory Panel on governance decisions affecting the Deaf and hard-of-hearing user population

### 5.2 Governance Review Cadence

| Review Type | Frequency | Output |
|---|---|---|
| Operational telemetry review | Monthly | AGPO internal report |
| Risk register update | Quarterly | Updated risk scores, open action tracking |
| Conformity pack review | Annual (or after material system change) | Updated conformity pack documents |
| Post-incident review | Within 30 days of any P1 or P2 incident | Incident summary, corrective action plan |
| AI Governance Committee review | Quarterly | Board-reportable governance status |

### 5.3 Article 14(4) — System Interruption

Article 14(4) requires that high-risk AI systems allow the natural persons responsible for oversight to interrupt the system. The following interruption mechanisms are available:

| Mechanism | Who Can Activate | Effect |
|---|---|---|
| Per-session override | VRS interpreter | Suspends AI overlay for current call; call continues with human-only interpretation |
| System-wide suspension | Operations Manager or AGPO | Suspends AI-assisted processing across all active sessions; can be executed from Command Center |
| Emergency exclusion | Automatic (session classification) | Prevents AI activation for emergency calls; not dependent on human action |
| Deployment rollback | Engineering (authorised by CPO) | Full system rollback to previous version or to human-only operation |

All interruption actions are logged. System-wide suspension requires a named authorisation from the Operations Manager or AGPO and is documented in the audit log.

---

## 6. Fundamental Rights Impact

Article 14(5) requires that human oversight take into account the risk of fundamental rights impact. SP-AI-001 serves Deaf and hard-of-hearing users, for whom VRS is an essential communications service — not a convenience. Failure of interpretation does not produce a degraded experience. It produces a communication blackout in contexts including medical appointments, legal proceedings, employment interactions, and emergency relay.

The human oversight architecture is designed with this consequence in mind. The mandatory handoff threshold (SIMCS < 0.85), the emergency call exclusion, and the interpreter's unrestrictable override authority exist because the cost of a missed override is not recoverable in real time. The system cannot go back and correctly interpret a 911 call that was mishandled.

The Deaf Community Advisory Panel's role in governance oversight is documented in the Governance Operating Model. The Panel was consulted in the design of the human oversight architecture and has approved the current threshold and exclusion design as a minimum acceptable standard.

---

## 7. Document Control

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | May 2026 | AI Governance Program Office | Initial release |

*This document forms part of the EU AI Act Conformity Pack for SP-AI-001 SignalPath Interpret. Review by General Counsel is required prior to any regulatory submission.*
