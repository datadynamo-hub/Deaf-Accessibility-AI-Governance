# Document 6: Performance Monitoring Plan

**System:** HireAssist Pro (NS-AI-008)
**EU AI Act Reference:** Article 15 (Accuracy, Robustness, Cybersecurity) · Article 17 (Post-Market Monitoring)
**Document Type:** Deployer (NorthStar)
**Version:** 1.0 — March 2026

---

## 1. Purpose

Article 17 of the EU AI Act requires deployers of high-risk AI systems to implement a post-market monitoring plan that systematically collects and analyses performance data during the system's operational lifetime. Article 15 requires that high-risk AI systems achieve an appropriate level of accuracy and be robust to errors, faults, and inconsistencies.

This document defines NorthStar's monitoring plan for HireAssist Pro.

---

## 2. Monitoring Objectives

Post-deployment monitoring serves four objectives:

1. **Performance validation** — confirm the system continues to perform at or above accepted standards
2. **Fairness assurance** — detect emerging bias or disparate impact across candidate groups
3. **Oversight quality** — verify that human oversight is functioning as designed
4. **Drift detection** — identify when the candidate population or role requirements have shifted sufficiently that the model may need revalidation

---

## 3. Performance Metrics

### 3.1 Model Performance Metrics

These metrics measure whether the model is doing its job well:

| Metric | Definition | Target | Review Frequency | Alert Threshold |
|--------|-----------|--------|-----------------|----------------|
| **Shortlist acceptance rate** | % of AI-generated shortlists accepted by HR coordinators without modification | Baseline to be established in first 3 months of production | Monthly | >20% change from 3-month baseline |
| **Interview conversion rate** | % of AI-shortlisted candidates (including those not overridden) who progress to interview | Baseline to be established | Quarterly | >15% below baseline |
| **Explanation usefulness score** | HR coordinator self-reported rating of explanation text quality (1–5 scale) | ≥3.5 average | Quarterly | <3.0 for two consecutive quarters |
| **Special category data flag rate** | % of CVs triggering the special category data filter | Informational | Monthly | >10% (may indicate candidate population change) |

### 3.2 Fairness Metrics

These metrics detect potential discriminatory patterns in model outputs:

| Metric | Definition | Target | Review Frequency | Alert Threshold |
|--------|-----------|--------|-----------------|----------------|
| **Demographic parity ratio** | Ratio of shortlisting rate for protected group / shortlisting rate for reference group | ≥0.80 (for each measurable proxy group) | Quarterly | <0.80 or declining trend over two quarters |
| **Score distribution by proxy group** | Mean and standard deviation of AI scores by gender proxy, age band, name-inferred ethnicity proxy | No statistically significant difference between groups | Quarterly | p<0.05 significance in mean difference |
| **Override rate by candidate group** | Whether HR coordinators override AI recommendations at different rates for different candidate groups | No systematic pattern | Quarterly | Statistically significant difference |
| **Rejection rate by application source** | Whether candidates from specific recruitment channels are rejected at higher rates | No unexplained variation | Quarterly | >15% variation unexplained by role-specific factors |

**Note on demographic data:** NorthStar does not collect protected characteristic data from applicants. Proxy indicators are used (name-based gender and ethnicity inference, application metadata). These proxies are imperfect and monitoring results must be interpreted with that limitation acknowledged. Where proxy-based analysis identifies a potential issue, manual review of a sample is conducted.

### 3.3 Oversight Quality Metrics

These metrics verify that human oversight is functioning as designed:

| Metric | Definition | Target | Review Frequency | Alert Threshold |
|--------|-----------|--------|-----------------|----------------|
| **Override rate** | % of AI shortlists modified by HR coordinator | Target: 10–40% (meaningful oversight range) | Monthly | <5% (possible nominal oversight) or >80% (possible model failure) |
| **Review time (median)** | Median time spent by coordinator reviewing each candidate on shortlist | ≥45 seconds per candidate | Monthly | <30 seconds (insufficient review time) |
| **Challenge rate** | % of rejection decisions challenged by candidates | Informational | Quarterly | >2% (indicates potential systemic issue) |
| **Training currency** | % of active system users with current training certification | 100% | Monthly | <100% triggers access suspension for non-compliant users |

