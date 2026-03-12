# Project 1: AI System Inventory & Classification Engine

## Scenario

**Organisation:** NorthStar Financial Services — a mid-sized fintech operating across retail banking, lending, and insurance verticals. Approximately 1,400 employees. Regulated in the EU.

**Problem:** NorthStar's Chief Risk Officer has initiated an AI governance programme following the EU AI Act entering application. A preliminary internal survey revealed that AI systems have been deployed across multiple business units without central oversight or classification. The organisation does not have a single authoritative inventory of its AI systems.

**Objective:** Produce a structured AI system inventory and apply EU AI Act risk classification to each identified system. Map each system to the NIST AI RMF to identify governance gaps.

---

## What This Project Demonstrates

- Understanding of **proportionality** — not all AI systems carry the same obligations
- Ability to apply the **EU AI Act's risk-based classification logic** to realistic systems
- Practical knowledge of the **NIST AI RMF's four functions** as an operational lens
- Capacity to structure governance data in a format usable by risk, legal, and engineering teams

---

## Artefacts

| File | Description |
|------|-------------|
| [`ai-system-inventory.csv`](./ai-system-inventory.csv) | Structured inventory of NorthStar's AI systems |
| [`eu-ai-act-classification.md`](./eu-ai-act-classification.md) | Classification rationale for each system under the EU AI Act |
| [`nist-rmf-mapping.md`](./nist-rmf-mapping.md) | Mapping of each system to NIST AI RMF functions and gap analysis |

---

## Key Decisions & Rationale

**Why a CSV for the inventory?**
A structured data format (rather than a narrative document) makes the inventory queryable, sortable, and importable into GRC tooling. In practice, this would live in a system of record — the CSV approximates that structure.

**Why classify before full assessment?**
Classification determines the *level of due diligence* required. It is a triage step. High-risk classification triggers the deeper obligations in Projects 2 and 5. This mirrors real governance workflows, where classification gates further review.

**Fictional company, real logic**
NorthStar is fictional, but every system in the inventory reflects a genuine AI use case present in financial services today. The classification rationale cites specific articles and annexes from the EU AI Act.

---

## Frameworks Applied

- **EU AI Act** — Articles 5, 6, and Annex III (high-risk system categories)
- **NIST AI RMF** — Govern, Map, Measure, Manage functions
- **ISO/IEC 42001** — AI management system context (referenced in gap notes)
