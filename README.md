# SignalPath AI Governance Center

**Production-grade AI governance for a fictional Deaf accessibility company — built as a portfolio demonstrating what governance looks like when the stakes are real.**

> *"Reading the EU AI Act is not a project. These are."*

---

Built on top of Taimur Ijlal's open-source AI governance scaffolding ([taimurijlal/AIGovernance](https://github.com/taimurijlal/AIGovernance)). His wireframe, remapped entirely to a Video Relay Service context where AI governs real-time interpretation for Deaf people on phone calls, medical appointments, and emergency situations.

---

### 📺 Watch the Project Introduction (8 mins)

*Introduces the project goals and the remapping from Taimur's original scaffolding to the SignalPath context.*

<p align="center">
<img width="616" height="341" alt="Screenshot 2026-05-18 230148" src="https://github.com/user-attachments/assets/d5cbb04b-4a8d-44f9-b91d-e076ea827bd4" />
</p>

---

## The Scenario

**Organization:** SignalPath Technologies — a language services and accessibility technology provider serving Deaf, hard-of-hearing, and diverse language communities. 10,000+ employees. Operations across the United States, Canada, and the United Kingdom. Regulated by the FCC under Part 64 (Video Relay Service functional equivalency obligations), ADA Title IV, and GDPR for EU-adjacent operations.

**The system at the center of this build:** SP-AI-001 SignalPath Interpret — a real-time ASL interpretation AI deployed in a limited pilot as an overlay to human interpreter capacity. Not replacing interpreters. Augmenting them, with a mandatory human handoff at any confidence threshold below 0.85, and mandatory human routing for all emergency relay calls.

**The governance question this repo answers:** What does responsible AI deployment actually look like when the people your model serves cannot simply opt out of needing it?

---

## The Application

Five sections. Each one is a production artifact, not a homework exercise.

| Section | What It Contains |
|---------|-----------------|
| **Command Center** | Live operational dashboard — active incidents, system health, governance alerts |
| **AI System Registry** | Full inventory of 16 SignalPath AI systems with EU AI Act risk classification and NIST AI RMF mapping |
| **Risk Intelligence** | Structured risk assessment for SP-AI-001 with an interactive 5×5 risk matrix, inherent vs. residual toggle, and executive governance memo |
| **Incident Response** | SP-INC-2026-001 — a real bias incident during the SP-AI-001 POC, with 7-phase response walkthrough, timeline, and root cause analysis |
| **Governance Documentation Hub** | Responsible AI Policy, Governance Operating Model, AI Review Process, EU AI Act Classification rationale, NIST RMF Mapping, and EU AI Act Conformity Pack (in progress) |

---

## Repository Structure

```
.
├── app.py                          # Streamlit application (934 lines)
├── data/
│   └── ai-system-inventory.xlsx    # 16-system inventory, 17 columns
├── content/
│   ├── policy/                     # Responsible AI Policy, Governance Operating Model,
│   │                               #   AI Review Process, EU AI Act Classification,
│   │                               #   NIST RMF Mapping
│   ├── risk-assessment/            # SP-AI-001 risk register, governance review memo
│   ├── incident-response/          # SP-INC-2026-001 scenario, timeline, root cause analysis
│   └── conformity-pack/            # EU AI Act conformity documents — Articles 9–17
│                                   #   (Project 5, in progress)
└── requirements.txt
```

---

## Framework Coverage

### EU AI Act — Risk Tiers

| Tier | Description | Examples |
|------|-------------|---------|
| Unacceptable | Prohibited outright | Social scoring, real-time biometric surveillance in public spaces |
| **High Risk** | Strict conformity obligations | **SP-AI-001** — biometric processing, essential communications service for protected population |
| Limited Risk | Transparency obligations | Chatbots, AI-generated content |
| Minimal Risk | No specific obligations | Spam filters, recommendation engines |

### NIST AI RMF — Core Functions

| Function | Purpose |
|----------|---------|
| **GOVERN** | Establish accountability structures, policies, and culture |
| **MAP** | Identify and categorize AI risks in context |
| **MEASURE** | Analyze and assess AI risks quantitatively and qualitatively |
| **MANAGE** | Prioritize and treat risks; respond to incidents |

---

## Why the EU AI Act as the Standard for a US Company

The United States has no federal AI Act equivalent. Most of the industry is in wait-and-see mode. SignalPath applies the EU AI Act as its governance benchmark for reasons that are not abstract.

EU AI Act Article 2(1)(c) applies to AI systems whose outputs are used in the Union — the question is not where the server is, but where the output is consumed. GDPR Article 9 applies to biometric data processing with no headquarters exception. SP-AI-001 processes hand shape, facial expression, and body position — biometric data under GDPR Article 4(14). And Deaf people travel.

A Deaf American using a US-based VRS product while in Paris is in EU jurisdiction when that call is processed. The product may not be built to EU standards. The data collected during that call may not meet GDPR requirements. The company may have no idea this is happening. That is not a hypothetical edge case. It is compliance being broken accidentally, at scale, every time a Deaf traveler picks up their phone abroad.

The EU AI Act is the highest standard currently available. This build treats it as the floor, with US federal (FCC Part 64, ADA Title IV) and US state (Illinois BIPA, California CPRA) obligations documented alongside it. Governance that only works in one jurisdiction is not governance.

---

## About

Scaffolding: [Taimur Ijlal](https://github.com/taimurijlal) — The Cloud Security Guy. Original repo: [taimurijlal/AIGovernance](https://github.com/taimurijlal/AIGovernance).

This build: Jonathan Khan, Data Infrastructure and AI Governance Professional. Deaf community member. Building publicly because the right questions deserve public answers.

Follow the build on LinkedIn: [Jonathan Khan](https://www.linkedin.com/in/jonathan-k-184393120/)
