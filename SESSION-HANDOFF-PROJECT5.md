# SignalPath AI Governance — Project 5 Handoff
# EU AI Act Conformity Pack: SP-AI-001 SignalPath Interpret
*Created: 2026-05-19 | Verification password: BlueOstrich42*

---

## PASTE THIS INTO THE NEW CHAT TO RESUME

> I'm continuing the SignalPath AI Governance Center build. This handoff covers Project 5: the EU AI Act Conformity Pack for SP-AI-001 (SignalPath Interpret). This is a research-heavy, accuracy-critical deliverable. The verification password is **BlueOstrich42**. Read this file fully before doing anything. DO NOT write any document content until we align on the research and fact-checking plan.

---

## 1. What Project 5 Is

Six EU AI Act conformity documents covering SP-AI-001 (SignalPath Interpret), the real-time ASL interpretation AI. Each document maps to a specific article of the EU AI Act. These documents form the "EU AI Act Conformity Pack" tab inside the Governance Documentation Hub section of the Streamlit app.

**Why this matters for the portfolio:** These documents demonstrate Article 9–17 knowledge at the working level — not just awareness of the law, but the ability to produce the actual compliance artifacts that a deployer of a High Risk AI system would need. This is hire-worthy at companies building or deploying AI in any regulated or sensitive context.

**Why this is high-stakes:** Every legal citation must be verified. Every claim about what an article requires must be sourced against the actual text. This is the one section of the portfolio where a technically sophisticated interviewer — particularly one with EU AI Act, GDPR, or US privacy law background — will probe specific claims.

---

## 2. The Six Documents

| # | Filename | EU AI Act Reference | What It Covers |
|---|---------|--------------------|-----------------|
| 01 | `01-intended-purpose.md` | Article 11, Annex IV §1–2 | System identification, intended purpose, prohibited uses, known limitations, classification basis |
| 02 | `02-risk-management.md` | Article 9 | Risk management system, identified risks, pre-deployment evaluations, foreseeable misuse, residual risk |
| 03 | `03-data-governance.md` | Article 10 | Training data provenance, representativeness, bias assessment, candidate/user data processing, lawful basis |
| 04 | `04-human-oversight.md` | Article 14 | Oversight design, roles, workflow, override mechanism, training, effectiveness monitoring |
| 05 | `05-logging-traceability.md` | Article 12 | What must be logged, logging architecture, retention, integrity, active monitoring |
| 06 | `06-performance-monitoring.md` | Articles 15 + 17 | Accuracy metrics, fairness metrics, oversight quality metrics, drift detection, annual review |

**Start with Document 01.** It is the most factual and least legally complex. Use it to establish the template and voice before moving to the legally heavier documents.

---

## 3. The Core Legal Argument — "Deaf People Travel Too"

This is the spine of the entire conformity pack and must be bulletproof. The argument:

**EU AI Act and GDPR jurisdiction follows the affected person, not the company's headquarters.**

SignalPath is a US company. It does not operate in the EU. But:

1. Deaf US users travel internationally. A Deaf user making a VRS call from Paris, London, or Berlin is in the EU when the call is processed.
2. GDPR Article 9 applies to biometric data processing. SP-AI-001 processes hand shape, facial expression, and body position — biometric data under GDPR Article 4(14). The processing occurs regardless of where the company is headquartered.
3. EU AI Act Annex III High Risk classification: SP-AI-001 processes biometric data to produce outputs affecting access to essential communications services for a protected population. Once a user is in the EU, the system is operating in EU jurisdiction.
4. The EU AI Act Article 2(1)(c) applies to AI systems whose outputs are used in the EU — the question is not where the server is, but where the output is consumed.

**This argument is the reason a US accessibility company must care about EU AI Act conformity.** Without it, a hiring manager might reasonably ask "why does a US company need an EU AI Act conformity pack?" The answer is: because your users travel, because GDPR Article 9 has no headquarters exception, and because the functional equivalency standard for your emergency relay calls does not stop at the US border.

---

## 4. The Jurisdictional Stack

Every conformity document should be written with awareness of three regulatory layers. Where a US obligation is as strong or stronger than the EU requirement, note both. This demonstrates that you understand the full regulatory surface area, not just EU compliance.

### Layer 1: US Federal
- **FCC Part 64** — Video Relay Service functional equivalency standard. Relay services must provide access substantially equivalent to voice telephone service. Emergency relay failures are a direct violation.
- **ADA Title IV** — Telecommunications relay services must be functionally equivalent. This is the domestic statutory basis.
- **FCC VRS requirements** — Quality of service standards, call handling requirements, mandatory human interpreter capacity.

