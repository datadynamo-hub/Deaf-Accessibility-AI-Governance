# Project 3: Responsible AI Policy and Governance Operating Model

## Scenario

**Organization:** SignalPath Technologies
**Context:** Following the AI system inventory in Project 1 and the risk assessment and governance memo in Project 2, SignalPath's Board has approved the establishment of a formal AI governance program. The AI Governance Program Office has been asked to develop two foundational documents: a Responsible AI Policy and a Governance Operating Model.

The policy defines what SignalPath believes and commits to. The operating model defines how those commitments are made real.

This is where principles stop being decoration. If the governance work done in Projects 1 and 2 surfaces risks but nothing changes how decisions get made, the company is not governing AI. It is documenting it. There is a difference.

---

## What This Project Demonstrates

- Understanding that responsible AI principles must translate into process, not just statements
- Ability to design a governance operating structure: committees, roles, accountability lines, escalation paths
- Knowledge of how the NIST AI RMF Govern function works in practice, not just on paper
- Understanding of the AI lifecycle from use case submission through production monitoring
- Ability to connect legal, risk, engineering, product, and community stakeholders in a governance structure that can actually hold
- Recognition that governance in a VRS and accessibility technology context carries obligations that do not exist in generic enterprise AI contexts

---

## Artifacts

| File | Description |
|------|-------------|
| [`responsible-ai-policy.md`](./responsible-ai-policy.md) | Full Responsible AI Policy for SignalPath Technologies |
| [`ai-review-process.md`](./ai-review-process.md) | AI use case submission, review, and approval workflow |
| [`governance-operating-model.md`](./governance-operating-model.md) | Operating model narrative and role descriptions |

---

## Design Principles for This Project

**Principles without process are decoration.** Many organizations publish AI principles that look good on a website and do not change a single decision or workflow. Every principle in this policy has a corresponding process that makes it operational.

**Governance is not a bottleneck.** The review process is proportionate. Minimal-risk systems get lightweight review. High-risk systems, particularly those processing biometric data from Deaf users in real-time relay of legally protected communications, get rigorous review with mandatory gate conditions. The goal is appropriate oversight, not maximum friction.

**Structure reflects a real organization.** SignalPath is a mid-size VRS and accessibility technology company regulated by the FCC under Part 64, operating under ADA Title IV obligations, with EU-adjacent GDPR surface area from international users and the UK operations footprint. The governance structure is designed for this specific regulatory and community context, not for a generic enterprise. It uses roles and committees that already exist at a company of this size and re-purposes them for AI oversight.

**The Deaf community is not a footnote.** Governance decisions about AI systems that interpret ASL, route relay calls, and caption live speech directly affect the lives of Deaf users who depend on SignalPath for communication access to emergency services, medical care, and legal proceedings. A governance structure that excludes Deaf community input in favor of purely internal deliberation is not governing the risk. It is managing the perception of risk. These are different things.

**The ASL plain-language requirement is a first-class obligation, not a communications add-on.** Every policy that governs how SignalPath builds or deploys AI systems must be translatable into plain English accessible to lay audiences. Key policies must have an ASL summary available. If a governance policy cannot be explained to a Deaf user in their primary language, that is a signal the policy may not be understood well enough to be enforced.

---

## Key Design Decisions

**Why the Deaf Community Advisory Panel is a named governance role, not an optional advisory group**

Project 2 documented the risk of designing AI systems for the Deaf community without Deaf representation in the governance structure. That risk does not disappear in Project 3. The operating model names the Deaf Community Advisory Panel as a structural participant in governance with documented influence on design decisions, not a consultative body that can be skipped when the timeline is tight.

**Why EU AI Act deployer obligations are treated as relevant even though SignalPath is primarily a provider**

SignalPath builds and deploys AI systems for use by its own end users. For core product AI, SignalPath occupies both provider and deployer roles simultaneously. Articles 9, 14, and 13 of the EU AI Act apply to how SignalPath operates SignalPath Interpret (SP-AI-001) in production. Articles 28 and 29 are also referenced for the enterprise-embedded AI systems where SignalPath is the deploying organization. The README source from which this project is adapted cited Articles 28-29 as deployer obligations: they apply here specifically to SignalPath's use of third-party AI systems including Workday AI (SP-AI-006, high-risk) and Microsoft Copilot M365 (SP-AI-005). This distinction is preserved explicitly because collapsing provider and deployer roles creates compliance gaps that regulators will find.

**Why the review process uses tiered intake, not a single universal gate**

Sixteen AI systems are in the SignalPath inventory, spanning four risk tiers from minimal to unclassifiable. A single universal review gate would create a bottleneck that incentivizes teams to route around governance. A tiered intake process routes systems to the appropriate level of review, reserves the full governance committee for high-risk decisions, and reduces friction for low-risk deployments without reducing oversight where it matters.

---

## Frameworks Applied

- **NIST AI RMF:** Govern function: accountability, culture, policies, roles, and organizational context
- **EU AI Act:** Article 9 (risk management system), Article 13 (transparency obligations), Article 14 (human oversight), Articles 28-29 (deployer obligations for enterprise-embedded AI)
- **OECD AI Principles:** Human-centered values, transparency, accountability
- **ISO/IEC 42001:** AI management system requirements for structure and policy alignment
- **FCC Part 64:** VRS service reliability obligations and the functional equivalency standard
- **ADA Title IV:** Telecommunications accessibility obligations for relay service providers

---

> **REVIEW FLAG:** The governance operating model diagram is described narratively in `governance-operating-model.md`. A visual diagram is a separate deliverable not produced in this file. Before this project goes into a Loom walkthrough, the diagram should be built and reviewed for accuracy against the role descriptions in the operating model document.

> **REVIEW FLAG:** Accuracy benchmarks and monitoring thresholds for SignalPath Interpret (SP-AI-001) are referenced in the policy's monitoring section. These thresholds need a dedicated review against real VRS operational context before any public presentation. Industry insiders will scrutinize them. Do not present specific numbers without verification.
