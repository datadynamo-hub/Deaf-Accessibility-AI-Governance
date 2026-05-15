# Deaf-Accessibility-AI-Governance

**3 Practical Projects Demonstrating Operational AI Governance in the Deaf Accessibility Space**

> \*"Reading the EU AI Act is not a project. These are."\*

\---

This repository applies Taimur Ijlal's open-source AI governance scaffolding to a domain where the stakes are real and the right questions are not being asked: AI deployment in Deaf accessibility services.

Full credit to Taimur Ijlal ([taimurijlal/AIGovernance](https://github.com/taimurijlal/AIGovernance)) for the wireframe. This build remaps his variables to a fictional but realistic Video Relay Service company called SignalPath Technologies. The scaffolding is his. The context, the risk framing, and the community are mine.

Built publicly. Feedback welcome. Fork it and map it to your industry or build with me.

\---

## The Scenario

**Organization:** SignalPath Technologies, a leading language services and accessibility technology provider serving Deaf, hard-of-hearing, and diverse language communities. 10,000+ employees. Operations across the United States, Canada, and the United Kingdom. Regulated by the FCC under Part 64 (Video Relay Service obligations), ADA Title IV, GDPR for EU-adjacent operations, and CCPA.

**The problem this repo addresses:** AI is being built to interpret for Deaf people in real time. Phone calls, medical appointments, legal situations. The people making those decisions are sitting in boardrooms where not a single Deaf person has a seat at the table. This repository asks what governance should look like before someone gets hurt.

\---

## Repository Structure

```
.
├── project-01-ai-system-inventory/     # Inventory and EU AI Act classification
├── project-02-risk-assessment/         # Structured risk assessment and governance memo
├── project-03-responsible-ai-policy/   # Policy, principles, and operating model
└── README.md                           # This file
```

\---

## The Three Projects

|#|Project|Primary Framework|Key Artefact|
|-|-|-|-|
|1|[AI System Inventory](./project-01-ai-system-inventory/)|EU AI Act, NIST AI RMF|Inventory + classification rationale|
|2|[AI Risk Assessment and Governance Review Pack](./project-02-risk-assessment/)|NIST AI RMF (Map, Measure)|Risk matrix + executive memo|
|3|[Responsible AI Policy and Operating Model](./project-03-responsible-ai-policy/)|NIST AI RMF (Govern)|Policy document + process diagram|

\---

## How to Use This Repository

Each project folder contains:

* **`README.md`** — scenario context, objectives, and how artifacts connect to frameworks
* **Artifacts** — the actual governance documents: inventories, assessments, policies, memos

Read them in order if you are new to AI governance. Each project builds on the one before it. Navigate directly to the most relevant project if you are preparing for a specific role or interview.

To use this as a starting point for your own build: fork the repo, swap the company context, and map the variables to an industry you know. 

\---

## Framework Quick Reference

### EU AI Act — Risk Tiers

|Tier|Description|Examples|
|-|-|-|
|Unacceptable|Prohibited outright|Social scoring, real-time biometric surveillance|
|High-Risk|Strict obligations|Recruitment, credit, critical infrastructure, biometric processing|
|Limited Risk|Transparency obligations|Chatbots, AI-generated content|
|Minimal Risk|No specific obligations|Spam filters, recommendation engines|

### NIST AI RMF — Core Functions

|Function|Purpose|
|-|-|
|**GOVERN**|Establish accountability structures, policies, and culture|
|**MAP**|Identify and categorize AI risks in context|
|**MEASURE**|Analyze and assess AI risks quantitatively and qualitatively|
|**MANAGE**|Prioritise and treat risks; respond to incidents|

\---

## Why the EU AI Act as the Standard for a US Company

The United States has no federal AI Act equivalent. Most of the industry is in wait-and-see mode. SignalPath applies the EU AI Act as its ethical benchmark for four reasons: EU-facing operations create real regulatory surface area, GDPR biometric data obligations apply to sign language processing, building to the strictest available standard protects the community SignalPath serves regardless of where jurisdiction lines fall, and Deaf people travel.

That last point matters more than most compliance teams realize. A Deaf American using a US-based VRS product while traveling in the EU is operating in a legal grey area. The product may not be built to EU standards. The data collected during that call may not meet GDPR requirements. The company may have no idea this is happening. That is not a hypothetical edge case. It is compliance being broken accidentally, at scale, every time a Deaf traveler picks up their phone abroad.

The EU AI Act is the highest standard currently available. This build treats it as the floor and builds upward from there.

\---

## About

Scaffolding: [Taimur Ijlal](https://github.com/taimurijlal) — The Cloud Security Guy. Original repo: [taimurijlal/AIGovernance](https://github.com/taimurijlal/AIGovernance).

This build: Jonathan Khan, Data Infrastructure and AI Governance Professional. Deaf community member. Building publicly because the right questions deserve public answers, not private ones.

Follow the build on LinkedIn: [Jonathan Khan](https://www.linkedin.com/in/jonathan-k-184393120/)

