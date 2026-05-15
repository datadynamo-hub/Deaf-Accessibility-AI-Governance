# NIST AI RMF Mapping — SignalPath Technologies

**Framework Reference:** NIST AI Risk Management Framework (AI RMF 1.0)
**Mapping Date:** May 2026

---

## Purpose

This document maps each AI system in SignalPath's inventory against the four core functions of the NIST AI RMF. It identifies which practices are in place, which are absent, and where the most significant governance gaps exist.

The four functions are:

| Function | Core Question |
|----------|--------------|
| **GOVERN** | Are the right accountability structures, policies, and culture in place? |
| **MAP** | Have we identified and contextualised the risks associated with this system? |
| **MEASURE** | Have we analysed and assessed those risks in a rigorous, documented way? |
| **MANAGE** | Are we actively treating risks, monitoring systems, and ready to respond? |

Maturity is rated 1–4:

| Level | Description |
|-------|-------------|
| 1 | Initial — ad hoc or absent |
| 2 | Developing — some practices exist but inconsistently applied |
| 3 | Defined — documented and repeatable processes in place |
| 4 | Optimised — continuously improved with feedback loops |

---

## System Mappings

---

### SP-AI-001 · SignalPath Interpret (High Risk — Pre-Production)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | Chief Product Officer listed as accountable. No formal AI governance charter references this system. No board-level visibility of risk classification. | No AI governance policy for pre-deployment systems. No defined escalation path for model risk decisions. No community advisory input from Deaf users. | 1 |
| **MAP** | Engineering team understands the use case. Risk context partially documented in product roadmap. | No formal risk mapping document. Signer variation risks (accent, dialect, physical limitation) not assessed. Affected population (all VRS Deaf users) not formally documented. Emergency relay call risk scenario not modeled. | 1 |
| **MEASURE** | POC accuracy benchmarking underway for hand shape. Facial expression classification accuracy not benchmarked. No bias evaluation across signer demographics. | No performance thresholds defined for production readiness. No fairness assessment. No documentation of training data provenance or signer diversity in training set. | 1 |
| **MANAGE** | No production monitoring framework exists — system not yet deployed. No incident response plan for interpretation errors. No defined human oversight architecture for low-confidence outputs. | Production monitoring plan required before deployment. Human-in-the-loop architecture must be defined and tested. Incident response playbook for 911 relay call failures required. | 1 |

**Overall Maturity: 1.0 (Initial)**
**Priority Actions:** Establish governance gate criteria for production deployment. Conduct bias audit across signer variation. Define accuracy thresholds — including minimum acceptable performance on emergency relay calls. Build human oversight architecture. This system must not go to production without completing these steps.

---

### SP-AI-002 · SignalPath Forum (Limited Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | Head of Product — Captioning accountable. GDPR consent framework in place for voice data. | No AI-specific governance policy. Captioning accuracy standard not formally defined at governance level. | 2 |
| **MAP** | Use case and risk context well understood. PII and voice data risks identified. | Risk mapping informal. Medical and legal context risks (high-stakes captioning errors) not formally assessed. | 2 |
| **MEASURE** | Accuracy monitored with human review trigger below 94% threshold. Session deletion compliance tracked. | No formal bias assessment. Accuracy benchmarks not documented to audit standard. | 3 |
| **MANAGE** | Auto-deletion at session end implemented. PII detection in pipeline active. Human review escalation defined. | No formal AI incident classification. Accuracy degradation response procedure not documented. | 3 |

**Overall Maturity: 2.5 (Developing — Defined)**
**Priority Actions:** Formalize risk mapping document. Define and document accuracy thresholds to audit standard. Add AI incident category to complaints framework.

---

### SP-AI-003 · SignalPath Express Call Routing ML (Limited Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | Head of VRS Operations accountable. Operational runbook exists for call handling. | No AI-specific governance policy. Routing model not reviewed at governance level. | 2 |
| **MAP** | Operational risk context understood by VRS team. Emergency call escalation logic exists. | Routing logic not formally documented. Risk of emergency call misrouting not formally modeled. | 2 |
| **MEASURE** | Wait time and call completion rates tracked. | Routing model accuracy and failure modes not formally benchmarked. No fairness assessment across caller demographics. | 2 |
| **MANAGE** | Human override available at all times. Emergency call flag routes to senior interpreter pool. | No defined response procedure for routing model failures during peak load or outages. | 2 |

