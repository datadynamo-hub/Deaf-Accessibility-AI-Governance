# EU AI Act Conformity Pack — Document 03
## Data Governance
**Article 10**

**System:** SP-AI-001 SignalPath Interpret
**Organization:** SignalPath Technologies
**Version:** 1.0 | **Classification:** Internal — Governance Documentation
**Effective Date:** May 2026 | **Next Review:** May 2027
**Owner:** Chief Privacy Officer | **Prepared by:** AI Governance Program Office

---

> **Review note for Jonathan:** This document contains the highest proportion of inferred detail. The consent framework, training data sourcing specifics, and jurisdiction detection mechanism are described at a governance level consistent with the rest of the repo, but the specific vendor names, dataset sizes, and technical implementation of the DPIA are placeholders that reflect what a real version of this document would contain. Review this one first.

---

## 1. Purpose and Scope

Article 10 of the EU AI Act requires that high-risk AI systems be developed using training, validation, and testing datasets that meet standards for relevance, representativeness, freedom from errors, and completeness. This document describes SignalPath's data governance practices for SP-AI-001 SignalPath Interpret, covering training data sourcing and provenance, data quality and bias assessment, biometric data handling under GDPR, consent frameworks, and data subject rights procedures.

---

## 2. Data Classification

SP-AI-001 processes the following data categories during inference:

| Data Type | Classification | Legal Basis |
|---|---|---|
| Live video feed — hand shape, hand position, movement trajectory | Biometric data — GDPR Article 4(14), Article 9 | Explicit consent (Article 9(2)(a)) |
| Live video feed — facial expression and configuration | Biometric data — GDPR Article 4(14), Article 9 | Explicit consent (Article 9(2)(a)) |
| Body position and posture | Biometric data — GDPR Article 4(14), Article 9 | Explicit consent (Article 9(2)(a)) |
| Audio feed from hearing party | Personal data — GDPR Article 4(1) | Legitimate interest / contractual necessity |
| Session metadata (call type, region, interpreter ID) | Operational data | Contractual necessity |
| Confidence score output and audit logs | Operational data | Legitimate interest (compliance and safety) |

The classification of visual sign language features as biometric data is not a conservative interpretation. Hand shape, facial expression, and body position in the context of ASL interpretation constitute data derived from the physical characteristics of a natural person that allow or confirm that person's unique identification — the GDPR Article 4(14) definition. This classification is reinforced by the Article 9 restriction on processing biometric data for the purpose of uniquely identifying natural persons, which applies even where unique identification is not the system's primary purpose.

---

## 3. Training Data

### 3.1 Sourcing and Provenance

SP-AI-001 v1.0 was trained on a curated corpus of annotated ASL video data. The training corpus comprises:

- **Primary dataset:** Annotated ASL gesture sequences collected directly by SignalPath from consenting signers across multiple US regions, conducted between 2022 and 2024. Collection was conducted under IRB-equivalent research protocols with explicit informed consent for use in AI model training.
- **Secondary datasets:** Supplementary annotated ASL corpora from academic research partners, licensed for commercial AI training use. Provenance documentation is maintained in the Engineering data registry.
- **Exclusions:** No data sourced from VRS calls was used in training. Call data is operationally collected under a separate legal basis and is explicitly excluded from training pipelines by a data segregation control implemented in the data infrastructure.

### 3.2 Dataset Composition

| Demographic Variable | Coverage | Known Gap |
|---|---|---|
| Skin tone (Fitzpatrick scale) | Tones I–IV well represented; V–VI underrepresented | Documented in RISK-001; corrective action initiated |
| Age | 18–45 primary; under 18 and over 65 limited | Planned expansion in v1.1 data refresh |
| Regional ASL dialect | East Coast and West Coast primary; Midwest, Southern Black ASL limited | Targeted collection underway |
| Physical variation (limb difference, limited mobility) | Minimal representation | Open gap; no corrective action date set |
| Oral Deaf and non-native ASL signers | Limited representation | Documented in RISK-001 |

The demographic gaps above are not hypothetical. Incident SP-INC-2026-001 documented a measurable skin tone accuracy disparity in SP-AI-001 during the proof of concept phase. The corrective action from that incident — expanded demographic coverage in the v1.1 training data refresh — is in progress and is a condition of production deployment clearance.

### 3.3 Annotation Quality

Training data annotation was performed by a combination of Deaf ASL-fluent annotators and hearing ASL-certified interpreters. Annotation guidelines specify:

- Per-segment confidence scoring by annotators
- Disagreement resolution protocol: minimum three annotators per segment; majority agreement required; disputed segments escalated to a Deaf senior annotator
- Annotation quality audit: 10% random sample of annotated segments reviewed by a separate annotation quality team

Annotation quality metrics are maintained in the Engineering data registry and reviewed at each retraining cycle.

### 3.4 Validation and Test Data

Validation and test datasets were held out from training data at the point of collection. They are not subsets of the training corpus. The validation set was used during model development to tune hyperparameters and confidence thresholds. The test set was used for final pre-deployment evaluation only.

