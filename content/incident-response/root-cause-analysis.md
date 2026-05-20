# Root Cause Analysis — SP-INC-2026-001

**Incident:** SP-AI-001 Skin Tone Accuracy Disparity
**RCA Status:** Final
**Prepared by:** AI Governance Program Office (AGPO) and ML Engineering
**Review Date:** 19 June 2026
**Approved by:** AI Governance Committee

---

## 1. Incident Summary

SignalPath Interpret (SP-AI-001) produced systematically lower confidence scores for signers with darker skin tones throughout an expanded proof-of-concept (POC) deployment lasting 52 days. The disparity originated in the computer vision pipeline's normalization algorithm, which was calibrated on a training dataset that did not adequately represent the demographic diversity of the Deaf community. The result was a materially worse AI interpretation experience for a segment of the Deaf user population the system is built to serve.

---

## 2. Root Cause Analysis Method

This analysis uses the Five Whys method to trace the incident to its root cause, followed by a contributing factors analysis to identify systemic conditions that allowed the failure to occur and persist. The goal is not to assign individual blame but to identify what must change so this class of failure cannot recur.

---

## 3. Five Whys Analysis

**Problem statement:** SignalPath Interpret produced confidence scores averaging 17 percentage points lower for signers in the lower skin tone luminance quartile, resulting in a 3.2x higher rate of automatic human interpreter handoff for those users throughout the expanded POC period.

---

**Why 1: Why did confidence scores drop for users with darker skin tones?**

Because the computer vision pipeline's normalization algorithm performed differently on darker skin, producing lower-quality feature inputs to the classification model. The algorithm was designed to standardize lighting across call environments. Its calibration assumed a training distribution skewed toward lighter skin tones, so its normalization behavior degraded quality for underrepresented skin tones rather than correcting for them.

---

**Why 2: Why was the normalization algorithm calibrated on a dataset skewed toward lighter skin tones?**

Because the training dataset was assembled without documented demographic composition requirements. Skin tone distribution was not recorded, not measured, and not audited as part of dataset intake. No minimum representation threshold existed for any demographic dimension of signer identity.

---

**Why 3: Why did no demographic representation requirement exist for the training dataset?**

Because the bias audit — which was a gate condition for expanded POC — was scoped to cover signer variation broadly (regional dialect, physical limitation, non-native ASL, oral Deaf users) but did not explicitly include skin tone normalization in the computer vision pipeline as a test dimension. The audit was commissioned and in progress, but the audit scope did not catch the specific failure mode that the incident exposed.

---

**Why 4: Why was skin tone normalization not included in the bias audit scope?**

Because the bias audit scope was defined without specific input from the Deaf Community Advisory Panel on which failure modes matter most to the community. The Panel was established as a gate condition and was active, but its input on audit scope was not formally solicited before the audit specification was finalized. The audit scope was defined by the AGPO and engineering team without community review.

---

**Why 5: Why did the gate conditions allow expanded POC to proceed with the bias audit incomplete and the audit scope unreviewed by the Panel?**

Because the gate conditions, as written, required that the bias audit be commissioned — not completed. The gate condition read: "Bias audit commissioned with independent auditor and scope defined." This allowed deployment to proceed while the audit that was supposed to catch this exact class of failure was still in progress. The gate condition was technically met while the risk it was designed to mitigate remained unaddressed.

**Root cause:** The gate condition for bias audit completion was insufficient. Allowing expanded POC deployment before a completed, Panel-reviewed bias audit placed Deaf users at risk from the exact failure mode the audit was designed to detect. The bias audit should have been a completion gate, not a commissioning gate, for any deployment involving real users.

---

## 4. Contributing Factors

### CF-1: Demographic Monitoring Not Operational at POC Launch

The monitoring framework was designed to include a demographic segmentation layer tracking confidence scores and accuracy by user demographic proxies. This layer was not configured before POC expansion — it was scheduled for post-launch setup. As a result, the automated monitoring system would not have detected the disparity even if it had been operating normally. The incident was detected by the Advisory Panel, not by monitoring.

**Implication:** Demographic monitoring is not an enhancement — it is a prerequisite. Any deployment involving real users must have demographic accuracy monitoring operational before the first call is processed.

---

### CF-2: Audit Scope Defined Without Deaf Community Advisory Panel Input

The bias audit scope was finalized by the AGPO and engineering team. The Deaf Community Advisory Panel was not consulted on which failure modes to prioritize, which demographic dimensions to test, or what constitutes an acceptable result. A Panel-reviewed audit scope would likely have included skin tone normalization as an explicit test dimension, given the well-documented challenges of computer vision systems with darker skin tones.

**Implication:** Audit scope for systems serving the Deaf community must include Deaf Community Advisory Panel review before the audit begins. Community input at the design stage of quality assurance is not a courtesy — it is the mechanism for catching failure modes that technical teams alone will not anticipate.

---

### CF-3: Skin Tone Normalization Is a Known Computer Vision Risk That Was Not Explicitly Tested

The failure of computer vision systems on darker skin tones is well-documented in the research literature and in publicized incidents involving facial recognition, medical imaging, and video analysis systems. This is not an unknown risk. It was not unknown to the team. It was not tested because the audit scope did not require it.

