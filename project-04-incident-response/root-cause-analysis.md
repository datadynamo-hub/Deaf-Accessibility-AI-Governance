# Root Cause Analysis — AI-INC-2026-001

**Incident:** CreditScore Pro Postcode Bias
**RCA Status:** Final
**Prepared by:** AI Governance Programme Office + ML Engineering
**Review Date:** 15 May 2026
**Approved by:** AI Governance Committee

---

## 1. Incident Summary

CreditScore Pro assigned systematically lower credit scores to applicants from postcodes correlating with ethnic minority populations in Amsterdam and Rotterdam, constituting indirect discrimination. The bias was present from model go-live (March 2022) and was active for approximately four years before detection.

---

## 2. Root Cause Analysis Method

This RCA uses the **5 Whys** method to trace the incident to its root causes, followed by a contributing factors analysis to capture systemic issues. The goal is not to assign individual blame but to identify the conditions that allowed the failure to occur and persist.

---

## 3. Five Whys Analysis

**Problem statement:** CreditScore Pro produced discriminatory credit scores for applicants from specific postcodes, resulting in higher rejection rates and inflated interest rates for protected groups.

---

**Why 1: Why did the model produce discriminatory scores?**

Because postcode was included as a feature and acted as a statistically significant proxy for ethnicity, depressing scores for applicants in historically ethnic-minority-concentrated areas.

---

**Why 2: Why was postcode included as a feature without recognising its discriminatory potential?**

Because the model development team conducted no formal proxy analysis of the features used. Postcode was treated as a legitimate geographic risk variable (reflecting local economic conditions) without analysis of whether it also encoded protected characteristics.

---

**Why 3: Why was no proxy analysis conducted?**

Because there was no requirement to do so. At the time of model development (2021–2022), NorthStar had no formal AI governance process, no fairness evaluation requirement, and no standard for pre-deployment bias assessment. The data science team followed standard credit risk modelling practice, which at the time did not include systematic fairness auditing.

---

**Why 4: Why was there no fairness evaluation requirement?**

Because NorthStar had no Responsible AI Policy or AI governance programme. The model was developed and deployed in the absence of any structured governance framework. There was no mechanism for identifying the need for fairness assessment or requiring it.

---

**Why 5: Why did the absence of a governance framework go unaddressed for four years?**

Because AI governance was not treated as a priority until regulatory pressure (the EU AI Act) created urgency. Before 2026, AI risk was managed informally within individual teams without cross-functional oversight, escalation paths, or executive accountability. There was no central inventory, no review process, and no monitoring framework that would have detected ongoing bias.

**Root cause:** Absence of an enterprise AI governance programme. The discriminatory model feature was a symptom; the root cause was the absence of the structures, processes, and accountability that would have prevented its inclusion, required its testing, and detected its effects.

---

## 4. Contributing Factors

### CF-1: Training Data Encoding Historical Discrimination

The model was trained on NorthStar's historical lending data (2015–2021). This data reflected lending decisions made before AI — and those decisions may themselves have been influenced by the geographic biases present in traditional credit assessment. Training on historically discriminatory outcomes can embed that discrimination into a model even without intent.

**Implication:** Retrospective datasets are not neutral. Governance frameworks must require assessment of whether training data encodes historical patterns that would be unacceptable if explicitly designed in.

---

### CF-2: Postcode as a Proxy — A Known Problem Ignored

The risk of using geographic variables as ethnicity proxies in credit models is a well-documented concern in academic literature, regulatory guidance (including FCA and ECB), and NGO reporting. The data science team was not aware of this literature and had not been trained to look for proxy discrimination risks.

**Implication:** ML practitioners need AI governance training that covers fairness concepts, not just technical skills. Governance is not just a policy function.

---

### CF-3: No Post-Deployment Monitoring for Bias

Once deployed, CreditScore Pro's performance was monitored for accuracy (default prediction accuracy, AUC) but not for fairness metrics. Demographic parity, equalised odds, and disparate impact measures were not tracked. The bias was therefore invisible to the operational monitoring regime.