**Overall Maturity: 2.0 (Developing)**
**Priority Actions:** Document routing logic to explainability standard. Define emergency call routing failure response procedure. Formalize model performance benchmarks.

---

### SP-AI-004 · CaptionCall AI (Limited Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | Head of Product — CaptionCall accountable. FCC compliance monitoring in place. | No AI-specific governance layer beyond FCC compliance. | 3 |
| **MAP** | Use case and regulatory context well understood. FCC accuracy standards define risk boundary. | Risk mapping informal — adequate given risk tier. | 3 |
| **MEASURE** | FCC accuracy and reliability metrics tracked. | No formal bias assessment — appropriate given risk classification. | 3 |
| **MANAGE** | FCC compliance monitoring active. Service reliability SLAs in place. | No AI-specific incident classification beyond FCC reporting requirements. | 3 |

**Overall Maturity: 3.0 (Defined)**
**Priority Actions:** Add AI incident category. Confirm AI disclosure language. Annual review sufficient otherwise.

---

### SP-AI-005 · Microsoft Copilot M365 (Limited Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | IT / CTO accountable at system level. No AI-specific governance policy governing Copilot data access scope. | No policy defining what data Copilot may access. No employee training on Copilot data exposure. Board has no visibility of Copilot's data access profile. | 1 |
| **MAP** | Productivity use case understood. Data exposure risks not formally assessed. | Copilot's access to relay call strategy discussions, interpreter HR data, and FCC compliance documents not mapped. Shadow access risk not quantified. | 1 |
| **MEASURE** | No formal measurement of Copilot data access scope or outputs. | No audit of what data Copilot has accessed or summarized. No monitoring for sensitive data appearing in Copilot outputs. | 1 |
| **MANAGE** | Microsoft enterprise agreement governs data handling at a high level. | No SignalPath-specific Copilot data governance policy. No process for employees to report Copilot misuse or data exposure. | 1 |

**Overall Maturity: 1.0 (Initial)**
**Priority Actions:** Define Copilot data access scope policy immediately. Conduct tenant-level audit of Copilot access permissions. Train employees on what Copilot can see. This is a High priority action despite Limited Risk EU AI Act classification.

---

### SP-AI-006 · Workday AI (High Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | Chief People Officer accountable. Workday managed through HR and IT procurement. | No AI-specific governance policy for Workday AI features. HR staff using AI-generated recommendations have not received AI governance training. No board visibility of high-risk classification. | 1 |
| **MAP** | HR use case understood. Workforce planning risks identified at an operational level. | Attrition prediction bias risk not formally assessed. Interpreter workforce demographic profile not mapped against model training data. Affected population (10,000+ employees) not formally documented in governance terms. | 1 |
| **MEASURE** | Workday provides standard HR analytics. No independent bias evaluation conducted. | No fairness metrics tracked. No accuracy benchmarks for attrition prediction. No documentation of training data provenance from Workday. | 1 |
| **MANAGE** | HR managers make final decisions — human in the loop at a functional level. No formal policy requiring human review of AI recommendations before employment action. | No AI monitoring framework. No incident response procedure for biased or erroneous AI-driven HR recommendations. | 1 |

**Overall Maturity: 1.0 (Initial)**
**Priority Actions:** Require Workday to supply training data documentation and bias audit results. Update vendor contract with AI Act compliance clauses. Implement formal human review policy before any employment decision informed by Workday AI. Conduct internal bias assessment on attrition model outputs.

---

### SP-AI-007 · UKG AI — Workforce Management (Limited Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | Head of VRS Operations accountable. UKG managed through IT procurement. | No AI-specific governance policy. FCC staffing compliance validation process not formally tied to UKG outputs. | 2 |
| **MAP** | Scheduling use case understood. FCC minimum staffing requirements known. | Risk of scheduling outputs affecting interpreter income without human review not formally mapped. | 2 |
| **MEASURE** | Scheduling efficiency and FCC staffing compliance tracked operationally. | No formal measurement of scheduling model fairness across interpreter demographics. | 2 |
| **MANAGE** | Operations managers review schedules before publication. | No formal policy requiring human review before any output that reduces interpreter hours. Escalation path for scheduling disputes not documented in AI governance terms. | 2 |