**Implication:** Governance frameworks for computer vision systems must include skin tone normalization as an explicit test requirement, documented as a named risk, not subsumed under general "bias audit" language.

---

### CF-4: Training Data Composition Was Not Documented

No demographic composition fields were recorded when the training dataset was assembled. There was no skin tone distribution, no signing dialect breakdown, no age range profile, no physical limitation representation count. The dataset was treated as a technical artifact, not as a governance artifact with demographic accountability.

**Implication:** Training datasets for systems serving the Deaf community are governance artifacts. Composition must be documented, audited, and reviewed before training begins. A dataset with unknown demographic composition cannot be certified as representative.

---

### CF-5: The Incident Exposed a Broader Representativeness Problem

The external fairness specialist and the Deaf Community Advisory Panel both identified that skin tone is one dimension of a broader training data representativeness gap. Preliminary analysis showed performance gaps — at lower magnitudes — for age-related signing variation and physical limitation variation as well. The skin tone disparity was the largest and most immediately detectable, but it is not the only one.

**Implication:** The remediation plan must address the full demographic scope of representativeness, not only the dimension that triggered the incident. Fixing skin tone while leaving other gaps unaddressed would be a partial remediation that still fails members of the Deaf community.

---

## 5. Corrective Action Plan

| Action | Contributing Factor Addressed | Owner | Due Date | Status |
|--------|------|-------|---------|--------|
| Redesign and recalibrate normalization algorithm on demographically balanced evaluation set | Root cause, CF-1, CF-3 | ML Engineering | 30 June 2026 | In progress |
| Commission supplemental training data collection across all underrepresented demographic dimensions | CF-4, CF-5 | Chief Product Officer + AGPO | 31 July 2026 | In progress |
| Define minimum representation thresholds per demographic dimension as a formal dataset intake requirement | CF-4 | AGPO + ML Engineering | 30 June 2026 | In progress |
| Require Deaf Community Advisory Panel review of bias audit scope before any audit begins | CF-2 | AGPO | 30 June 2026 | In progress |
| Deploy demographic accuracy monitoring (segmented by skin tone proxy, age, dialect variation) before any future POC or production deployment | CF-1 | ML Engineering + Engineering Lead | 30 September 2026 (before POC resumption) | Not started |
| Retrain SP-AI-001 on expanded, demographically documented dataset | Root cause, CF-4, CF-5 | ML Engineering | 31 August 2026 | Not started |
| Conduct independent fairness audit across all demographic dimensions before POC resumption | Root cause, CF-2, CF-3 | AGPO + external auditor | 15 October 2026 | Not started |
| Revise gate conditions: replace "bias audit commissioned" with "bias audit completed with Panel-reviewed scope" for all high-risk deployments involving real users | Root cause, CF-2 | AGPO | 30 June 2026 | In progress |
| Update AI Use Case Review process to require skin tone normalization testing as an explicit requirement for all computer vision systems | CF-3 | AGPO | 31 July 2026 | Not started |
| Provide full incident summary and corrective action plan to Deaf Community Advisory Panel | All | AGPO + Chief Product Officer | 26 June 2026 | Scheduled |

---

## 6. Lessons Learned

**For the AI governance program:**

1. **A commissioned audit is not a completed audit.** Gate conditions that allow deployment before an audit is finished are gate conditions that fail at exactly the moment they are supposed to protect users. Any gate condition involving a quality assurance activity should require completion, not initiation.

2. **Community input belongs at the design stage of quality assurance, not the review stage.** The Advisory Panel was established. The Panel was active. The Panel was not asked to review the audit scope before the audit was scoped. That sequencing produced an audit that missed the failure mode the community would have prioritized. Consultation is only useful if it happens before the decision, not after.

3. **Monitoring is not something you configure after deployment.** The demographic segmentation layer was planned but not operational. If it had been operational, this incident would have been detected within days, not 52 days. Monitoring readiness is a deployment gate, not a post-deployment task.

4. **The Deaf community is demographically diverse, and that diversity must be documented, not assumed.** Skin tone, age, physical variation, dialect, and language background are all dimensions where training data can fail. Each one must be explicitly documented, explicitly tested, and explicitly reported. "We ran a bias audit" is not a governance answer. "Our bias audit tested these specific dimensions against these specific thresholds and produced these specific results" is.

5. **The Advisory Panel worked.** The detection mechanism for this incident was a community member, not an automated system. That is both a validation of the governance structure and an indictment of the monitoring gap. Both things are true. The lesson is to close the monitoring gap — not to rely on community members to catch what the system should catch automatically.

6. **Proactive governance protects the community better than reactive governance.** The bias audit was designed to prevent this incident. The incident happened because the audit was incomplete when deployment began. Earlier completion, broader scope, and Panel-reviewed design would have caught this before any Deaf user experienced it.

---

*RCA approved by AI Governance Committee — 19 June 2026*
*Distribution: AI Governance Committee · Board Risk and Audit Committee · FCC (summary version) · Deaf Community Advisory Panel*