### Layer 2: US State (High Priority)
- **Illinois Biometric Information Privacy Act (BIPA)** — The strictest biometric privacy law in the US. Covers retina/iris scans, fingerprints, voiceprints, and **scans of face geometry or hand geometry**. SP-AI-001 processes hand geometry and facial expression — almost certainly within BIPA scope.
  - Requires written consent before collection
  - Requires written retention and destruction policy publicly available
  - Private right of action: $1,000 per negligent violation, $5,000 per intentional or reckless violation
  - No need to prove actual harm — statutory damages
  - Class action exposure is severe
  - **Verify:** Does VRS call processing of hand shape constitute "scan of hand geometry" under 740 ILCS 14/? (This is the adversarial review question.)

- **California CPRA (Consumer Privacy Rights Act)** — Biometric data is sensitive personal information under Section 1798.140(ae)(1)(E). Requires disclosure and opt-out right. CPRA applies if SP-AI-001 processes data from California residents — which it will for any California VRS user.

- **New York** — No comprehensive biometric privacy law as of May 2026, but NYC Local Law 144 (AI in employment) shows direction of travel. Monitor for state-level biometric legislation.

- **Texas** — Capture or Use of Biometric Identifier (CUBI) act, similar to BIPA but weaker enforcement. Applies to biometric identifiers including hand geometry.

### Layer 3: EU/UK
- **GDPR Article 4(14)** — Definition of biometric data includes "specific technical processing relating to the physical, physiological or behavioural characteristics of a natural person, which allow or confirm the unique identification of that natural person." SP-AI-001 processes hand shape and facial expression — this likely meets the definition.
- **GDPR Article 9** — Biometric data used to uniquely identify natural persons is a special category requiring explicit consent (or another Article 9(2) basis). No GDPR Article 9 consent framework existed before the POC — this was RISK-004 in the risk assessment.
- **GDPR Article 35** — Data Protection Impact Assessment required for large-scale processing of biometric data. Mandatory before deployment.
- **EU AI Act Article 6 + Annex III** — High Risk classification. SP-AI-001 falls under Annex III Category 1 (biometric identification and categorisation) or Category 6 (access to essential services) — **verify which category applies and which is stronger.**
- **EU AI Act Article 9** — Risk management system: continuous iterative process across lifecycle.
- **EU AI Act Article 10** — Data governance: training data must be relevant, representative, free from errors, complete.
- **EU AI Act Article 11 + Annex IV** — Technical documentation requirements.
- **EU AI Act Article 12** — Record-keeping: logging capabilities enabling traceability.
- **EU AI Act Article 14** — Human oversight: deployers must implement measures enabling humans to understand, monitor, and intervene.
- **EU AI Act Article 15** — Accuracy, robustness, cybersecurity: appropriate levels for intended purpose.
- **EU AI Act Article 17** — Post-market monitoring plan for deployers.
- **EU AI Act Article 43** — Conformity assessment: mandatory before deployment for High Risk systems.
- **EU AI Act Article 73** — Serious incident reporting to national authorities.
- **UK** — UK AI Act trajectory follows EU direction. Not legally equivalent as of May 2026 but directionally relevant.

---

## 5. Claims Requiring Adversarial Review

These are the specific legal claims that a technically sophisticated interviewer might probe. Verify each one against primary sources before finalizing the documents.

### Claim 1: EU AI Act Annex III Category — Which one applies?
**The question:** SP-AI-001 processes biometric data for ASL interpretation. Does it fall under:
- Annex III Category 1(a): "AI systems intended to be used for the biometric identification of natural persons" — or
- Annex III Category 6: "AI systems intended to be used in the context of... essential private and public services"?

**Why it matters:** Category 1(a) systems have the strictest conformity assessment requirements (notified body, not internal control). If SP-AI-001 is Category 1(a), internal conformity assessment under Article 43(2) may not be sufficient.

**Likely answer:** The EU AI Act Article 3(40) defines "real-time remote biometric identification system" narrowly. SP-AI-001 does not identify individuals — it interprets language. It is more defensibly Category 6 (essential services) than Category 1(a) (identification). But this needs to be sourced against the actual Annex III text, not assumed.

### Claim 2: BIPA Scope — Does VRS hand processing constitute "scan of hand geometry"?
**The question:** BIPA covers "scans of face geometry or hand geometry." Does SP-AI-001's computer vision processing of hand shape for ASL interpretation constitute a "scan of hand geometry" under 740 ILCS 14/?

**Why it matters:** If yes, BIPA consent and retention obligations apply for all Illinois users — and the class action exposure is severe.

**Likely answer:** Yes. Illinois courts have interpreted BIPA broadly. Processing a video frame to extract hand shape features likely constitutes a "scan of hand geometry." But the specific case law and Illinois AG guidance should be checked.

### Claim 3: GDPR Article 9 Lawful Basis — Which Article 9(2) exception applies?
**The question:** If SP-AI-001 processes biometric data, which Article 9(2) basis justifies it?
- Article 9(2)(a): Explicit consent — requires affirmative opt-in, can be withdrawn
- Article 9(2)(g): Substantial public interest — possible for emergency relay context