**Overall Maturity: 2.0 (Developing)**
**Priority Actions:** Document human review requirement for any scheduling output reducing interpreter hours. Validate FCC staffing compliance process against UKG outputs formally.

---

### SP-AI-008 · Zendesk AI (Limited Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | Head of Customer Experience accountable. Zendesk managed through CX procurement. | No AI-specific governance policy. Sentiment model not reviewed at governance level. | 2 |
| **MAP** | Customer support use case understood. Escalation to human agent defined. | Deaf user communication pattern risk — written English as a second language affecting sentiment model accuracy — not formally identified or mapped. | 1 |
| **MEASURE** | Customer satisfaction scores and escalation rates tracked. | Sentiment model accuracy not validated against Deaf user communication patterns. No fairness assessment for ASL-first English writers. | 1 |
| **MANAGE** | Human escalation path exists. Customer complaints process covers AI interactions. | No AI-specific incident classification. No process for identifying or correcting systematic misclassification of Deaf user communications. | 2 |

**Overall Maturity: 1.5 (Initial — Developing)**
**Priority Actions:** Validate sentiment model against Deaf user writing patterns — this is a SignalPath-specific risk that does not exist in standard Zendesk deployments. Implement AI disclosure. Add AI incident category to complaints framework.

---

### SP-AI-009 · Autogen AI — RFP Platform (Minimal Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | Head of Sales accountable. Managed through sales procurement. | No AI-specific governance policy — adequate at this risk level. Vendor data handling not reviewed. | 2 |
| **MAP** | RFP use case understood. Proprietary data exposure risk not formally mapped. | Risk of confidential pricing and FCC compliance data being retained by Autogen vendor not assessed. | 2 |
| **MEASURE** | RFP win rates tracked. Output quality reviewed by sales team before submission. | No formal measurement of proprietary data exposure. | 2 |
| **MANAGE** | All outputs reviewed and approved by humans before submission. | No policy governing what data may be submitted to Autogen. Vendor data retention terms not reviewed. | 2 |

**Overall Maturity: 2.0 (Developing)**
**Priority Actions:** Review Autogen vendor data retention and training policy. Define policy on what data may be submitted to RFP platform.

---

### SP-AI-010 · ZoomInfo AI (Minimal Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | Head of Sales accountable. Managed through sales procurement. | No AI-specific governance policy — adequate at this risk level. GDPR legal basis for EU contacts not confirmed. | 2 |
| **MAP** | Sales use case understood. GDPR exposure for EU contacts not formally mapped. | EU contact data processing legal basis not documented. | 2 |
| **MEASURE** | Lead quality and conversion tracked. | No GDPR compliance audit of ZoomInfo contact data. | 2 |
| **MANAGE** | Human sales staff review all outputs before outreach. | No process for EU data subject requests flowing through ZoomInfo. | 2 |

**Overall Maturity: 2.0 (Developing)**
**Priority Actions:** GDPR team to confirm legal basis for EU contact processing. Review ZoomInfo DPA.

---

### SP-AI-011 · Gong — Revenue Intelligence (Limited Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | VP of Sales accountable. Gong managed through sales procurement. | No AI-specific governance policy. Gong's potential role in performance management not addressed at governance level. | 2 |
| **MAP** | Sales coaching use case understood. Recording consent risk identified. | Performance management risk — if Gong scores inform employment decisions — not formally mapped or addressed. | 2 |
| **MEASURE** | Deal risk scores and coaching outcomes tracked. | Recording consent compliance not formally audited across sales team. | 2 |
| **MANAGE** | Sales managers review Gong outputs. | No formal policy on use of Gong scores in performance reviews. No AI incident classification for recording consent failures. | 2 |

**Overall Maturity: 2.0 (Developing)**
**Priority Actions:** Define formal policy on whether Gong outputs may be used in performance or termination decisions — if yes, reclassify as High Risk. Audit recording consent procedures across sales team.

