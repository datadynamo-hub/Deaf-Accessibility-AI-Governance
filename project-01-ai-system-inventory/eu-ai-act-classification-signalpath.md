# EU AI Act Risk Classification — SignalPath Technologies

**Classification Date:** May 2026
**Prepared by:** AI Governance Program Office
**Review Due:** November 2026

\---

## Classification Framework

The EU AI Act establishes four risk tiers. Classification determines the compliance obligations that attach to a system. This document records the classification decision and rationale for each AI system in SignalPath's inventory.

SignalPath applies the EU AI Act as its ethical benchmark globally — not only where legally mandated. EU-facing operations, GDPR biometric data obligations, and the presence of traveling US Deaf users accessing SignalPath services from EU countries create real regulatory surface area. Building to the strictest available standard protects the community SignalPath serves.

### Risk Tier Overview

|Tier|Regulatory Treatment|
|-|-|
|**Unacceptable Risk**|Prohibited. System must not be deployed.|
|**High Risk**|Strict pre-deployment obligations. Conformity assessment required. Ongoing monitoring, logging, human oversight, and documentation mandated.|
|**Limited Risk**|Transparency obligations. Users must be informed they are interacting with an AI.|
|**Minimal Risk**|No specific regulatory obligations under the Act. General sector rules (FCC, GDPR, ADA) still apply.|

\---

## Classification Decisions

\---

### SP-AI-001 · SignalPath Interpret

**Classification: HIGH RISK**

**Legal Basis:** EU AI Act Annex III, Category 5(b) — AI systems processing biometric data to produce outputs that directly affect access to essential communications services. FCC functional equivalency standard applies independently.

**Rationale:**

SignalPath Interpret processes biometric data — hand shape, facial expression, body position — simultaneously to translate ASL in real time. In ASL, facial expressions carry grammatical meaning: a raised eyebrow changes a statement into a question. A model that gets the hands right but the face wrong is not making a translation error — it is producing a different sentence.

This is not a productivity tool. It is the communication channel itself for Deaf users. Errors carry direct consequences in medical appointments, legal proceedings, and emergency relay calls. A misclassified sign on a 911 relay call is a life-safety event.

**Obligations triggered:**

* Conformity assessment before production deployment (Article 43)
* Technical documentation (Article 11 + Annex IV)
* Logging and traceability — every interpretation session (Article 12)
* Human oversight — human interpreter on standby for low-confidence outputs (Article 14)
* Accuracy, robustness, and bias testing across signer variation, regional dialect, and physical limitation (Article 15)
* Biometric data processing — explicit consent required (GDPR Article 9)
* Registration in EU database (Article 71)

**Current compliance gap:** System is pre-production. No conformity assessment conducted. No bias audit for signer variation. Facial expression classification accuracy not benchmarked. Human oversight architecture not yet defined. **Priority: Critical — gate condition for production deployment.**

\---

### SP-AI-002 · SignalPath Forum

**Classification: LIMITED RISK**

**Legal Basis:** EU AI Act Article 52(1) — transparency obligation for AI systems interacting directly with natural persons. GDPR Article 9 applies to voice data processed in real time.

**Rationale:**

SignalPath Forum transcribes speech in real time for hard-of-hearing users. It does not make decisions affecting access to services, employment, or other consequential outcomes. Users retain full agency — they can request clarification if errors occur. Not listed in Annex III high-risk categories.

Voice data processed in real time constitutes biometric data under GDPR. Ephemeral processing mitigates but does not eliminate the obligation.

**Obligations triggered:**

* AI disclosure to end users (Article 52(1))
* GDPR Article 9 — explicit consent for biometric voice data processing
* No high-risk conformity requirements

**Current compliance gap:** Disclosure implementation to be verified across all channels. GDPR consent adequacy to be confirmed at next review. **Priority: Low.**

\---

### SP-AI-003 · SignalPath Express Call Routing ML

**Classification: LIMITED RISK**

**Legal Basis:** Not listed in Annex III. Does not meet high-risk threshold under current architecture. FCC emergency call handling requirements apply independently.

