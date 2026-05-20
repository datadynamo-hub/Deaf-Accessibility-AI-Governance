# Incident Description — SP-AI-001 Skin Tone Accuracy Disparity

**Incident ID:** SP-INC-2026-001
**System:** SP-AI-001 · SignalPath Interpret
**Incident Type:** AI Fairness / Discriminatory Output — Skin Tone-Correlated Confidence Disparity
**Severity:** 1 — Critical
**Status:** Under Investigation (as of Week 2)
**Incident Owner:** Chief Product Officer
**Governance Lead:** AI Governance Program Office (AGPO)

---

## Incident Summary

SignalPath Interpret (SP-AI-001), operating in an expanded proof-of-concept (POC) deployment across SignalPath's Video Relay Service (VRS) operations, has been found to produce systematically lower confidence scores for signers with darker skin tones. The disparity is statistically significant and is not explained by differences in signing fluency, vocabulary, or call quality indicators.

Lower confidence scores result in more frequent interpretation errors and higher rates of automatic human interpreter handoff. In practice, this means that Deaf users with darker skin tones receive a materially degraded AI interpretation experience compared to users with lighter skin tones — a discriminatory service outcome affecting a protected population.

The root cause is located in the computer vision pipeline's skin tone normalization algorithm, which was calibrated on a training dataset skewed toward lighter skin tones. This is a known failure mode in computer vision systems and represents a training data composition problem, not an isolated technical defect.

---

## How the Incident Was Detected

**Detection source:** Deaf Community Advisory Panel member report

**Detection narrative:**

On 4 May 2026, a member of the Deaf Community Advisory Panel submitted a written report to the AGPO. The panel member, who is an active VRS user and has been participating in the expanded POC, noted that she and several members of her network had been experiencing more frequent interpretation errors than other POC participants she was in contact with. The errors were described as the AI interpreter producing incorrect signs or triggering interpreter handoff during calls that the users felt were proceeding clearly.

The AGPO triaged the report on 5 May 2026. Engineering pulled confidence score logs for the affected users and conducted an initial analysis on 6 May 2026.

**Initial engineering findings:**

Confidence scores were segmented by a proxy measure of skin tone: relative luminance values extracted from video frame samples during calls. The analysis found a statistically significant correlation between lower luminance values (darker skin tones) and reduced model confidence scores. Users in the lower luminance quartile showed average confidence scores 17 percentage points below users in the upper luminance quartile, controlling for call duration, vocabulary range, and network quality indicators.

At SignalPath Interpret's Lower Control Limit (LCL) threshold of 75%, users in the lower luminance quartile were triggering automatic human interpreter handoff at a rate approximately 3.2 times higher than users in the upper quartile.

The AGPO classified the finding as Severity 1 on 6 May 2026 and initiated incident response.

---

## Why the Disparity Occurs

The computer vision pipeline in SignalPath Interpret extracts hand shape, finger configuration, movement, and position from video frames. Before feature extraction, the pipeline applies a lighting normalization algorithm to standardize image contrast across varying call environments.

The normalization algorithm was trained and calibrated on a dataset that did not include sufficient representation of darker skin tones. As a result:

- The algorithm's contrast normalization performs differently on darker skin, producing lower-quality feature inputs to the classification model
- The classification model — trained on the same demographically narrow dataset — has lower confidence when operating on the normalized outputs from darker-skin frames
- Lower confidence produces more interpretation errors and more frequent LCL threshold breaches

This is a training data composition problem at two levels: the normalization algorithm and the classification model. It cannot be resolved by a single parameter adjustment. It requires retraining on a dataset that adequately represents the demographic diversity of the Deaf community.

---

## Scope and Impact Assessment

**Deployment context:** SignalPath Interpret entered expanded POC on 14 March 2026, approximately 52 days before detection. Approximately 340 calls per day are processed through the system across the POC participant group.

**Estimated affected population (preliminary):**
- POC participants in the lower skin tone luminance quartile: approximately 28% of the active participant pool, based on engineering's luminance analysis
- Estimated calls affected since POC expansion: to be quantified during investigation