---

### SP-AI-012 · GitHub Copilot — Engineering (Minimal Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | CTO / Engineering Lead accountable. GitHub Copilot managed through IT. | No policy governing what code or data engineers may submit to Copilot. Personal account shadow use not addressed. | 2 |
| **MAP** | Engineering productivity use case understood. Proprietary code and API key exposure risk not formally mapped. | Risk of sensitive internal architecture appearing in Copilot prompts not assessed. | 1 |
| **MEASURE** | Developer productivity informally tracked. | No measurement of proprietary data exposure through Copilot prompts. | 1 |
| **MANAGE** | Enterprise license data handling governed by GitHub terms. | No SignalPath-specific policy on Copilot prompt content. No monitoring for engineers using personal accounts. | 1 |

**Overall Maturity: 1.25 (Initial)**
**Priority Actions:** Define and publish policy on what code and data may be submitted to Copilot. Audit for personal account shadow use. Despite Minimal Risk EU AI Act classification, data governance risk here is real.

---

### SP-AI-013 · Outside Counsel AI — Harvey AI (High Risk — Third Party)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | General Counsel accountable for outside counsel relationships. No AI governance framework covers third-party vendor AI use. | No policy requiring outside counsel to disclose AI tool use. No approval process for vendor AI touching SignalPath data. Board has no visibility of this exposure. | 1 |
| **MAP** | Outside counsel relationship and data flows understood at a legal level. AI risk within that relationship not mapped. | Specific risk that outside counsel's AI (Harvey or equivalent) processes SignalPath's FCC filings, contracts, and privileged communications has not been formally identified or documented. | 1 |
| **MEASURE** | Legal work product quality reviewed by General Counsel. | No measurement of what SignalPath data has been processed by outside counsel AI. No audit of Harvey AI data retention practices. | 1 |
| **MANAGE** | Outside counsel engagement managed through legal retainer agreements. | No AI clause in engagement agreements. No right to audit outside counsel AI use. No remediation path if privileged data has been processed without authorization. | 1 |

**Overall Maturity: 1.0 (Initial)**
**Priority Actions:** Immediately update outside counsel engagement agreements to require AI tool disclosure and prior approval. Add Harvey AI or equivalent as a named sub-processor in relevant DPAs. Establish audit rights. This is industry-wide gap — SignalPath can lead by addressing it first.

---

### SP-AI-014 · FCC Regulatory Monitoring Tool (Minimal Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | Chief Compliance Officer accountable. Vendor relationship managed through compliance procurement. | Specific vendor not yet confirmed — governance ownership pending vendor discovery. | 2 |
| **MAP** | Regulatory monitoring use case understood. Missed alert risk identified operationally. | Formal risk mapping not completed pending vendor confirmation. | 2 |
| **MEASURE** | Alert relevance informally validated by compliance team. | No formal false negative rate tracking — missed regulatory changes are the primary failure mode. | 2 |
| **MANAGE** | Compliance team reviews all outputs before action. | Vendor SLA covers uptime — not alert quality. No defined escalation if tool misses a material FCC change. | 2 |

**Overall Maturity: 2.0 (Developing)**
**Priority Actions:** Confirm vendor. Document validation process. Define escalation procedure for missed material FCC regulatory changes.

---

### SP-AI-015 · Microsoft Sentinel / Defender AI (Limited Risk)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | CISO / IT Security Lead accountable. Sentinel managed through IT security. | No policy governing automated response actions affecting interpreter accounts during active VRS shifts. | 2 |
| **MAP** | Security monitoring use case well understood. VRS service delivery impact of automated actions not formally mapped. | Risk that automated account blocks during active shifts take interpreters offline mid-call not formally identified in security governance. | 2 |
| **MEASURE** | Threat detection rates and false positive rates tracked by IT security. | No measurement of VRS service impact from Sentinel automated responses. | 2 |
| **MANAGE** | Automated response rules active. Human security team reviews incidents. | No carve-out policy protecting interpreter accounts from automated blocks during active call shifts. No coordination between IT security and VRS operations for incident response. | 2 |

**Overall Maturity: 2.0 (Developing)**
**Priority Actions:** Define and implement policy requiring human review before automated actions affecting interpreter accounts during active shifts. Establish coordination protocol between IT security and VRS operations.