**Implication:** Monitoring frameworks for AI systems must include fairness metrics, not just accuracy metrics.

---

### CF-4: No Mechanism for Affected Individuals to Surface Issues

Between 2022 and 2026, some applicants who were rejected may have suspected unfairness. But there was no accessible mechanism for affected applicants to raise a concern specifically about AI-driven decisions, and no requirement to inform applicants that an AI system was involved in their assessment. Their concerns, if any, entered the general complaints process without flagging as an AI fairness issue.

**Implication:** Customer-facing AI systems need accessible mechanisms for affected individuals to challenge AI-assisted decisions and a process for routing those challenges to people who can assess them.

---

### CF-5: Delayed Governance Programme Establishment

NorthStar's AI governance programme was established in January 2026 — triggered by the EU AI Act entering application for high-risk systems. Had the programme been established earlier (even in 2023, following broader industry signals), the bias audit that detected this incident would have occurred two to three years sooner. Approximately 2,500 fewer applications would have been affected.

**Implication:** Proactive governance, not compliance-driven governance, produces better outcomes. Waiting for regulation to require governance is not the same as managing risk.

---

## 5. Corrective Action Plan

| Action | Root Cause / Contributing Factor Addressed | Owner | Due Date | Status |
|--------|------|-------|---------|--------|
| Remove postcode feature and retrain CreditScore Pro | Direct remediation | ML Engineering | 30 April 2026 | Complete |
| Mandate pre-deployment proxy analysis for all geographic and demographic features in future models | CF-1, CF-2 | ML Engineering + AGPO | 30 June 2026 | In progress |
| Implement fairness metrics (demographic parity, disparate impact) in all credit model monitoring dashboards | CF-3 | ML Engineering | 30 June 2026 | In progress |
| Develop and deliver AI fairness training for all ML Engineering and data science staff | CF-2 | AGPO + HR | 31 July 2026 | Not started |
| Implement customer-facing AI disclosure and challenge mechanism for all credit decisions | CF-4 | Legal + Product + Customer Experience | 31 August 2026 | Not started |
| Update AUCR template and Enhanced Review criteria to mandate proxy analysis for any feature that could encode protected characteristics | Root cause | AGPO | 30 June 2026 | In progress |
| Conduct retrospective proxy analysis on all other production ML models (NS-AI-002, NS-AI-005) | CF-1, CF-3 | ML Engineering | 31 August 2026 | Not started |
| Include fairness monitoring requirements in standard vendor AI contract terms | CF-3 | Legal + Procurement | 31 July 2026 | Not started |

---

## 6. Lessons Learned

**For the AI governance programme:**

1. **Governance programmes must cover existing systems, not just new ones.** The AI governance programme was established in January 2026 but initially focused on new use cases going forward. This incident shows that the most significant governance gaps may be in systems already in production. A retrospective audit programme should be a standing element of the governance programme.

2. **Monitoring frameworks must include fairness metrics from day one.** Accuracy alone is not enough. Every AI system that affects individuals should have defined fairness metrics tracked alongside performance metrics.

3. **Proxy discrimination is not obvious.** Postcode seems like a legitimate variable. The discriminatory effect was not visible to the team that built the model. Governance frameworks must include explicit prompts to look for proxy effects — it is not enough to prohibit intentional discrimination.

4. **Speed of detection determines scale of harm.** This bias was active for four years. An earlier governance programme — or even periodic fairness monitoring — would have detected it sooner. The corrective action plan should prioritise building detection capability.

5. **Regulatory compliance and good governance are not the same thing.** The EU AI Act did not require a fairness audit of this model in 2022. A proactive governance approach would have. Governance programmes should aspire to better-than-minimum standards.

---

*RCA approved by AI Governance Committee — 15 May 2026*
*Distribution: AI Governance Committee · Board Risk & Audit Committee · AFM (summary version) · Internal audit*
