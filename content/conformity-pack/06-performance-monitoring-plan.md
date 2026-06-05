# EU AI Act Conformity Pack — Document 06
## Performance Monitoring Plan
**Articles 15 + 17**

**System:** SP-AI-001 SignalPath Interpret
**Organization:** SignalPath Technologies
**Version:** 1.0 | **Classification:** Internal — Governance Documentation
**Effective Date:** May 2026 | **Next Review:** May 2027
**Owner:** Chief Product Officer | **Prepared by:** AI Governance Program Office

---

## 1. Purpose and Scope

Article 15 of the EU AI Act requires that high-risk AI systems achieve appropriate levels of accuracy, robustness, and cybersecurity throughout their lifecycle, and that accuracy metrics and robustness performance be declared. Article 17 requires that providers establish quality management systems that include post-market monitoring plans.

This document describes SignalPath's performance monitoring plan for SP-AI-001 SignalPath Interpret, covering accuracy metrics and thresholds, robustness requirements, drift detection, post-market monitoring architecture, and the governance process for acting on monitoring findings.

---

## 2. Performance Baseline

### 2.1 Accuracy Metrics

SP-AI-001's primary accuracy metric is the Simulated Ingestion Model Confidence Score (SIMCS), a per-segment confidence score expressed as a percentage (0–100). The SIMCS reflects the model's self-assessed confidence in its natural language output for each ASL gesture segment processed.

The SIMCS is the operational proxy for accuracy because direct accuracy measurement (comparing AI output to a ground-truth interpretation) is not feasible in real-time call processing. Post-call accuracy assessment is conducted through a sampling programme described in Section 4.

| Metric | Definition | Pre-Production Baseline | Pilot Target |
|---|---|---|---|
| Session-level mean SIMCS | Average SIMCS across all segments in a session | 85% | ≥ 85% |
| Threshold breach rate | Percentage of sessions with at least one SIMCS < 80% event | Established in pilot | < 5% of sessions |
| Critical exception rate | Percentage of sessions with at least one SIMCS < 75% event | Established in pilot | < 1% of sessions |
| Demographic parity gap | Difference in mean SIMCS between highest and lowest demographic group | Established in pilot; SP-INC-2026-001 identified skin tone gap | < 5 percentage points |
| Human override rate | Percentage of AI-generated segments overridden by interpreters | Established in pilot | Monitored; no fixed threshold (interpreter judgment is valid) |

Baseline values for pilot metrics will be established during the first 90 days of limited pilot operation. Production deployment targets will be set based on pilot baseline evidence and reviewed by the AI Governance Committee before production deployment clearance.

### 2.2 Accuracy Declaration

In accordance with Article 15(1), the following accuracy limitations are declared:

1. **Demographic variation:** Model accuracy varies systematically across demographic groups. Skin tone disparity was documented in SP-INC-2026-001. Age, regional dialect, and physical variation in signing style represent known but less precisely quantified gaps. Performance metrics published for v1.0 represent aggregate accuracy and likely overstate accuracy for underrepresented demographics.

2. **Language scope:** The model is validated on ASL only. Performance on other sign languages (BSL, LSF, ISL, etc.) is not tested and is not expected to be reliable.

3. **Environmental variation:** Model performance is sensitive to video quality, lighting conditions, and background complexity. Performance in low-quality video conditions is not separately characterised in v1.0.

4. **Temporal drift:** Model accuracy will degrade over time as ASL continues to evolve. The retraining cadence described in Section 5 is designed to manage but not eliminate this risk.

### 2.3 Robustness Requirements

Article 15(3) requires that high-risk AI systems be resilient to errors, faults, and inconsistencies. The following robustness requirements are in place for SP-AI-001:

| Requirement | Implementation |
|---|---|
| Graceful degradation at threshold | At SIMCS < 80%, system reduces output frequency and flags segments for interpreter review rather than failing silently |
| Failsafe at critical exception | At SIMCS < 75%, system suspends AI overlay and reverts to human-only interpretation. Human interpretation remains fully available. |
| Emergency call failsafe | Emergency calls are excluded from AI processing at the session classification layer, before any model inference occurs |
| Network and latency resilience | Target inference latency < 200ms per segment; latency breaches above 500ms trigger automatic suspension of AI overlay for the affected session |
| Model serving redundancy | Model serving infrastructure is deployed with redundancy sufficient to maintain availability at VRS peak load; failover to human-only interpretation is automatic if serving infrastructure is unavailable |

---

## 3. Real-Time Monitoring

### 3.1 Command Center Live Control Monitor

The primary real-time monitoring tool is the AI Governance Center Command Center's Live Control Monitor. For each active system target, the Live Control Monitor displays:

- Current session SIMCS, updated in real time
- Threshold state indicator (normal / elevated / breach / critical)
- Automated alert display for threshold breach and critical exception events
- Guardrail action log for the current session

The Operations Manager and AGPO monitor the Command Center continuously during operational hours. Automated alerts are sent to on-call engineering and operations staff for critical exception events outside monitored hours.

### 3.2 Aggregate Dashboard Metrics

The Command Center dashboard provides aggregate metrics that surface system-wide patterns:

| Metric | What It Detects |
|---|---|
| Centralised oversight count (active systems) | Registry completeness and operational scope |
| High-critical risk vector count | Risk register changes requiring escalation |
| Threshold breach rate trend | Early signal of model degradation or environmental drift |
| Demographic confidence monitoring | Systematic accuracy gaps correlated with user demographics |

