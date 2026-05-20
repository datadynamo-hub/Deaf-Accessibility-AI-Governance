# Incident Response Timeline: SP-INC-2026-001

**Incident:** SP-AI-001 Skin Tone Accuracy Disparity
**Timeline Period:** May 2026 to July 2026

---

## Week 1 (4–8 May 2026): Detection and Immediate Response

### Day 1: Sunday 4 May
**Event:** Detection via Deaf Community Advisory Panel

- Advisory Panel member submits written report to the AGPO describing elevated interpretation errors among her network of POC (proof of concept) participants
- Report flagged for engineering review on Monday morning

**Status:** Detection initiated

---

### Day 2: Monday 5 May
**Event:** Engineering Triage

- AGPO reviews Advisory Panel report; engineering team tasked with confidence score log analysis
- Initial log pull begins: confidence scores segmented by video luminance proxy measure
- AGPO notifies Chief Product Officer of potential fairness anomaly

**Status:** Triage in progress

---

### Day 3: Tuesday 6 May
**Event:** Finding Confirmed; Severity 1 Declared

- Engineering completes initial luminance analysis: 17-percentage-point confidence score gap confirmed between lower and upper luminance quartiles
- Handoff rate disparity confirmed: 3.2x higher for lower luminance quartile
- AGPO classifies as Severity 1 incident (SP-INC-2026-001) and initiates formal incident response

**Notifications issued:**
- Chief Risk Officer notified (Day 3, within 24-hour requirement) ✓
- General Counsel notified ✓
- Chief Privacy Officer notified ✓
- Chief Information Security Officer notified ✓

**Immediate containment recommendation:**
AGPO and Chief Product Officer recommend suspension of AI interpretation for the affected user group, pending further investigation. All POC calls to route to human interpreters during investigation period.

Chief Risk Officer approves containment measure.

---

### Day 4: Wednesday 7 May
**Event:** Containment Implemented; Board Notification

- SignalPath Interpret AI pipeline suspended for all POC calls. Full human interpreter routing activated.
- POC participants notified of temporary service change (framed as a planned system review, not an incident; legal review of communications language completed same day)
- Board Risk and Audit Committee Chair notified by Chief Risk Officer (within 48-hour requirement) ✓
- Extraordinary AI Governance Committee session scheduled for 9 May
- Incident document (SP-INC-2026-001) drafted and circulated internally

**Legal and Compliance begin regulatory disclosure assessment:**
- FCC (Federal Communications Commission) Part 64: does the disparity constitute a functional equivalency breach requiring FCC notification?
- EU AI Act Article 73: do any POC participants have EU data subject status (travelers) triggering serious incident reporting?
- BIPA: are any affected POC participants Illinois residents?
- GDPR (General Data Protection Regulation) Article 9: biometric data processing resulting in discriminatory output

---

### Day 5–6: Friday–Saturday 9–10 May
**Event:** AI Governance Committee Extraordinary Session

**Agenda:**
1. Incident briefing and confirmed scope
2. Containment status and POC suspension
3. Regulatory disclosure assessment
4. Investigation plan approval
5. Deaf Community Advisory Panel engagement plan

**Decisions made:**
1. Full POC suspension maintained pending investigation. No timeline for resumption until root cause is confirmed and training data remediation plan is approved.
2. Legal and General Counsel to prepare regulatory disclosure recommendation for Chief Risk Officer approval by 16 May
3. Engineering to conduct full training dataset audit: skin tone representation, dataset provenance documentation, luminance distribution across training samples; target: 23 May
4. External AI fairness specialist to be engaged for independent validation of engineering findings (engagement by 12 May)
5. Deaf Community Advisory Panel to be briefed directly on the incident by AGPO and Chief Product Officer by 14 May. No governance decision about remediation scope until Panel has provided input.
6. Internal communications: all staff in Interpreting Services, Product Management, and Advanced Sign Technology (AST) to receive briefing by 14 May

---

## Week 2 (11–15 May 2026): Investigation

### Actions

- External AI fairness specialist begins independent review of engineering findings
- Full training dataset audit underway: skin tone distribution, luminance representation across training samples, geographic and demographic tagging review
- AGPO reviews whether demographic monitoring was operational at POC launch. Preliminary finding: demographic segmentation layer was scheduled for post-launch configuration, not operational at launch (control gap documented).
- Legal drafts regulatory notification letters for FCC and EU AI Act authority pending scope confirmation
- Chief Privacy Officer reviews GDPR Article 9 exposure: biometric data processing producing discriminatory outputs across the POC period