**Rationale:**

The call routing model matches VRS calls to available interpreters. Human override is available at all times. A misrouted call is corrected by the next available interpreter — it does not constitute a denial of access to services.

If the routing model ever incorporates caller behavioral scoring or profiling beyond operational matching, classification must be revisited immediately.

**Obligations triggered:**

* No high-risk EU AI Act obligations
* FCC emergency call handling standards apply independently
* Article 52 not triggered — callers are not directly interacting with the AI

**Current compliance gap:** Routing logic not documented to explain ability standard. Emergency call escalation logic to be audited. **Priority: Medium — FCC exposure is the primary risk here.**

\---

### SP-AI-004 · CaptionCall AI

**Classification: LIMITED RISK**

**Legal Basis:** EU AI Act Article 52(1) — transparency obligation. FCC Telecommunications Relay Service rules are the primary regulatory framework.

**Rationale:**

CaptionCall AI provides home phone captioning for hard-of-hearing users. It does not make consequential decisions affecting natural persons. Users retain full agency. FCC captioning accuracy standards are the operative compliance framework.

**Obligations triggered:**

* AI disclosure — users should be informed captions are AI-generated (Article 52(1))
* FCC accuracy and reliability standards (primary framework)
* No high-risk conformity requirements

**Current compliance gap:** Disclosure language to be confirmed. FCC compliance monitoring in place. **Priority: Low.**

\---

### SP-AI-005 · Microsoft Copilot (M365)

**Classification: LIMITED RISK**

**Legal Basis:** EU AI Act Article 52(1) — Copilot interacts directly with employees and generates content on their behalf. Not listed in Annex III for internal productivity use.

**Rationale:**

Microsoft Copilot is embedded across M365. The EU AI Act tier is Limited. The data governance profile is not. Copilot can ingest emails, meeting transcripts, SharePoint documents, and Teams chat history across the entire M365 tenant. If that data includes relay call strategy, interpreter personal data, FCC compliance discussions, or HR records, Copilot's data access scope becomes a governance event independent of its EU AI Act classification.

**Obligations triggered:**

* Article 52(1) — employees should understand they are using an AI system
* Microsoft EU AI Act compliance representations in enterprise agreement to be reviewed
* GDPR data minimization — Copilot access scope must be defined and restricted

**Current compliance gap:** Copilot data access scope not formally defined. Employee awareness of what Copilot can access is low. **Priority: High — data exposure profile exceeds EU AI Act tier.**

\---

### SP-AI-006 · Workday AI

**Classification: HIGH RISK**

**Legal Basis:** EU AI Act Annex III, Category 4(a) — *"AI systems intended to be used for recruitment or selection of natural persons, notably for advertising vacancies, screening or filtering applications, evaluating candidates in the course of interviews or tests, or for making decisions on promotion and termination of work-related contractual relationships."*

**Rationale:**

Workday AI influences workforce planning, attrition prediction, skills matching, and recruiting decisions across SignalPath's 10,000+ person workforce. AI-driven recommendations about who to hire, who is at risk of leaving, and which roles to fill affect employment outcomes for thousands of individuals.

Attrition prediction models carry bias risk — if historical attrition data reflects structural inequity, the model may encode and amplify it. The interpreter workforce is SignalPath's operational core.

**Obligations triggered:**

* Conformity assessment (Article 43)
* Technical documentation (Article 11)
* Human oversight — AI recommendations reviewed by HR before any employment decision is finalized (Article 14)
* Bias audit on training data for interpreter workforce demographics (Article 10)
* Workday vendor contract must include EU AI Act compliance representations (Article 28)

**Current compliance gap:** No bias audit confirmed. Workday contract AI Act clauses not verified. Attrition model logic not documented. **Priority: High.**

\---

### SP-AI-007 · UKG AI (Workforce Management)

**Classification: LIMITED RISK**

**Legal Basis:** Not listed in Annex III for operational scheduling. Outputs inform but do not autonomously determine employment decisions.

**Rationale:**

