# EU AI Act Conformity Pack — Document 01
## Intended Purpose and System Description
**Article 11 | Annex IV**

**System:** SP-AI-001 SignalPath Interpret
**Organization:** SignalPath Technologies
**Version:** 1.0 | **Classification:** Internal — Governance Documentation
**Effective Date:** May 2026 | **Next Review:** May 2027
**Owner:** Chief Product Officer | **Prepared by:** AI Governance Program Office

---

## 1. System Identification

| Field | Detail |
|---|---|
| System ID | SP-AI-001 |
| System Name | SignalPath Interpret |
| System Category | Real-time ASL Interpretation AI |
| EU AI Act Risk Classification | High Risk — Annex III, Point 1(a) |
| Deployment Status | Limited Pilot — Pre-Production |
| Deployment Geography | United States (pilot); Canada and United Kingdom (planned) |
| Regulatory Scope | FCC Part 64, ADA Title IV, GDPR Articles 9 and 22, EU AI Act Annex III |

---

## 2. Intended Purpose

SignalPath Interpret is a real-time artificial intelligence system designed to support Video Relay Service (VRS) interpreting for Deaf and hard-of-hearing callers. The system performs automated recognition of American Sign Language (ASL) gestures — including hand shape, hand position, movement, facial expression, and body position — and generates a real-time natural language output for use by human VRS interpreters as an assistive overlay.

**The system is not deployed as a replacement for human interpreters.** Its intended function is augmentation: reducing cognitive load on human interpreters during high-volume call periods, improving response latency, and flagging confidence anomalies for human escalation.

The system's intended purpose is bounded by the following operational constraints, which are not adjustable without a formal governance review:

- The system operates only as an overlay to human interpreter capacity.
- Human interpreters retain final authority over all interpreted output delivered to the hearing party.
- Mandatory human handoff is triggered at any model confidence score below 0.85 on the Simulated Ingestion Model Confidence Score (SIMCS) metric.
- All emergency relay calls (911, 988, and equivalent) are routed exclusively to human interpreters. The system does not process or assist with emergency relay calls under any operational configuration.

---

## 3. System Architecture and Technical Description

### 3.1 Input

The system receives:

- Live video feed from the Deaf caller, captured via standard VRS client applications
- Audio feed from the hearing party (for context alignment, not for interpretation)
- Session metadata: call type, caller region, interpreter assignment

Input data constitutes biometric data under GDPR Article 4(14) and Article 9. Hand shape, facial expression, and body position are processed as identifying features of sign language gesture. This classification triggers the consent framework documented in Document 03 (Data Governance) and the processing safeguards documented in Document 04 (Human Oversight).

### 3.2 Model Architecture

SP-AI-001 uses a multi-stream convolutional neural network architecture trained on annotated ASL gesture sequences. The model processes:

- **Spatial stream:** frame-by-frame hand shape and facial configuration recognition
- **Temporal stream:** movement trajectory and transition pattern recognition
- **Fusion layer:** combined confidence scoring across spatial and temporal outputs

The model outputs a confidence-scored natural language segment, updated continuously at a rate consistent with real-time call processing requirements (target latency: under 200ms per segment).

### 3.3 Output

The system produces:

- A real-time natural language text stream delivered to the human interpreter's interface
- A per-segment confidence score (SIMCS, expressed as a percentage)
- A session-level aggregate confidence metric used for post-call audit and monitoring
- Automated threshold breach alerts at SIMCS < 0.85, triggering human escalation workflow

Outputs are not delivered directly to any end user. All output is mediated through a human interpreter.

### 3.4 Training Data Overview

Training data provenance and governance are documented in full in Document 03 (Data Governance). A summary:

- The model was trained on annotated ASL video datasets collected from consenting signers across multiple demographic groups.
- Known limitation: training data skews toward a narrower demographic range than the full SignalPath VRS user population, particularly with respect to skin tone, age, regional dialect variation, and physical variation in signing style.
- This limitation is the subject of RISK-001 (Signer Variation & Demographic Bias) in the SP-AI-001 Risk Register and the documented incident SP-INC-2026-001.

---

## 4. Intended Users

| User Category | Role | Access to System Output |
|---|---|---|
| VRS Interpreters | Primary operational users | Real-time overlay in interpreter interface |
| VRS Operations Management | Monitoring and escalation | Aggregate confidence dashboard |
| AI Governance Program Office | Compliance and audit | Full telemetry and audit logs |
| Engineering | Model maintenance and monitoring | Full system access |

Deaf and hard-of-hearing callers are the **affected population** — the people whose communications are mediated by the system — but are not direct system users. Their interests are represented in the governance structure through the Deaf Community Advisory Panel, documented in the Governance Operating Model.

---

## 5. Reasonably Foreseeable Misuse

In accordance with Article 9(2)(b) requirements, the following misuse scenarios were evaluated during risk assessment:

| Misuse Scenario | Assessment |
|---|---|
| Deployment without human oversight for standard calls | Prohibited by system architecture; confidence threshold enforcement is not operator-configurable |
| Use for emergency relay calls | Prohibited by hardcoded call routing logic; emergency call types are excluded at the session classification layer |
| Use as sole interpreter without human review of output | Not supported by the interface design; interpreter interface does not permit bypass of human review |
| Deployment in jurisdictions where biometric processing lacks a legal basis | Addressed in consent framework (Document 03); deployment requires jurisdiction-specific legal basis confirmation before go-live |
| Use for languages other than ASL | System is trained and validated on ASL only; deployment for other sign languages is not supported in v1.0 |

---

## 6. EU AI Act Annex IV Documentation Map

Annex IV of the EU AI Act specifies the technical documentation required for high-risk AI systems. The following table maps Annex IV requirements to documents within this conformity pack.

| Annex IV Requirement | Document |
|---|---|
| General description of the system and its intended purpose | This document (01) |
| Risk management system | Document 02 (Article 9) |
| Data governance and management practices | Document 03 (Article 10) |
| Technical robustness and accuracy metrics | Document 06 (Articles 15 + 17) |
| Human oversight measures | Document 04 (Article 14) |
| Logging and record-keeping | Document 05 (Article 12) |
| Post-market monitoring plan | Document 06 (Articles 15 + 17) |

---

## 7. Document Control

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | May 2026 | AI Governance Program Office | Initial release |

*This document forms part of the EU AI Act Conformity Pack for SP-AI-001 SignalPath Interpret. It is an internal governance document and does not constitute legal advice. Review by General Counsel is required prior to any regulatory submission.*
