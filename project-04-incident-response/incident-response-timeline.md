# Incident Response Timeline — AI-INC-2026-001

**Incident:** CreditScore Pro Postcode Bias
**Timeline Period:** March 2026 — May 2026

---

## Week 1 (10–14 March 2026): Detection and Immediate Response

### Day 1 — Tuesday 10 March
**Event:** Detection

- Data scientist identifies anomalous postcode-correlated score disparity during bias audit
- Initial finding documented and shared with ML Engineering manager
- Informal escalation to Head of Credit Risk begins

**Status:** Detection phase

---

### Day 2 — Wednesday 11 March
**Event:** Escalation and Initial Triage

- Head of Credit Risk convenes emergency call with ML Engineering lead and the data scientist
- Preliminary analysis confirms finding: the disparity is statistically significant and consistent across multiple postcode clusters
- Head of Credit Risk notifies AI Governance Programme Office
- AGPO classifies as Severity 1 incident (AI-INC-2026-001) and initiates incident response

**Notifications issued:**
- CRO notified (Day 2, within 24-hour requirement) ✓
- Legal and Compliance notified ✓
- Data Protection Officer notified ✓

**Immediate containment decision:**
AGPO and Head of Credit Risk recommend immediate suspension of automated decision-making for applications from affected postcodes, pending further investigation. Applications in the affected postcodes will be routed to manual underwriting review.

CRO approves containment measure.

---

### Day 3 — Thursday 12 March
**Event:** Containment Implemented; Board Notification

- CreditScore Pro model output for applications from affected postcode clusters is suspended as the sole decisioning input
- Applications from affected postcodes (approximately 15–20 per day) routed to manual underwriting queue
- Manual underwriting capacity confirmed adequate for interim volume
- Board Risk & Audit Committee Chair notified by CRO (within 48-hour requirement) ✓
- Extraordinary AI Governance Committee session scheduled for 14 March

**Legal and Compliance begin regulatory disclosure assessment:**
- EU AI Act Article 73 — does this constitute a "serious incident"?
- AFM — FCA equivalent, Netherlands — notification obligations?
- GDPR Article 22 — were past applicants informed of automated processing?

---

### Day 4–5 — Friday–Saturday 14–15 March
**Event:** AI Governance Committee Extraordinary Session

**Agenda:**
1. Incident briefing and confirmed scope
2. Containment status
3. Regulatory disclosure recommendation
4. Investigation plan approval
5. Customer communication approach

**Decisions made:**
1. Containment measure approved as ongoing pending model investigation
2. Legal and Compliance to prepare regulatory disclosure recommendation for CRO approval by 21 March
3. Independent external forensic analysis of model commissioned (ML bias consultancy engaged by Monday 16 March)
4. Past application review programme initiated: all applications from affected postcodes in the past 24 months to be reviewed
5. Customer communication: no proactive outreach to affected applicants until scope of harm is quantified (target: 28 March for outreach plan)
6. Internal communications: staff in Credit Risk, Customer Experience, and Compliance to receive briefing by 18 March

---

## Week 2 (16–20 March 2026): Investigation

### Actions

- External forensic analysis of CreditScore Pro model begins
- Internal data pull: all applications from affected postcodes since model go-live (March 2022 — March 2026)
- Full feature importance analysis commissioned to identify all features contributing to disparity
- DPO reviews whether GDPR Article 22 disclosures were made correctly for past automated decisions
- Legal begins drafting regulatory notification letters
- HR contacted: same postcode clusters exist in NorthStar's service area — check whether TalentMatch AI (NS-AI-003) exhibits same pattern

**Emerging findings (preliminary):**
- Postcode feature contributes approximately 8% to overall model score in the affected clusters
- The disparity has been present since model go-live; it was not introduced by a recent update
- Approximately 4 years of applications are in scope for retrospective review
- TalentMatch AI: HR Director confirms use in affected postcodes; separate bias review initiated

---

## Week 3 (23–27 March 2026): Scope Confirmation and Regulatory Engagement

### External Forensic Analysis — Preliminary Findings (24 March)