UKG AI recommends shift structures and flags staffing gaps. Final scheduling decisions are made by operations managers. However, scheduling outputs affect interpreter income directly. If UKG outputs are applied without human review to reduce interpreter hours, the high-risk threshold may be crossed and classification must be revisited.

**Obligations triggered:**

* No high-risk EU AI Act obligations under current architecture
* FCC minimum staffing compliance: UKG outputs must be validated against FCC requirements before implementation
* Human review required before any scheduling output that reduces interpreter hours

**Current compliance gap:** Human review process not formally documented. FCC staffing compliance validation not confirmed. **Priority: Medium.**

\---

### SP-AI-008 · Zendesk AI

**Classification: LIMITED RISK**

**Legal Basis:** EU AI Act Article 52(1) — Zendesk AI interacts directly with customers through automated responses.

**Rationale:**

Zendesk AI triages support tickets and routes cases. Customers can escalate to human agents at any point. It does not make consequential access decisions.

One SignalPath-specific consideration: many Deaf users communicate in written English as a second language, with ASL as their primary language. Sentiment analysis models trained on native English writing may systematically misclassify Deaf users' communications. This bias vector does not exist in standard Zendesk deployments and must be validated.

**Obligations triggered:**

* Article 52(1) — customers should be informed when interacting with AI support
* Sentiment model accuracy validation for ASL-first English writing patterns
* No high-risk conformity requirements

**Current compliance gap:** Sentiment model not validated for Deaf user communication patterns. Disclosure implementation to be confirmed. **Priority: Medium.**

\---

### SP-AI-009 · Autogen AI (RFP Platform)

**Classification: MINIMAL RISK**

**Legal Basis:** Not listed in Annex III. Internal sales operations tool. No direct impact on natural persons outside SignalPath.

**Rationale:**

Autogen AI generates RFP responses reviewed and approved by humans before submission. It does not make decisions affecting natural persons. Risk shifts if proprietary pricing, FCC compliance representations, or confidential capability data is retained or used for model training by the vendor — a data governance concern, not an EU AI Act issue.

**Obligations triggered:**

* No EU AI Act obligations
* Vendor data retention and training policy must be reviewed

**Current compliance gap:** Vendor data handling policy not reviewed. **Priority: Low.**

\---

### SP-AI-010 · ZoomInfo AI

**Classification: MINIMAL RISK**

**Legal Basis:** Not listed in Annex III. B2B sales intelligence tool. No consequential decisions affecting natural persons made autonomously.

**Rationale:**

ZoomInfo enriches contact data and surfaces buying intent signals. Human staff review all outputs before outreach. GDPR is the operative concern — ZoomInfo's data sourcing practices have faced European regulatory scrutiny.

**Obligations triggered:**

* No EU AI Act obligations
* GDPR Article 6 legal basis for processing EU contact data must be confirmed
* ZoomInfo Data Processing Agreement to be reviewed

**Current compliance gap:** GDPR legal basis for EU contact processing not confirmed. **Priority: Low.**

\---

### SP-AI-011 · Gong (Revenue Intelligence)

**Classification: LIMITED RISK**

**Legal Basis:** EU AI Act Article 52(1) — Gong records and transcribes conversations involving natural persons. Participants must be informed.

**Rationale:**

Gong records sales calls and applies AI analysis to transcripts and deal risk scores. External prospects must be informed. Call recording consent is a legal requirement in most jurisdictions independently of the EU AI Act.

If Gong outputs inform performance reviews or termination decisions for sales staff, reclassification as High Risk under Annex III Category 4(a) is required.

**Obligations triggered:**

* Article 52(1) — prospects must be informed calls are recorded and AI-analyzed
* Reclassify as High Risk if Gong is used in employment performance decisions
* Recording consent procedures to be audited

**Current compliance gap:** Consent disclosure consistency not confirmed. Gong's role in performance management to be clarified before final classification is confirmed. **Priority: Medium.**

\---

### SP-AI-012 · GitHub Copilot (Engineering)

**Classification: MINIMAL RISK**

**Legal Basis:** Not listed in Annex III. Developer productivity tool. No direct impact on natural persons.