**Service impact to affected users:**
- Elevated interpretation error rates throughout the POC period
- Higher handoff rates to human interpreters — the fallback worked as designed, but the AI interpretation experience was materially worse for these users
- No evidence of failed emergency calls in the POC period — emergency calls route to human interpreters by design, per the gate conditions established before POC expansion

**Regulatory implications:**
- **ADA Title IV / FCC Part 64:** The functional equivalency standard requires that VRS provide access substantially equivalent to voice telephone service for hearing users. A system that systematically delivers lower-quality service to Deaf users with darker skin tones does not meet functional equivalency.
- **EU AI Act Article 73:** If SignalPath Interpret is within EU AI Act scope for any affected user — including Deaf travelers accessing VRS from EU countries — this may constitute a serious incident requiring notification to the relevant national authority.
- **GDPR Article 9:** Biometric data processing resulting in discriminatory outputs creates additional compliance exposure for affected users with EU data subject rights.
- **Illinois Biometric Information Privacy Act (BIPA):** If any affected POC participants are Illinois residents, BIPA violations related to biometric data processing compound the regulatory exposure.

**Reputational risk:** Critical. SignalPath's core market is the Deaf community. A discriminatory AI system disproportionately failing users with darker skin tones — discovered during an internal POC — must be handled with full transparency and proactive remediation. The Deaf community is closely networked. The Advisory Panel member's report reflects exactly the kind of trust relationship that governance structures are designed to maintain.

---

## Immediate Context

**Why did the training data skew toward lighter skin tones?**
The training dataset provenance documentation was incomplete. Skin tone distribution was not recorded as part of the dataset composition documentation. No requirement to document or audit skin tone representation existed in the dataset intake process at the time the training data was assembled. This gap was identified as a control deficiency at the time of the original risk assessment but was treated as an audit action rather than a deployment gate condition.

**Was this risk known?**
Yes. The original risk assessment (RISK-001, May 2026) identified demographic bias in training data as a High risk with a likelihood score of 4. The bias audit was commissioned as a gate condition for expanded POC. The audit scope covered signer variation, regional dialect, physical limitation, non-native ASL, and oral Deaf users — but skin tone normalization in the computer vision pipeline was not explicitly scoped as a test dimension. This was an audit design gap, not a concealment.

**Is this ongoing?**
Yes. SignalPath Interpret is processing VRS calls in expanded POC as of the incident detection date. Affected users are continuing to experience the disparity. Immediate containment decisions are required.

---

## Incident Severity Classification

| Dimension | Assessment |
|-----------|-----------|
| Harm to affected users | High — systematic interpretation degradation for a protected group throughout POC period |
| Regulatory exposure | Critical — FCC functional equivalency, potential EU AI Act serious incident, BIPA risk |
| Reputational risk | Critical — Deaf community trust is the foundation of SignalPath's market position |
| Operational impact | Medium — human interpreter fallback has been functioning; no catastrophic service failure |
| Reversibility | Medium — affected calls cannot be retroactively corrected; model retraining is achievable with timeline |

**Overall severity: 1 — Critical**

Severity 1 incidents require:
- Immediate notification to AI Governance Committee (within 24 hours)
- Chief Risk Officer notification within 24 hours
- Board Risk and Audit Committee notification within 48 hours
- Legal and General Counsel immediate involvement
- Assessment of regulatory disclosure obligations (FCC, EU AI Act Article 73)

---

## Immediate Governance Note

The detection mechanism for this incident was the Deaf Community Advisory Panel — not the automated monitoring system. The demographic segmentation layer of the monitoring framework was not fully operational at the time of POC expansion. This is a control gap that must be addressed as part of the corrective action plan: demographic accuracy monitoring must be operational before any further deployment expansion, not configured post-incident.

The Advisory Panel worked exactly as designed. This is the governance structure functioning. The lesson is not that the Panel saved us from a monitoring failure — it is that the monitoring should have caught this first.

---

*This incident document was prepared by the AI Governance Program Office on 7 May 2026. It is a living document updated as the investigation progresses.*
