# Incident Description — CreditScore Pro Postcode Bias

**Incident ID:** AI-INC-2026-001
**System:** NS-AI-001 · CreditScore Pro
**Incident Type:** AI Fairness / Discriminatory Output
**Severity:** 1 — Critical
**Status:** Under Investigation (as of Week 2)
**Incident Owner:** Head of Credit Risk
**Governance Lead:** AI Governance Programme Office

---

## Incident Summary

CreditScore Pro, NorthStar's ML-based credit scoring model, has been found to systematically assign lower credit scores to loan applicants residing in postcodes that correlate with high concentrations of ethnic minority residents in the Netherlands. The effect is statistically significant and cannot be explained by differences in financial history or creditworthiness indicators alone.

The disparity results in affected applicants facing higher rejection rates, higher interest rates, or lower loan limits than comparably creditworthy applicants from other postcodes. This constitutes potential indirect discrimination under EU anti-discrimination law and raises serious compliance concerns under the EU AI Act.

---

## How the Incident Was Detected

**Detection source:** Internal complaint — NorthStar data scientist

**Detection narrative:**

On 10 March 2026, a data scientist in the ML Engineering team was conducting exploratory analysis on the CreditScore Pro model as part of the new AI governance programme's bias audit initiative. She was examining feature importance and model outputs by geographic segment when she noticed an anomaly: applicants from a cluster of postcodes in Amsterdam (predominantly the Bijlmer district) and Rotterdam (Feijenoord district) were receiving scores 35–55 points lower on average than applicants with comparable financial profiles from other postcodes.

She flagged the finding to her manager, who escalated to the Head of Credit Risk on 11 March 2026.

Initial internal analysis confirmed the finding. The postcode cluster corresponds closely with areas that, according to CBS (Statistics Netherlands) data, have above-average concentrations of Surinamese, Turkish, and Moroccan-Dutch residents.

A preliminary assessment indicates that postcode is a significant feature in the model — it was included in training data as a "geographic risk factor" — and is acting as a proxy for ethnicity, producing indirect discrimination.

---

## Scope and Impact Assessment

**Estimated affected population (preliminary):**
- Approximately 2,400 loan applications processed in the affected postcodes in the 12 months preceding discovery
- Of those, approximately 680 resulted in rejection decisions
- Approximately 1,100 resulted in approval at higher interest rates or lower limits than a postcode-agnostic model would have produced

**Financial impact to affected customers (preliminary estimate):**
- Excess interest paid due to higher risk pricing: to be calculated
- Credit access denied: 680 applications — some proportion of which would likely have been approved under a fair model

**Regulatory implications:**
- EU AI Act Article 73: Serious incidents involving AI systems must be reported to national authorities. This incident may meet the definition of a "serious incident" (significant impairment of a person's right to non-discrimination)
- Dutch financial regulator (AFM): Obligation to report material conduct issues
- GDPR: Automated decision-making challenge rights under Article 22 may have been unlawfully denied if affected applicants were not informed their decisions were AI-assisted
- EU Equal Treatment in Access to Goods and Services Directive: Indirect discrimination in access to financial services

**Reputational risk:** High. Algorithmic discrimination in financial services is a high-profile regulatory and media issue. Proactive, transparent handling of this incident is essential.

---

## Immediate Context

**Why was postcode included in the model?**
Postcode was included as a geographic risk variable on the assumption that it reflected local economic conditions (unemployment rates, property values, local business health). This is a commonly used variable in credit risk modelling. However, in the Dutch context, postcode also encodes historical patterns of ethnic residential segregation, meaning it functions as an ethnicity proxy in practice.

**Was the risk known?**
The prior risk assessment (conducted informally at build time in 2022) did not include a formal analysis of proxy discrimination risk via geographic variables. The use of postcode was not questioned. This is a finding that the governance programme should address structurally.

**Is this ongoing?**
Yes. CreditScore Pro is processing applications in real time. Every application processed during the incident period may be affected. Immediate containment actions are required.

---

## Incident Severity Classification

| Dimension | Assessment |
|-----------|-----------|
| Harm to individuals | High — potential financial harm and discrimination against multiple protected groups |
| Regulatory exposure | Critical — multiple potential reporting obligations |
| Reputational risk | High |
| Operational impact | Medium — model suspension would require manual underwriting |
| Reversibility | Medium — past decisions can be reviewed and remediated; model can be retrained |

**Overall severity: 1 — Critical**

Severity 1 incidents require:
- Immediate notification to AI Governance Committee (within 24 hours)
- CRO notification within 24 hours
- Board Risk & Audit Committee notification within 48 hours
- Legal and Compliance immediate involvement
- Consideration of regulatory disclosure obligations

---

*This incident document was prepared by the AI Governance Programme Office on 12 March 2026. It is a living document updated as the investigation progresses.*