**Why it matters:** Article 9(2)(a) explicit consent is the most defensible basis but requires an operational consent mechanism. Article 9(2)(g) is more flexible but requires a basis in EU or Member State law. For a US company, consent is the cleaner argument.

### Claim 4: EU AI Act Territorial Scope — Does Article 2 extend to US companies serving EU travelers?
**The question:** EU AI Act Article 2(1)(c) applies to "providers and deployers of AI systems that are not established or located in the Union, where the output produced by the AI system is used in the Union." Does a US Deaf user making a VRS call from France trigger this?

**Why it matters:** This is the core of the "Deaf people travel" argument. If the answer is yes, SP-AI-001 falls within EU AI Act scope when used by EU-based travelers.

**Likely answer:** Yes, for calls placed from within the EU. Article 2(1)(c) is clear on output being used in the Union. The output (interpreted speech) is consumed by both parties on the call — if either party is in the EU, the argument strengthens.

---

## 6. Research Protocol

Before writing any document, verify the following sources in order:

1. **EU AI Act full text** — Fetch from EUR-Lex. Verify Annex III categories, Annex IV documentation requirements, and Articles 9, 10, 11, 12, 14, 15, 17, 43, 73 in full.
   - URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689

2. **GDPR full text** — Verify Articles 4(14), 9, 35 for biometric data definitions and DPIA requirements.
   - URL: https://gdpr-info.eu/

3. **BIPA (Illinois)** — Verify the definition of "biometric identifier" and "biometric information" under 740 ILCS 14/10.
   - URL: https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=3004

4. **CPRA (California)** — Verify definition of biometric data as sensitive personal information under Section 1798.140.
   - California AG website or leginfo.legislature.ca.gov

5. **FCC Part 64** — Verify functional equivalency standard for VRS.
   - FCC website or ecfr.gov

6. **ADA Title IV** — Verify telecommunications relay service requirements.
   - ADA.gov

**Multi-model cross-check protocol:**
After drafting each document, run the following prompt through a second model (e.g., GPT-4o or Gemini):
> "Review this EU AI Act conformity document for [System X]. Identify any legal claims that are inaccurate, overstated, or not supported by the cited articles. Flag any missing obligations that a High Risk deployer would be required to address under the EU AI Act."

Focus adversarial review on Documents 02 (risk management) and 03 (data governance), which contain the most specific legal claims.

---

## 7. Document Template

Each document should follow this structure:

```
# Document [N]: [Title]
**System:** SignalPath Interpret (SP-AI-001)
**EU AI Act Reference:** Article [X]
**Document Type:** Deployer (SignalPath Technologies)
**Version:** 1.0 — [Date]
**Regulatory Coverage:** EU AI Act | GDPR | FCC Part 64 | [State law if applicable]
---
[Document content]
---
*Regulatory references verified against primary sources as of [date].*
```

Each document should include a "Jurisdictional Coverage" note where relevant — not a full legal opinion, but an acknowledgment that the obligation described applies under EU AI Act AND is paralleled (or exceeded) by US Federal or State law. This is where the "Deaf people travel" argument lives operationally.

---

## 8. Situational Framing Approach

For each Article, write two layers:
1. **What the Article requires** — Plain English, accurate, sourced
2. **What it means for SignalPath specifically** — Situational application, why this matters for a Deaf accessibility company, where the Deaf travel argument applies

Example (Article 14, Human Oversight):
> "Article 14 requires that High Risk AI systems be designed to allow human oversight. For SignalPath Interpret, this is not an abstract compliance requirement. It is the architecture decision that determines whether a Deaf user on a 911 call has a backup when the AI fails. Every technical decision about confidence thresholds and human interpreter handoff is an Article 14 implementation decision."

This framing is what makes the documents portfolio-worthy versus compliance-boilerplate.

---

## 9. Build Sequence for Project 5 Session

1. Fetch and read EU AI Act Annex III — confirm SP-AI-001 classification category
2. Fetch and read EU AI Act Annex IV — confirm technical documentation requirements
3. Verify BIPA scope claim (hand geometry)
4. Write Document 01 (Intended Purpose) — least legally complex, establishes template
5. Review Document 01 before proceeding
6. Write Documents 02–06 in order, verifying each article citation before writing
7. Multi-model adversarial review of Documents 02 and 03
8. Wire all 6 documents into the Streamlit conformity pack tab (already scaffolded in app.py)
9. Update the main README to reflect Project 5 completion

---

## 10. What Is Already Built

By the time this session runs, the following will be in place:
- app.py has a "EU AI Act Conformity Pack" tab inside the Governance Documentation Hub section
- The tab shows a selectbox for Document 1–6 with a "Coming soon" placeholder
- The `content/conformity-pack/` folder exists in the repo
- The repo is restructured to Option Clean layout

The only work remaining for Project 5 is: research, write the 6 documents, drop them into `content/conformity-pack/`, and remove the placeholder text from app.py.

---

*This handoff was created 2026-05-19. Start by reading the EU AI Act text, then align before writing.*