---

### SP-AI-016 · Shadow AI — Unmanaged Employee AI Use (Unclassifiable — High Risk pending discovery)

| RMF Function | Current State | Gaps | Maturity |
|---|---|---|---|
| **GOVERN** | No owner. No policy. No governance framework covers shadow AI. | No AI acceptable use policy. No approved tool list. No employee training on shadow AI risk. Board has no visibility. This is a governance absence, not a gap. | 1 |
| **MAP** | Shadow AI risk is known at industry level. SignalPath-specific shadow AI landscape has not been mapped. | No discovery has been conducted. The specific tools in use, the data being processed, and the regulatory exposure created are entirely unknown. For a VRS company handling FCC-protected relay call content, this is the most significant unmapped risk in the inventory. | 1 |
| **MEASURE** | No measurement possible without discovery. | Cannot measure what has not been identified. Until CASB logs, endpoint scans, and expense reports are audited, the scope of shadow AI use is unknown. | 1 |
| **MANAGE** | No management framework exists. | No acceptable use policy. No approved tool list. No reporting mechanism for employees using unauthorized AI. No remediation path for data already processed by consumer AI tools. | 1 |

**Overall Maturity: 1.0 (Initial — by definition)**
**Priority Actions:** This is the most urgent item in the portfolio. Begin discovery immediately: (1) CASB or firewall log audit for outbound traffic to known AI tool domains, (2) endpoint management scan for unauthorized browser extensions, (3) expense report review for micro-transactions to AI vendors ($10–$30/month to OpenAI, Anthropic, Midjourney, ElevenLabs). Publish acceptable use policy and approved tool list before any other governance initiative. The probability that a compliance event has already occurred is high.

---

## Portfolio-Level Summary

| System | EU AI Act Tier | RMF Maturity | Action Priority |
|--------|---------------|-------------|----------------|
| SP-AI-001 SignalPath Interpret | High Risk | 1.0 | Critical — pre-production gate |
| SP-AI-002 SignalPath Forum | Limited Risk | 2.5 | Low |
| SP-AI-003 Express Call Routing ML | Limited Risk | 2.0 | Medium |
| SP-AI-004 CaptionCall AI | Limited Risk | 3.0 | Low |
| SP-AI-005 Microsoft Copilot | Limited Risk | 1.0 | High |
| SP-AI-006 Workday AI | High Risk | 1.0 | High |
| SP-AI-007 UKG AI | Limited Risk | 2.0 | Medium |
| SP-AI-008 Zendesk AI | Limited Risk | 1.5 | Medium |
| SP-AI-009 Autogen AI | Minimal Risk | 2.0 | Low |
| SP-AI-010 ZoomInfo AI | Minimal Risk | 2.0 | Low |
| SP-AI-011 Gong | Limited Risk | 2.0 | Medium |
| SP-AI-012 GitHub Copilot | Minimal Risk | 1.25 | Low |
| SP-AI-013 Outside Counsel Harvey AI | High Risk (Third-Party) | 1.0 | Critical |
| SP-AI-014 FCC Monitoring Tool | Minimal Risk | 2.0 | Low |
| SP-AI-015 Microsoft Sentinel | Limited Risk | 2.0 | Medium |
| SP-AI-016 Shadow AI | Unclassifiable — High Risk | 1.0 | Critical — begin discovery immediately |

**Portfolio risk concentration:** Four systems carry Critical priority status. Three of SignalPath's core AI products are High Risk under the EU AI Act, with SP-AI-001 (SignalPath Interpret) a pre-production gate condition. Two additional systems (Outside Counsel AI and Shadow AI) represent governance gaps that are industry-wide but unaddressed at SignalPath. The overall portfolio maturity is low — most systems are at Level 1 or 2. A structured remediation programme is required, sequenced by priority: Shadow AI discovery first, Outside Counsel AI contract remediation second, SignalPath Interpret pre-deployment governance third.

---

*Next review: November 2026, or upon any new AI system deployment, material change to an existing system, or new regulatory guidance from FCC, NIST, or EU AI Act implementing authorities.*