**Key findings:**
1. Postcode feature acts as a statistically significant proxy for ethnicity in 11 postcode clusters across Amsterdam and Rotterdam
2. The average score depression for affected applicants is 43 points (range: 31–67 points across clusters)
3. At NorthStar's credit policy thresholds, a 43-point depression translates to an increased rejection rate of approximately 12 percentage points for borderline applicants
4. The disparity cannot be explained by underlying creditworthiness differences — the model is introducing a bias, not measuring a real risk differential
5. Root cause (preliminary): postcode was included as a geographic feature without proxy analysis. The training data reflected historical lending patterns in those areas, which themselves reflected past discriminatory lending practices (redlining)

**Scope confirmed:**
- 4,127 applications from affected postcodes reviewed since March 2022
- 847 rejections that may have been influenced by the bias
- 1,892 approvals at potentially inflated interest rates

**Regulatory disclosure decision (27 March):**
CRO approves regulatory notifications:
- AFM formal notification submitted: 27 March 2026
- EU AI Act national authority (Dutch Authority for Digital Infrastructure) notified: 27 March 2026
- Data Protection Authority notified (GDPR Article 22 potential breach): 27 March 2026

---

## Week 4 (30 March – 3 April 2026): Customer Impact Assessment and Communication Plan

### Customer Impact Quantification

Finance and Credit Risk teams complete financial impact modelling:
- Total estimated excess interest charged to affected approved applicants: €2.3 million
- Estimated customers who were rejected but would have been approved under a fair model: 234 (based on re-scoring without postcode feature)

### Customer Communication Plan Approved (2 April)

**Decision:** Proactive outreach to all affected customers

Communication approach:
1. **Affected applicants who were rejected** — personal letter acknowledging that their application may have been unfairly assessed, offering a fresh review at no cost, with human underwriter making the decision
2. **Affected applicants who were approved at higher rates** — personal letter acknowledging potential overcharging, confirming they will receive a calculation of excess interest paid and a refund
3. **General customer notice** — published on NorthStar website: confirmation that a bias issue was identified and is being remediated

Legal approves communications. DPO confirms GDPR compliance.

**Customer outreach begins: 7 April 2026**

---

## Week 5–6 (6–17 April 2026): Remediation

### Model Remediation Plan (approved 6 April)

**Short-term (immediate):**
- Remove postcode as a feature from CreditScore Pro model
- Retrain model on adjusted dataset — postcode excluded
- Validate retrained model against fairness criteria before redeployment

**Medium-term (60 days):**
- Commission full fairness audit of retrained model by independent evaluator
- Implement ongoing demographic parity monitoring in production
- Establish automated alerts for emerging score disparities

**Model retraining timeline:**
- Postcode removal and retraining: 6 April – 30 April
- Internal validation: 1–14 May
- External fairness audit: 15–31 May
- Redeployment (with enhanced monitoring): 1 June 2026

**During remediation period:** All credit decisions from manual underwriting

### Retrospective Review Programme

- 847 rejected applications under review by external underwriting panel (NorthStar staff with conflict-of-interest recusal)
- Target: complete by 30 April 2026
- Applicants whose rejections are reversed will be contacted with a new offer

---

## Week 8–10 (May 2026): Root Cause Analysis and Lessons Learned

- Formal root cause analysis document completed (see [`root-cause-analysis.md`](./root-cause-analysis.md))
- AI Governance Committee reviews RCA and approves corrective action plan (15 May)
- Model retrained and independently validated
- External fairness audit completed

**Model redeployment approved: 2 June 2026** (conditional on enhanced monitoring controls being in place at go-live)

---

## Week 12 (9–13 June 2026): Incident Closure

**Closure conditions:**
- [x] All affected customers contacted
- [x] Retrospective review of rejected applications complete
- [x] Refunds calculated and issued
- [x] Retrained model independently validated
- [x] Fairness audit completed
- [x] Regulators updated with closure report
- [x] Root cause analysis and corrective actions documented and approved
- [x] Lessons learned shared with AI governance programme
- [x] Board notified of closure

**Incident closed: 12 June 2026**

---

## Incident Summary — Key Metrics

| Metric | Value |
|--------|-------|
| Detection to containment | 2 days |
| Detection to regulatory notification | 16 days |
| Affected applications reviewed | 4,127 |
| Rejections under retrospective review | 847 |
| Offers issued to previously rejected applicants | 234 |
| Excess interest refunded | €2.3 million |
| Days to model redeployment | 84 |
| Total incident duration | 95 days |

---

*This timeline is a simulation of a well-managed AI incident response. In practice, timelines vary significantly based on investigation complexity, regulatory requirements, and organisational capacity.*
