# Document 3: Data Governance

**System:** HireAssist Pro (NS-AI-008)
**EU AI Act Reference:** Article 10 (Data and Data Governance)
**Document Type:** Provider documentation (supplied by HireFlow) + Deployer (NorthStar) additions
**Version:** 1.0 — March 2026

---

## 1. Overview

Article 10 of the EU AI Act requires that high-risk AI systems use training, validation, and testing data that meets defined quality criteria. This document records the data governance practices for HireAssist Pro, covering both the training data used by the provider (HireFlow Technologies Ltd) and the candidate data processed by NorthStar as deployer.

---

## 2. Training Data (Provider — HireFlow Technologies Ltd)

### 2.1 Training Dataset Description

| Parameter | Detail |
|-----------|--------|
| Dataset name | HireFlow Recruitment Corpus v3 |
| Size | 4.2 million CV–job description pairs |
| Geographic coverage | EU-27 (weighted towards Germany, Netherlands, France, Poland) |
| Time range | 2015–2024 |
| Languages | English, German, Dutch, French |
| Source | Aggregated from HireFlow enterprise customers (anonymised) + public job posting datasets |

### 2.2 Data Provenance and Lawfulness

HireFlow confirms that:
- All data was collected under applicable data protection law
- Enterprise customer data was provided under data processing agreements that include authorisation for aggregated model training (confirmed in contract)
- Public dataset sources are identified in the technical documentation annex
- No data was used that was subject to a competing intellectual property claim

**NorthStar confirmation received:** Legal confirmed that the data provenance documentation satisfies NorthStar's standard for third-party AI training data. [Date: to be confirmed]

### 2.3 Data Relevance and Representativeness

The training dataset has been assessed for relevance and representativeness against the following criteria (Article 10(3)):

| Criterion | Assessment |
|-----------|-----------|
| **Relevance** | Dataset consists of real CV–job description pairs. Relevant to the task of CV-to-job matching. ✓ |
| **Representativeness** | Dataset covers EU geographies with weighting. Underrepresentation risk exists for Eastern European candidates and non-EU educational backgrounds. Documented limitation (see Document 1, Section 5). |
| **Completeness** | Dataset is large (4.2M pairs). Completeness assessed as adequate for the task. |
| **Freedom from errors** | Automated quality filtering applied (deduplication, format normalisation, personally identifiable information removal). Manual spot-checking of 2% of records performed. |
| **Statistical properties** | Dataset statistics documented by HireFlow in technical documentation annex. Gender distribution: 51% male-presenting / 44% female-presenting / 5% not determinable. Age: median applicant age 31; range 18–72. |

### 2.4 Bias Assessment of Training Data

HireFlow conducted a bias evaluation of the training dataset and model outputs prior to v3.1 release. Key findings:

- **Gender:** Demographic parity ratio (female:male shortlisting rate) = 0.94. Within accepted threshold (≥0.80). No remediation required.
- **Age:** Candidates over 50 show a 0.87 demographic parity ratio. Flagged as a monitoring priority. Vendor has introduced age-neutral feature weighting for v3.1 to address this.
- **Ethnicity proxy (name-based):** Analysis conducted using name-based ethnicity inference as a proxy. Demographic parity ratio for name-inferred non-European candidates = 0.91. Within threshold.
- **Disability:** Insufficient signal in training data to evaluate. NorthStar to implement manual process for candidates who disclose disability in application.

**NorthStar independent validation** of the bias evaluation is planned for April 2026 using a sample candidate dataset. Results will be documented separately and will be a condition of go-live approval.

---

## 3. Validation and Testing Data

### 3.1 Validation Dataset

HireFlow used a held-out validation set of 420,000 CV–job description pairs (10% of total dataset, stratified by geography and industry). Validation metrics are documented in the technical documentation annex.

### 3.2 NorthStar Acceptance Testing Dataset

NorthStar will conduct acceptance testing using a dataset of 300 historical NorthStar job applications (anonymised) across three representative role types:
- Junior analyst (entry level, high volume)
- Senior technology specialist (specialist role, lower volume)
- Operations coordinator (administrative, mixed volume)

Acceptance criteria are defined in the deployment plan. The testing dataset includes known-quality indicators to allow validation against ground truth.

---

## 4. Candidate Data Processed by NorthStar (Deployer)

### 4.1 Data Processed

HireAssist Pro processes the following candidate personal data when deployed by NorthStar:

| Data Category | Source | Processing Purpose | Retention |
|---|---|---|---|
| CV content (unstructured text) | Candidate submission | Model input for CV-JD matching | 12 months post-application |
| Job description text | NorthStar HR team | Model input | Indefinite (as job records) |
| Fit score and explanation output | Generated by system | Reviewer reference | 12 months post-application |
| Reviewer decision and override notes | HR coordinator | Oversight log | 36 months (employment law minimum) |

### 4.2 Lawful Basis

| Processing Activity | Lawful Basis | Notes |
|--------------------|-------------|-------|
| CV processing for shortlisting | Legitimate interests (GDPR Article 6(1)(f)) | Balanced against candidate rights assessment completed. Alternative: contract (Article 6(1)(b)) — legal to confirm preferred basis. |
| Logging of AI-assisted decisions | Legal obligation (GDPR Article 6(1)(c)) | EU AI Act Article 12 requires logging. |
| Retention for challenge/dispute purposes | Legitimate interests | Retention period justified by employment dispute limitation periods. |

**Note:** Candidates will be informed in the application process that AI is used for initial CV screening (transparency obligation). A GDPR Article 22 notice will be provided explaining that the AI output is reviewed by a human before any decision is communicated, and explaining how to request human review of any rejection.

### 4.3 Data Minimisation

NorthStar's deployment configuration processes only:
- CV content as submitted by the candidate
- Role-specific job descriptions

NorthStar does not supply to the model: social media profiles, salary data, references, or demographic information beyond what appears in the CV. Additional data sources require a new DPIA and are prohibited without AGPO approval.

### 4.4 Special Category Data

CVs may inadvertently contain special category data (health information, trade union membership, political views). HireFlow's system applies a special category data filter to identify and flag records that may contain such information. Flagged records are routed for manual review only — they are not processed by the AI model.

NorthStar candidates are instructed in the application portal not to include sensitive personal information beyond what is relevant to the role.

---

## 5. Data Governance Controls

| Control | Owner | Mechanism |
|---------|-------|----------|
| Data processing agreement with HireFlow | Legal | Executed — includes EU AI Act Article 28 deployer obligations |
| Candidate-facing AI disclosure | Legal + Product | Application portal notice — reviewed and approved |
| Special category data filter | HireFlow (provider) | Technical control in v3.1 |
| Data retention enforcement | IT / DPO | Automated deletion at 12/36 month thresholds |
| Annual data governance review | DPO + AGPO | Included in annual system review cycle |

---

*Vendor technical documentation (HireFlow HireAssist Pro v3.1 — Data and Training Documentation) is attached as Appendix A to the full conformity pack and available on request from the AI Governance Programme Office.*