---

## 4. Monitoring Cadence and Responsibilities

| Activity | Frequency | Owner | Output |
|----------|-----------|-------|--------|
| Automated metric dashboard refresh | Daily | IT / AGPO (automated) | Dashboard — accessible to HR Director and AGPO |
| Override rate review | Monthly | HR Director | Escalation to AGPO if threshold triggered |
| Full performance report | Quarterly | AGPO | Report to AI Governance Committee |
| Fairness analysis | Quarterly | AGPO + ML Engineering | Included in quarterly report |
| Annual system review | Annual | AGPO | Full system review — feeds renewal decision |
| Vendor model performance report | Quarterly (from HireFlow) | Head of Credit Risk (as contract contact) | Reviewed by AGPO; escalate material changes |

---

## 5. Drift Detection and Model Revalidation Triggers

The model must be revalidated if any of the following triggers occur:

| Trigger | Rationale |
|---------|-----------|
| Demographic parity ratio drops below 0.80 for any measurable group | Potential emerging discriminatory pattern |
| Interview conversion rate declines >15% from baseline for two consecutive quarters | Model may no longer be matching candidates effectively to roles |
| NorthStar's candidate population changes significantly (e.g., entry into new geographies, new role types) | Model trained on existing patterns may not generalise |
| HireFlow releases a new model version | Material change requires NorthStar validation before acceptance |
| AI incident involving HireAssist Pro | Post-incident revalidation standard |
| 24 months since last full revalidation (if no other trigger) | Scheduled revalidation cycle |

When a revalidation trigger is reached, AGPO initiates a revalidation review. The system continues to operate during revalidation unless AGPO determines there is a material risk requiring suspension.

---

## 6. Vendor Monitoring Obligations

NorthStar relies on HireFlow Technologies Ltd to:

- Notify NorthStar of any material model changes ≥60 days in advance
- Provide quarterly performance reports covering accuracy, fairness, and known issues
- Report any serious incidents involving HireAssist Pro across its customer base within 24 hours of discovery
- Maintain the technical documentation and make it available to NorthStar on request
- Cooperate with regulatory inspections that relate to HireAssist Pro

These obligations are contractually captured. Failure to meet notification or reporting obligations is a material contract breach.

---

## 7. Serious Incident Reporting

If post-deployment monitoring detects a potential serious incident (e.g., discriminatory outcomes affecting a protected group), the following escalation applies:

```
[Detection] Metric alert triggered or complaint received
     |
     v
[AGPO triage] Is this a potential serious incident? (24h)
     |
     +---> No: Document finding; increase monitoring frequency
     |
     +---> Yes: Initiate AI Incident Response (AI-INC classification)
              |
              v
           [AI Governance Committee] Notified within 24h
              |
              v
           [Assess regulatory reporting obligation] (Article 73, EU AI Act)
              |
              v
           [Containment, investigation, remediation] per incident response procedure
```

---

## 8. Annual System Review

At the 12-month mark from go-live (target: June 2027 for first review), AGPO will conduct a full annual system review covering:

1. Performance summary against all metrics in this plan
2. Fairness analysis summary
3. Incident log review
4. Oversight quality assessment
5. Vendor performance assessment
6. Regulatory change assessment (any new obligations that affect the system)
7. Recommendation: continue as-is / modify / decommission

The annual review is presented to the AI Governance Committee. Continuation of the system in production is conditional on a satisfactory review.

---

## 9. Documentation and Retention

All monitoring outputs — dashboards, quarterly reports, annual reviews, incident records, revalidation findings — are retained for 36 months and stored in the AI Governance Programme Office documentation archive. They are available for regulatory inspection.

---

*This monitoring plan is a living document. Metric thresholds and review frequencies may be adjusted based on experience in the first year of operation, subject to AGPO approval.*
