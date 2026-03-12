# Document 1: System Description and Intended Purpose

**System:** HireAssist Pro
**Provider:** HireFlow Technologies Ltd (v3.1)
**Deployer:** NorthStar Financial Services
**Document Type:** Provider documentation (supplied) + Deployer context (NorthStar-authored)
**EU AI Act Reference:** Article 11, Annex IV §1 and §2
**Version:** 1.0 — March 2026

---

## 1. System Identification

| Field | Value |
|-------|-------|
| System name | HireAssist Pro |
| Version | 3.1.2 |
| Provider | HireFlow Technologies Ltd, Amsterdam, Netherlands |
| Deployer | NorthStar Financial Services |
| Deployment context | Internal HR — all recruitment activity across NorthStar DE and NL |
| EU AI Act classification | High Risk — Annex III Category 4(a) |
| Unique system identifier | NS-AI-008 |
| Date of first deployment (NorthStar) | Target: 1 June 2026 (pending conformity confirmation) |

---

## 2. General Description of the AI System

HireAssist Pro is an AI-assisted recruitment support system that analyses candidate CVs and job descriptions to generate structured shortlists and candidate assessments. It is designed to support, not replace, human recruitment decisions.

The system uses a transformer-based natural language processing model to extract and compare candidate qualifications, experience, and skills against role requirements. It produces:

- A structured shortlist ranked by relevance score
- Per-candidate fit assessment across defined criteria
- Plain-language explanation of the basis for each candidate's score (explanation module)

The system is not an autonomous decision-making system. It generates recommendations. All decisions — shortlisting, rejection, invitation to interview — are made by human HR staff using the system's output as one input among several.

---

## 3. Intended Purpose

**Primary intended purpose:** To assist NorthStar HR coordinators and hiring managers in the initial screening of job applications, reducing the time required to review high volumes of CVs while maintaining structured, criteria-based assessment.

**Intended users:** Trained HR coordinators and hiring managers at NorthStar Financial Services.

**Intended context of use:** The system is deployed within NorthStar's applicant tracking system (Workday integration). It is used for all open roles across NorthStar's operations in Germany and the Netherlands. It is not intended for, and must not be used for, any purpose other than initial CV screening and shortlisting recommendations.

**Outputs and their intended use:**
- Shortlist and scores are **recommendations** to the HR coordinator
- HR coordinators are required to review the shortlist and exercise independent judgment before any candidate communication
- The system's explanation output is intended to assist reviewers in understanding the basis for the recommendation and in exercising meaningful oversight

**Intended operational lifespan:** 3 years, subject to annual review and performance assessment.

---

## 4. Prohibited Uses

The following uses of HireAssist Pro are explicitly prohibited at NorthStar:

- Using the system's output as the sole basis for any candidate rejection without human review
- Using the system for internal promotion or performance assessment decisions
- Using the system beyond the screening and initial shortlisting phase (e.g., for interview scoring, reference assessment)
- Processing candidate data beyond what is contained in submitted CVs and job descriptions without explicit candidate consent
- Allowing any individual who has not completed HireAssist Pro oversight training to act as a reviewer

Prohibited uses will be documented in the system's governance record and communicated to all system users during onboarding.

---

## 5. Known Limitations

The following limitations are acknowledged and documented:

| Limitation | Description | Mitigation |
|-----------|-------------|-----------|
| Language and format sensitivity | The model performs more accurately on well-formatted CVs with standard section headings. Unusual formats may result in incomplete data extraction. | HR coordinators are trained to identify and manually review non-standard CVs flagged by the system. |
| Skills vocabulary drift | Technical skills terminology evolves rapidly. The model may not recognise very recent terminology for emerging roles. | Job descriptions should include both current and legacy terminology where relevant. Model to be reviewed for vocabulary updates annually. |
| Over-reliance risk | Users may be tempted to accept AI recommendations without sufficient scrutiny. | Oversight training emphasises that the AI output is a starting point, not a conclusion. Override rates are monitored. |
| Coverage gaps for non-EU educational systems | The model was trained predominantly on European CV formats and educational credentials. Candidates with non-EU educational backgrounds may be disadvantaged if their credentials are not recognised. | HR coordinators are trained to verify credential equivalences manually for international candidates. Vendor to provide international credential mapping in v3.2. |

---

## 6. EU AI Act Classification Basis

**Classification:** High Risk
**Legal basis:** EU AI Act Annex III, Category 4(a) — *"AI systems intended to be used for recruitment or selection of natural persons, notably for advertising vacancies, screening or filtering applications, evaluating candidates in the course of interviews or tests or for filtering or ranking applications."*

HireAssist Pro falls squarely within this category. It screens and ranks candidate applications. The consequential nature of the decisions it informs (employment access) and the breadth of individuals affected makes this classification clear and non-controversial.

**Conformity assessment pathway:** Internal control (Article 43(2)) — the system is not a safety component in critical infrastructure and does not use real-time biometric identification. Internal conformity assessment is the applicable pathway.

---

*Provider documentation sections (§§ 1–5 of Annex IV) have been supplied by HireFlow Technologies Ltd and are incorporated into this document. NorthStar-specific deployer context is clearly identified above and in subsequent documents.*