**Rationale:**

GitHub Copilot assists engineers with code generation. EU AI Act risk tier is minimal. The data governance risk is not: engineers may inadvertently include API keys, internal data schemas, or proprietary architecture in Copilot prompts processed by GitHub's servers. Personal Copilot accounts used outside the enterprise license are Shadow AI (see SP-AI-016).

**Obligations triggered:**

* No EU AI Act obligations
* Policy required: what code and data may be submitted to Copilot
* Enterprise license data handling terms to be reviewed

**Current compliance gap:** No formal policy on Copilot prompt content. Personal account shadow use unquantified. **Priority: Low.**

\---

### SP-AI-013 · Outside Counsel AI (Harvey AI)

**Classification: HIGH RISK (Third-Party Processor)**

**Legal Basis:** EU AI Act Article 28 — deployer obligations follow the data. GDPR processor obligations apply. SignalPath is the data controller. Its obligations travel with the data regardless of which entity processes it.

**Rationale:**

This is the governance gap most organizations have not addressed. When SignalPath sends contracts, FCC regulatory filings, and RFP documents to outside counsel, that data leaves SignalPath's control. If the law firm uses Harvey AI to analyze those documents — standard practice at major firms in 2026 — SignalPath has an AI system processing its most sensitive data that it did not procure, did not risk-assess, and has zero direct visibility into.

Documents processed include privileged legal communications, FCC compliance strategies, interpreter contract terms, and confidential capability data.

**Obligations triggered:**

* Article 28 — data processing agreement must explicitly address outside counsel's AI tool use
* GDPR — Harvey AI must be identified as a sub-processor in the DPA
* Outside counsel engagement agreement must require AI tool disclosure and prior approval
* SignalPath retains audit rights over AI-processed outputs

**Current compliance gap:** Outside counsel engagement agreement almost certainly does not contain AI tool clauses. This gap is industry-wide — most organizations have not addressed it. **Priority: Critical.**

\---

### SP-AI-014 · FCC Regulatory Monitoring Tool

**Classification: MINIMAL RISK**

**Legal Basis:** Not listed in Annex III. Internal compliance intelligence tool. Output is informational — all alerts reviewed by human compliance staff before action.

**Rationale:**

The FCC monitoring tool surfaces relevant regulatory changes to the compliance team. It does not make decisions affecting natural persons. If the tool misses a relevant FCC change, the consequence is operational non-compliance — not an EU AI Act classification issue.

**Obligations triggered:**

* No EU AI Act obligations
* Vendor to be confirmed — discovery item
* Output validation process to be documented

**Current compliance gap:** Vendor not yet confirmed. Validation process not documented. **Priority: Low.**

\---

### SP-AI-015 · Microsoft Sentinel / Defender AI

**Classification: LIMITED RISK**

**Legal Basis:** EU AI Act Article 14 (human oversight) applies in spirit — automated response actions affecting employee accounts warrant governance review even where formal high-risk classification does not apply.

**Rationale:**

Sentinel monitors the M365 environment for security threats. AI-automated responses — blocking accounts, quarantining files — can affect employees without immediate human review. In a VRS environment, an automated account block during a live shift takes an interpreter offline mid-call, creating both a service delivery failure and a potential FCC compliance event.

**Obligations triggered:**

* No high-risk EU AI Act obligations
* Human review policy required before automated actions affecting interpreter accounts during active shifts
* Logging of all automated responses for audit

**Current compliance gap:** Automated response rules not reviewed for VRS service delivery impact. **Priority: Medium.**

\---

### SP-AI-016 · Shadow AI — Unmanaged Employee AI Use

**Classification: UNCLASSIFIABLE — TREATED AS HIGH RISK PENDING DISCOVERY**

**Legal Basis:** EU AI Act classification requires knowing which systems are in use, what data they process, and under what terms. Classification is impossible until discovery is complete. Precautionary principle applies: treat as High Risk. GDPR Article 5 (data integrity and confidentiality) is violated by definition when employees submit corporate data to unvetted consumer AI tools without data processing agreements in place.