**Deaf Community Advisory Panel briefing (14 May):**
- Panel briefed on full incident findings by AGPO and Chief Product Officer
- Panel raises additional scope question: skin tone is one dimension; the underlying training data likely has other unaudited demographic gaps (signing dialect, age-related hand morphology, physical limitations)
- Panel recommends that remediation scope extend to comprehensive demographic representation audit, not a targeted skin tone fix
- AGPO documents Panel input; Committee to consider expanded remediation scope

**Emerging findings (preliminary):**
- Training dataset skin tone distribution: estimated 74% of training samples with luminance values corresponding to lighter skin tones; 26% darker: significant underrepresentation
- Normalization algorithm calibration was never tested against a skin-tone-stratified evaluation set
- Dataset provenance documentation: no skin tone or demographic composition fields recorded at dataset assembly

---

## Week 3 (18–22 May 2026): Scope Confirmation and Regulatory Engagement

### External Fairness Specialist Preliminary Findings (21 May)

**Key findings:**
1. Skin tone proxy correlation confirmed as statistically significant: not an artifact of the luminance measurement approach
2. The normalization algorithm introduces the primary performance gap before the classification model processes input. This means the classification model's accuracy figures in aggregate testing masked the disparity.
3. The 17-percentage-point confidence gap translates to a materially worse interpretation experience: longer pauses, higher error rates on low-frequency vocabulary, more frequent LCL breaches
4. The disparity is present throughout the POC period from first deployment. It was not introduced by a model update.
5. Panel's expanded scope recommendation is warranted: preliminary analysis of age-related signing variation and physical limitation variation also shows performance gaps, at lower magnitudes

**Scope of affected calls confirmed:**
- POC duration: 14 March to 6 May 2026 (52 days)
- Estimated calls in lower luminance quartile during that period: under investigation; preliminary estimate 1,800–2,400 calls
- No emergency calls in the affected group: emergency routing to human interpreters was operational throughout

**Regulatory disclosure decision (22 May):**
Chief Risk Officer approves regulatory notifications:
- FCC informal notification of potential functional equivalency concern submitted: 22 May 2026
- Assessment of EU AI Act Article 73 obligations: pending determination of whether any affected POC participants hold EU data subject status during calls

---

## Week 4–5 (25 May – 5 June 2026): Remediation Planning

### Remediation Scope Approved (29 May)

Following Deaf Community Advisory Panel input and external specialist findings, the AI Governance Committee approves an expanded remediation scope:

**Immediate (before any further POC or production deployment):**
- Full demographic representation audit of training dataset across: skin tone, age-related hand morphology, physical limitation variation (including limited finger mobility), regional ASL (American Sign Language) dialect, oral Deaf signer variation, BASL (Black American Sign Language) phonological features
- Normalization algorithm redesign and recalibration on a demographically balanced evaluation set
- Minimum representation thresholds defined for each demographic dimension before retraining begins

**Retraining plan:**
- Supplemental training data collection: engage Deaf community organizations to recruit consenting participants across underrepresented demographic dimensions
- Retraining conducted on expanded dataset
- Fairness evaluation per demographic segment before any redeployment, not aggregate accuracy only.

**Retraining timeline:**
- Supplemental data collection: 1 June – 31 July 2026
- Normalization algorithm redesign: 1 June – 30 June 2026
- Model retraining on expanded dataset: 1 August – 31 August 2026
- Internal fairness validation: 1–14 September 2026
- External independent fairness audit: 15 September – 15 October 2026
- Redeployment (expanded POC resumption, with full monitoring operational): November 2026

**During remediation period:** All VRS calls continue through full human interpreter routing

---

## Week 6–8 (8–26 June 2026): Root Cause Analysis and Lessons Learned

- Formal root cause analysis document completed (see `root-cause-analysis.md`)
- AGPO produces full incident summary for AI Governance Committee (12 June)
- AI Governance Committee reviews root cause analysis and approves corrective action plan (19 June)
- Deaf Community Advisory Panel receives full incident summary including Panel's own detection role and the impact of their expanded scope recommendation (26 June)

---

## Ongoing: Data Collection and Retraining

- Supplemental training data collection in progress
- Monitoring framework demographic segmentation layer deployed in staging environment (June 2026). Will be operational before any POC resumption.
- Quarterly updates to AI Governance Committee throughout remediation period

---

## Incident Summary: Key Metrics

| Metric | Value |
|--------|-------|
| Detection to containment | 2 days |
| Detection method | Deaf Community Advisory Panel member report |
| Detection to full POC suspension | 2 days |
| Detection to regulatory notification (FCC) | 16 days |
| POC calls in lower luminance quartile (estimated) | 1,800–2,400 |
| Emergency calls affected | 0 (emergency routing to human interpreters was operational) |
| Monitoring gap identified | Demographic segmentation layer not operational at POC launch |
| Target: redeployment with full monitoring | November 2026 |
| Total estimated incident duration | ~6 months |

---

*This timeline is based on the SignalPath Interpret expanded