Both validation and test sets were reviewed for demographic representativeness prior to use. Known demographic gaps in the training corpus are reflected in the validation and test sets, which means that published model performance metrics are likely to overstate accuracy for underrepresented demographics. This limitation is disclosed in the risk assessment (RISK-001) and is a condition on residual risk acceptance.

---

## 4. Biometric Data Processing — GDPR Compliance

### 4.1 Legal Basis

SignalPath processes biometric data in SP-AI-001 on the basis of explicit consent under GDPR Article 9(2)(a). Reliance on other Article 9(2) bases (substantial public interest, Article 9(2)(g); preventive medicine, Article 9(2)(h)) was evaluated and determined to be insufficiently defensible for a commercial AI system in a non-clinical setting. Explicit consent is the appropriate and most defensible basis.

For US-based users who are not EU data subjects at the time of processing, FCC Part 64 and SignalPath's VRS service terms govern data handling. The GDPR consent framework applies to all users where there is a reasonable possibility of EU jurisdiction at the point of processing — including US-based users traveling internationally.

### 4.2 Consent Framework

The SP-AI-001 consent framework covers:

**Pre-service disclosure:** Users are informed that the VRS service uses AI assistance. The disclosure specifies:
- What data is processed (visual sign language features including hand shape, facial expression, and body position)
- How it is used (real-time ASL interpretation support for human interpreters)
- Whether it is stored (session data retained for audit; raw video is not retained beyond call duration except under incident investigation protocols)
- That they can opt out of AI-assisted processing and receive human-only interpretation

**Explicit consent capture:** Consent is obtained at account creation and at first use of an AI-assisted session. Consent is recorded with timestamp, user ID, and the version of the consent language presented.

**Opt-out mechanism:** Users can opt out of AI-assisted processing at any time via account settings or by requesting human-only routing from the interpreter at the start of a call. Opt-out is immediate and does not affect service availability.

**Consent refresh:** Users are notified and re-consented when material changes are made to the biometric data processing scope.

### 4.3 Data Subject Rights

| Right | Implementation |
|---|---|
| Right of access (Article 15) | Users can request a summary of their consent record and session metadata. Raw video is not retained beyond call duration. |
| Right to rectification (Article 16) | Consent records and metadata can be corrected on request. |
| Right to erasure (Article 17) | Consent records and session metadata are deleted on request. Model weights are not individually reversible; this limitation is disclosed. |
| Right to restriction (Article 18) | Processing can be suspended for a specific user on request pending resolution of a dispute. |
| Right to object (Article 21) | Users can object to biometric processing and be moved to human-only routing. |
| Right not to be subject to solely automated decisions (Article 22) | Not triggered: all SP-AI-001 output is mediated by a human interpreter. No decision affecting the caller is made without human review. |

### 4.4 Data Retention

| Data Type | Retention Period | Basis |
|---|---|---|
| Raw video feed | Duration of call only; not retained | Minimisation |
| Confidence scores and session telemetry | 24 months | Compliance and audit |
| Consent records | Duration of user relationship + 7 years | Legal obligation |
| Incident investigation data | Duration of investigation + 5 years | Legal obligation |
| Audit logs | 24 months (standard); 5 years (incident-linked) | Article 12 obligations |

---

## 5. Data Quality Controls

In accordance with Article 10(3), the following practices are applied to ensure training data quality:

- **Bias assessment:** Demographic representativeness analysis is conducted on training data before each model training run. Results are documented and reviewed by the AI Governance Program Office.
- **Error detection:** Annotation quality audit (10% sample) conducted before training data finalisation.
- **Gap documentation:** Known gaps in demographic coverage are formally documented in the risk register and disclosed in this document.
- **Corrective action tracking:** Training data gaps identified in incident reviews (including SP-INC-2026-001) are tracked as open corrective actions with named owners and target dates.
- **No prohibited sources:** Training data does not include data scraped without consent, data obtained from VRS call recordings, or data from jurisdictions where collection was not legally authorised.

---

## 6. Data Protection Impact Assessment

A Data Protection Impact Assessment (DPIA) for SP-AI-001's biometric data processing has been initiated under the ownership of the Chief Privacy Officer, in accordance with GDPR Article 35 (processing of biometric data for the purpose of uniquely identifying natural persons triggers mandatory DPIA). The DPIA is in progress and its completion is a condition of production deployment clearance alongside the conformity pack.

The DPIA covers: processing necessity and proportionality; risks to data subjects; measures to address identified risks; and consultation with the Deaf Community Advisory Panel on community-specific privacy concerns.

---

## 7. Document Control

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | May 2026 | AI Governance Program Office | Initial release — see review note in header |

*This document forms part of the EU AI Act Conformity Pack for SP-AI-001 SignalPath Interpret. Review by General Counsel and Chief Privacy Officer is required prior to any regulatory submission. This document contains inferred detail that must be validated against actual engineering and legal records before external use.*