**Rationale:**

Shadow AI is not a single system — it is a risk class representing all AI tools currently in use by SignalPath employees without IT approval, security review, or data processing agreements. Industry benchmarks confirm shadow AI adoption is active and significant at organizations of this size and sector.

The VRS context elevates this from a data governance gap to a potential regulatory event. FCC rules protect relay call content as legally privileged communication. An interpreter coordinator summarizing call logs in ChatGPT, a legal staff member uploading a contract to Claude, an engineer pasting an internal API schema into Gemini — each instance is a potential FCC compliance violation with no audit trail and no remediation path.

Known shadow AI categories in this environment: consumer LLMs (ChatGPT, Claude, Gemini) used on work data; meeting recorders (Otter.ai, Fireflies, Fathom) uploading transcripts to third-party servers; browser extensions (Grammarly) processing email and document content; voice tools (ElevenLabs) used by training or marketing teams; translation tools (DeepL free tier) processing internal documents; document AI (ChatPDF, Adobe Acrobat AI) processing internal PDFs; personal coding AI accounts used by engineers outside enterprise license.

**Obligations triggered:**

* Immediate discovery: CASB or firewall log audit, browser extension scan via endpoint management, expense report review for micro-transactions to AI vendors
* GDPR — data processing agreements required for any tool touching personal data
* FCC — relay call content must not be processed by any system outside SignalPath's control without explicit policy and legal review
* Employee AI acceptable use policy required before this inventory is presented to the board
* Approved tool list to be published and communicated to all staff

**Current compliance gap:** No discovery conducted. No acceptable use policy exists. No approved tool list published. This is the highest-urgency governance gap in the inventory — not because the EU AI Act tier is highest, but because it is the gap most likely to have already produced a compliance event that SignalPath does not yet know about. **Priority: Critical — begin discovery immediately.**

\---

## Classification Summary

|System|Classification|Compliance Status|Priority|
|-|-|-|-|
|SP-AI-001 SignalPath Interpret|High Risk|Pre-production — conformity assessment required before deployment|Critical|
|SP-AI-002 SignalPath Forum|Limited Risk|Partial — disclosure verification required|Low|
|SP-AI-003 Express Call Routing ML|Limited Risk|Partial — routing logic documentation required|Medium|
|SP-AI-004 CaptionCall AI|Limited Risk|Adequate — disclosure language to confirm|Low|
|SP-AI-005 Microsoft Copilot|Limited Risk|Gap — data access scope undefined|High|
|SP-AI-006 Workday AI|High Risk|Gap — no bias audit, no contract AI clauses|High|
|SP-AI-007 UKG AI|Limited Risk|Partial — human review process not documented|Medium|
|SP-AI-008 Zendesk AI|Limited Risk|Gap — sentiment model not validated for Deaf users|Medium|
|SP-AI-009 Autogen AI|Minimal Risk|Gap — vendor data retention policy not reviewed|Low|
|SP-AI-010 ZoomInfo AI|Minimal Risk|Gap — GDPR legal basis for EU contacts unconfirmed|Low|
|SP-AI-011 Gong|Limited Risk|Gap — consent consistency and performance review role unclear|Medium|
|SP-AI-012 GitHub Copilot|Minimal Risk|Gap — no prompt content policy|Low|
|SP-AI-013 Outside Counsel Harvey AI|High Risk (Third-Party)|Critical gap — no AI clause in engagement agreement|Critical|
|SP-AI-014 FCC Monitoring Tool|Minimal Risk|Gap — vendor unconfirmed|Low|
|SP-AI-015 Microsoft Sentinel|Limited Risk|Gap — automated response rules not reviewed for VRS impact|Medium|
|SP-AI-016 Shadow AI|Unclassifiable — High Risk pending discovery|Critical gap — no discovery conducted, no policy exists|Critical|

\---

*Classification decisions are not static. Review required annually or upon material change to any system's design, purpose, deployment context, or applicable regulatory framework. Three systems carry Critical priority and require immediate action before this inventory is presented to the board.*

