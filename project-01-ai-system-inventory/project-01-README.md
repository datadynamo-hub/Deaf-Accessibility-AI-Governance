Project 1: AI System Inventory
 
**Organization:** SignalPath Technologies (fictional): one of the world's leading language services and accessibility technology providers, serving Deaf, hard-of-hearing, and diverse language communities. 10,000+ employees worldwide. Operations across the United States, Canada, the United Kingdom, and a global enterprise customer base. Regulated by the FCC under Part 64 (Video Relay Service obligations), GDPR for EU-adjacent operations, ADA Title IV, and CCPA.


**Problem:** SignalPath's Chief Risk Officer has initiated an AI governance program following the accelerated deployment of AI-assisted interpretation, captioning, and call routing technology across multiple business units. A preliminary internal survey revealed that AI systems have been deployed across product lines without central oversight or classification. The organization does not have a single authoritative inventory of its AI systems.


**Objective:** Produce a structured AI system inventory and apply EU AI Act risk classification to each identified system. Map each system to the NIST AI RMF to identify governance gaps.

\---

## What This Project Demonstrates

* Understanding of **proportionality** not all AI systems carry the same obligations
* Ability to apply the **EU AI Act's risk-based classification logic** to realistic VRS and accessibility technology systems
* Practical knowledge of the **NIST AI RMF's four functions** as an operational lens
* Capacity to structure governance data in a format usable by risk, legal, and engineering teams

\---

## Artifacts

|File|Description|
|-|-|
|[`ai-system-inventory.csv`](./ai-system-inventory.csv)|Structured inventory of SignalPath's AI systems|
|[`eu-ai-act-classification.md`](./eu-ai-act-classification.md)|Classification rationale for each system under the EU AI Act|
|[`nist-rmf-mapping.md`](./nist-rmf-mapping.md)|Mapping of each system to NIST AI RMF functions and gap analysis|

\---

## Key Decisions \& Rationale

**Why a CSV for the inventory?**
A structured data format (rather than a narrative document) makes the inventory queryable, sortable, and importable into GRC tooling. In practice, this would live in a system of record — the CSV approximates that structure.

**Why classify before full assessment?**
Classification determines the *level of due diligence* required. It is a triage step. High-risk classification triggers the deeper obligations in Projects 2 and 3. This mirrors real governance workflows, where classification gates further review.

**Why apply the EU AI Act as the classification standard for a US-based company?**
The United States currently has no federal AI Act equivalent. Most of the industry is in wait-and-see mode. SignalPath applies the EU AI Act as its ethical benchmark. EU-facing operations, GDPR biometric data obligations, and the presence of traveling US Deaf users accessing SignalPath services from EU countries all create real regulatory surface area. Building to the strictest available standard protects the community SignalPath serves.

**Fictional company, real logic**
SignalPath is fictional, but every system in the inventory reflects a genuine AI use case present in VRS and accessibility technology today. The classification rationale cites specific articles and annexes from the EU AI Act and cross-references FCC Part 64 service obligations where applicable.

\---

## Frameworks Applied

* **EU AI Act** — Articles 5, 6, and Annex III (high-risk system categories)
* **NIST AI RMF** — Govern, Map, Measure, Manage functions
* **FCC Part 64** — VRS service reliability and accessibility obligations
* **GDPR** — Biometric data processing restrictions for EU-adjacent operations
* **ISO/IEC 42001** — AI management system context (referenced in gap notes)
* **ADA Title IV** — Telecommunications accessibility obligations

\---

> ⚠️ \*\*REVIEW FLAG:\*\* AI system variables (SignalPath Interpret accuracy benchmarks, call routing ML specifics, CSAT scoring methodology, fraud detection thresholds) need a dedicated 2-3 hour deep-dive against real VRS operational context before this is video-ready. Industry insiders will scrutinize these. Verify before publishing.

