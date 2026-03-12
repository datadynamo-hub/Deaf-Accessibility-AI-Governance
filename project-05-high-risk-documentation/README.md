# Project 5: High-Risk AI Documentation & Conformity Pack

## Scenario

**Organisation:** NorthStar Financial Services
**System:** HireAssist Pro — AI-assisted hiring decisions system (replacing TalentMatch AI following the governance remediation in Projects 2 and 3)

Following the governance review of TalentMatch AI, NorthStar has decided to procure a new AI recruitment solution and build it out with proper governance from the start. Before the new system can go live, the AI Governance Programme Office must compile the documentation required for a high-risk AI system under the EU AI Act.

This project simulates that documentation pack.

---

## What This Project Demonstrates

- Detailed knowledge of **EU AI Act Article 9–17** obligations for high-risk AI providers and deployers
- Understanding of what **EU AI Act Annex IV** requires in technical documentation
- Ability to structure compliance documentation in a **defensible, auditable** format
- Practical knowledge of what **regulators and auditors look for** in AI conformity documentation
- Understanding that documentation is not bureaucracy — it is the evidence that governance is real

---

## Artefacts

| File | Description |
|------|-------------|
| [`01-intended-purpose.md`](./01-intended-purpose.md) | System description and statement of intended purpose |
| [`02-risk-management-summary.md`](./02-risk-management-summary.md) | Risk management approach and residual risk position |
| [`03-data-governance.md`](./03-data-governance.md) | Training data, validation data, and data governance practices |
| [`04-human-oversight.md`](./04-human-oversight.md) | Human oversight mechanisms and procedures |
| [`05-logging-traceability.md`](./05-logging-traceability.md) | Logging design and traceability approach |
| [`06-performance-monitoring.md`](./06-performance-monitoring.md) | Post-deployment monitoring and performance management plan |

---

## EU AI Act Article Mapping

| Artefact | Primary EU AI Act Articles |
|----------|--------------------------|
| Intended purpose | Art. 9(2)(a), Art. 11, Annex IV §1 |
| Risk management | Art. 9 (risk management system) |
| Data governance | Art. 10 (data and data governance) |
| Human oversight | Art. 14 (human oversight) |
| Logging and traceability | Art. 12 (record-keeping) |
| Performance monitoring | Art. 15 (accuracy, robustness), Art. 17 (post-market monitoring) |

---

## A Note on Scope

The EU AI Act places primary documentation obligations on AI **providers** (those who develop or place AI systems on the market). NorthStar is a **deployer** — it uses a system developed by a vendor (HireFlow Technologies Ltd, updated version).

However, deployers of high-risk AI systems have significant obligations under Articles 28–29, including:
- Ensuring the system is used in accordance with the instructions of use
- Ensuring required human oversight is in place
- Monitoring system performance in the deployed context
- Reporting serious incidents

This documentation pack covers **both** the provider documentation that NorthStar must obtain from HireFlow, and the deployer documentation that NorthStar must produce itself. Both are included and clearly labelled.

---

## Frameworks Applied

- **EU AI Act** — Articles 9–17, 28–29, Annex IV
- **NIST AI RMF** — Govern function (documentation and accountability)
- **ISO/IEC 42001** — AI management system documentation requirements