The demographic confidence monitoring panel was added to the Command Center following SP-INC-2026-001. It was not part of the original v1.0 design. This is documented as a corrective action from that incident.

---

## 4. Post-Market Monitoring

### 4.1 Sampling-Based Accuracy Assessment

Because real-time accuracy assessment against a ground truth is not feasible, SignalPath operates a sampling programme for post-call accuracy assessment:

- A random sample of 5% of AI-assisted calls is selected for post-call review
- Sampled calls are reviewed by a Deaf ASL-fluent quality assessor who evaluates the AI output against the interpreted content
- Assessors are not informed of the SIMCS for the sampled session to prevent anchoring
- Accuracy assessment results are recorded against the session's demographic metadata to enable demographic disaggregation

Post-call accuracy assessment results are aggregated monthly and reviewed by the AGPO. Significant divergence between SIMCS and post-call accuracy assessment is escalated to Engineering for investigation.

### 4.2 Drift Detection

Statistical process control monitoring is applied to SIMCS distributions to detect systematic degradation before it reaches threshold levels:

- Control charts track rolling mean and standard deviation of SIMCS across sessions
- Signals for investigation: mean SIMCS declining more than 3 percentage points over a 30-day window; standard deviation increasing more than 2 percentage points over a 30-day window
- Demographic drift: same SPC monitoring applied to demographic subgroups; a subgroup diverging from aggregate trend triggers a targeted investigation

Drift detection alerts are reviewed by Engineering and the AGPO. Confirmed drift triggers the retraining assessment process described in Section 5.

### 4.3 Incident-Triggered Review

Any P1 or P2 incident (as classified in the Incident Response Simulator) triggers a mandatory post-incident performance review:

- Review of SIMCS logs for the affected period and session types
- Demographic analysis of confidence score distributions
- Root cause assessment: inference-time failure vs. training data gap vs. environmental factor
- Corrective action determination and owner assignment
- Completion within 30 days of incident classification

The SP-INC-2026-001 post-incident performance review followed this process and produced the corrective actions documented in Document 02 (Risk Management Summary, RISK-001).

---

## 5. Retraining and Model Updates

### 5.1 Retraining Cadence

| Trigger | Action |
|---|---|
| Scheduled annual refresh | Full retraining with updated data corpus; mandatory before each calendar year anniversary of deployment |
| Drift detection signal | Retraining assessment initiated within 30 days of confirmed drift signal |
| Post-incident corrective action | Retraining with targeted data augmentation, timeline set in corrective action plan |
| Material demographic gap identified | Retraining with expanded demographic coverage; timeline set by AGPO |

### 5.2 Model Update Governance

All model updates — including retraining runs and version increments — require:

1. Documented rationale for the update
2. Evaluation against the accuracy metrics in Section 2.1 on held-out test data
3. Demographic disaggregation of evaluation results
4. Review and sign-off by the AGPO before deployment
5. Chief Product Officer approval for production deployment
6. Updated conformity pack assessment for any material change to system capabilities or limitations

Model updates that materially change the system's intended purpose, capabilities, or risk profile require a new governance gate review before deployment.

### 5.3 Version Control

Each deployed model version is assigned a version identifier. The mapping of model version to deployment date, training data vintage, and evaluation results is maintained in the Engineering data registry and is available to the AGPO for audit purposes.

---

## 6. Quality Management System

### 6.1 Article 17 QMS Coverage

Article 17 requires that providers of high-risk AI systems put in place a quality management system. The QMS for SP-AI-001 covers:

| QMS Element | Location |
|---|---|
| Strategy for regulatory compliance | Responsible AI Policy (Governance Hub, Tab 1) |
| Techniques for system design and development | System design specification (Engineering, internal) |
| Testing and validation procedures | This document (Sections 2–4) and Document 02 (risk assessment) |
| Data management practices | Document 03 (Article 10) |
| Risk management system | Document 02 (Article 9) |
| Post-market monitoring | This document (Section 4) |
| Incident reporting procedures | Governance Hub — Incident Response Simulator; Document 05 (Article 12) |
| Handling of non-conformities and corrective action | Risk register corrective action tracking; post-incident review process |
| Human oversight procedures | Document 04 (Article 14) |
| Record-keeping and documentation | Document 05 (Article 12) |

### 6.2 Continuous Improvement Targets

The AI Governance Center Command Center displays a NIST AI RMF Maturity Level metric tracking SignalPath's governance maturity against a 5.0 target. Current maturity at v1.0 conformity pack completion: 2.0 / 5.0. This reflects a governance programme in active development, not a mature production system. The maturity target trajectory:

| Milestone | Target Maturity | Key Requirements |
|---|---|---|
| Conformity pack completion (current) | 2.0 | Documentation framework in place |
| Pilot completion | 3.0 | Operational monitoring baseline established; DPIA complete |
| Production deployment | 3.5 | Full demographic monitoring; v1.1 training data refresh complete |
| 12 months post-production | 4.0 | First annual retraining cycle complete; post-market monitoring mature |
| 24 months post-production | 5.0 | Full NIST RMF implementation; external audit completed |

---

## 7. Document Control

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | May 2026 | AI Governance Program Office | Initial release |

*This document forms part of the EU AI Act Conformity Pack for SP-AI-001 SignalPath Interpret. Review by General Counsel is required prior to any regulatory submission.*
