# SignalPath Streamlit — Session Handoff Document
*Created: 2026-05-19 | Verification password: BlueOstrich42*

---

## PASTE THIS INTO THE NEW CHAT TO RESUME

> I'm continuing a multi-session build of the SignalPath AI Governance Center — a Streamlit portfolio app. I have a session handoff document with full context. The verification password is **BlueOstrich42**. Please read the file at `C:\Users\jonat\OneDrive\Documents\GitHub\AiGovernance\SESSION-HANDOFF.md` and confirm you've ingested it before we do anything. DO NOT write any code or call any tools until I give you the go-ahead. We align first, then build.

---

## 1. Who I Am & What This Project Is

**Jon Khan** — Data Infrastructure and AI Governance professional. Deaf community member. Building publicly.
- GitHub: https://github.com/datadynamo-hub
- LinkedIn: https://www.linkedin.com/in/jonathan-k-184393120/

**The Project:** SignalPath AI Governance Center — an interactive Streamlit portfolio demo built around a fictional Deaf accessibility company called **SignalPath Technologies**. The scaffolding is forked from Taimur Ijlal's open-source AI governance repo. The context, risk framing, and community are mine.

**The Goal:** Signal "production mindset" to GRC hiring managers. Static documents don't do that. A deployed, interactive governance platform with a video walkthrough does.

**The Deployment:** Streamlit Cloud, connected to GitHub. Live app updates on every push.

---

## 2. Repository Structure

**My working repo (the one we build in):**
`C:\Users\jonat\OneDrive\Documents\GitHub\AiGovernance`

**Taimur's original repo (reference only — do not modify):**
`C:\Career\Projects\Taimur AiGovernance Repo`

**Current file structure of my repo:**
```
AiGovernance/
├── .git/
├── project-01-ai-system-inventory/
│   ├── .streamlit/
│   │   └── config.toml
│   ├── ai-system-inventory-signalpath.xlsx   ← 16 AI systems, 17 columns
│   ├── app.py                                ← THE MAIN APP (462 lines, fully working)
│   ├── eu-ai-act-classification-signalpath.md
│   ├── nist-rmf-mapping-signalpath.md
│   ├── project-01-README.md
│   └── requirements.txt
├── project-02-risk-assessment/
│   ├── risk-assessment.md                    ← 269 lines
│   ├── governance-review-memo.md             ← 143 lines
│   └── project-02-README.md
├── project-03-responsible-ai-policy/
│   ├── responsible-ai-policy.md              ← 265 lines
│   ├── governance-operating-model.md         ← 289 lines
│   ├── ai-review-process.md                  ← 266 lines
│   └── project-03-README.md
└── README.md
```

**Taimur's repo has 2 additional projects we plan to incorporate:**
```
Taimur AiGovernance Repo/
├── project-04-incident-response/
│   ├── incident-scenario.md                  ← 92 lines (NorthStar Financial — needs SignalPath remap)
│   ├── incident-response-timeline.md         ← 216 lines
│   └── root-cause-analysis.md               ← 135 lines
└── project-05-high-risk-documentation/
    ├── 01-intended-purpose.md                ← 96 lines
    ├── 02-risk-management-summary.md         ← 182 lines
    ├── 03-data-governance.md                 ← 132 lines
    ├── 04-human-oversight.md                 ← 196 lines
    ├── 05-logging-traceability.md            ← 149 lines
    └── 06-performance-monitoring.md          ← 160 lines
```

---

## 3. Current State of app.py (FULLY WORKING — 462 lines)

**Location:** `C:\Users\jonat\OneDrive\Documents\GitHub\AiGovernance\project-01-ai-system-inventory\app.py`

**Streamlit Cloud main file setting:** `project-01-ai-system-inventory/app.py`

**Key architectural patterns — DO NOT change these without alignment:**

```python
BASE_PATH = "project-01-ai-system-inventory"
# All file paths build off this. Streamlit Cloud runs from repo root.
# xlsx: os.path.join(BASE_PATH, "ai-system-inventory-signalpath.xlsx")
# md files: os.path.join(BASE_PATH, "eu-ai-act-classification-signalpath.md")

# Navigation: session_state buttons (NOT st.tabs at the top level)
if "view" not in st.session_state:
    st.session_state.view = "Command Center"
# Three buttons: "Command Center" | "Active Registry Inventory" | "Regulatory Framework Mapping"
# type="primary" for active button, "secondary" for inactive

# System selector synced across tabs via:
st.session_state.selected_system  # shared between Command Center and Registry dropdowns

# Null field handling:
# mitigation_strategy → "Not yet defined"
# all other empty fields → "Under Review"
```

**Current 3-section structure:**
1. **Command Center** — 4 metric cards + system selector + Live Control Monitor (slider-based breach simulator)
2. **Active Registry Inventory** — filtered data grid (6 columns) + deep-dive profile panel (all 17 fields)
3. **Regulatory Framework Mapping** — st.tabs with EU AI Act .md and NIST RMF .md rendered as markdown

**SYSTEM_CONTROLS dict:** All 16 systems (SP-AI-001 through SP-AI-016) have unique per-system entries with 6 fields each: `breach_vector`, `guardrail`, `target_metric`, `response_sla`, `escalation_1`, `escalation_2`.

**Sidebar filters (LEFT SIDEBAR — working perfectly, do not touch):**
- Business Unit: selectbox ("All Units" + individual BUs)
- Risk Tiers: checkbox "All Risk Tiers" (default True) → conditional multiselect only shown when unchecked
- Deployment Status: checkbox "All Deployment Statuses" (default True) → conditional multiselect

**Dynamic banner** above content area changes text based on active view. Uses `st.info()`.

**Known technical debt:**
- `requirements.txt` is inside `project-01-ai-system-inventory/` but needs to be at repo root for Streamlit Cloud (currently working because Streamlit Cloud found it — do not move without testing)
- `.streamlit/config.toml` is inside `project-01-ai-system-inventory/.streamlit/` (same — working, do not move without testing)
- Line 344 has a duplicate `ap = get_system_profile(...)` call — cosmetic, not breaking

**Writing large files:** The Write tool truncates at lines containing `**` bold markers inside Python f-strings. ALWAYS use bash heredoc for full rewrites:
```bash
cat > "/sessions/.../mnt/AiGovernance/project-01-ai-system-inventory/app.py" << 'PYEOF'
[full file content]
PYEOF
```
Then verify with: `python3 -c "import py_compile; py_compile.compile('/path/app.py'); print('SYNTAX OK')"` and `wc -l`.

---

## 4. The Excel Data Schema (17 columns, 16 rows)

Column names (exact, snake_case):
`system_id`, `system_name`, `description`, `category`, `business_unit`, `primary_purpose`, `data_inputs`, `outputs`, `deployment_status`, `system_owner`, `vendor_or_internal`, `affected_persons`, `geographic_scope`, `eu_ai_act_risk_tier`, `nist_rmf_maturity_level`, `fcc_regulatory_exposure`, `notes`

`mitigation_strategy` column is empty for all 16 systems (handled via null protection).

Risk tiers in the data use mixed casing — normalized to lowercase for matching in the app.

---

## 5. The Expansion Plan (ALIGNED — this is the direction we're going)

### Target Architecture: 4 Nav Sections

```
[ Operational Command Center ] [ Risk Intelligence ] [ Incident Response Simulator ] [ Governance Documentation Hub ]
```

---

### Section 1: Operational Command Center (EXISTING — no changes needed)
Current state is final. Live Control Monitor, metric cards, system selector, filtered registry, deep-dive profiles.

---

### Section 2: Risk Intelligence (NEW — from Project 2)

**Source files:**
- `project-02-risk-assessment/risk-assessment.md`
- `project-02-risk-assessment/governance-review-memo.md`

**What to build:**
A **5×5 risk heat map** plotting all 16 SignalPath AI systems by likelihood × impact. This is the GRC equivalent of a model accuracy plot — recruiters understand it in 3 seconds.

**Implementation approach:**
- Extract likelihood and impact scores from the risk-assessment.md (or hardcode them as a dict if the .md doesn't have clean numeric data — check the file first)
- Use `st.plotly_chart` or `matplotlib` to render a color-coded 5×5 grid
- Each system appears as a labeled point on the grid
- Clicking (or selecting from dropdown) a system shows its risk narrative below
- The governance-review-memo.md renders as a styled executive memo in a second sub-tab

**Color coding:** Red = High/Unacceptable, Orange = High Risk, Yellow = Limited Risk, Green = Minimal Risk

---

### Section 3: Incident Response Simulator (NEW — from Project 4, remapped to SignalPath)

**Source files (Taimur's repo — need SignalPath remap):**
- `Taimur AiGovernance Repo/project-04-incident-response/incident-scenario.md`
- `Taimur AiGovernance Repo/project-04-incident-response/incident-response-timeline.md`
- `Taimur AiGovernance Repo/project-04-incident-response/root-cause-analysis.md`

**The SignalPath remap (CRITICAL DECISION — already aligned):**
Taimur's scenario involves NorthStar Financial's credit scoring AI being discriminatorily biased against specific postcodes. The SignalPath remap will use **SP-AI-001** (the real-time ASL interpretation AI) producing systematically worse recognition accuracy for **Black Deaf signers** — a documented real-world failure mode in computer vision models trained on non-diverse ASL datasets. This is authentic, defensible, and more impactful than a financial services scenario.

**What to build:**
A **phase-by-phase incident response walkthrough** with interactive progression:
- Phase 0: Detection (automated — control monitor fires below LCL)
- Phase 1: Triage (24 hours)
- Phase 2: Containment (model isolated, human interpreters activated)
- Phase 3: Investigation & Root Cause Analysis
- Phase 4: Remediation & Retraining
- Phase 5: Regulatory Reporting (FCC notification, ADA documentation)
- Phase 6: Post-Incident Review

UI pattern: `st.button("Next Phase →")` or `st.select_slider` to advance through phases. Each phase shows the timeline entry, key decisions made, who was notified, and what the governance log recorded. This directly extends the Live Control Monitor story — what happens after the alert fires.

**New SignalPath markdown files to create:**
- `project-04-incident-response/signalpath-incident-scenario.md`
- `project-04-incident-response/signalpath-incident-timeline.md`
- `project-04-incident-response/signalpath-root-cause-analysis.md`

These files need to be written before the UI can be built. The content rewrite is a research + writing task, not a coding task.

---

### Section 4: Governance Documentation Hub (NEW — from Projects 3 + 5)

**Source files (Projects 3 and 5):**
Project 3: `responsible-ai-policy.md`, `governance-operating-model.md`, `ai-review-process.md`
Project 5: All 6 EU AI Act conformity documents (currently NorthStar/HireAssist Pro — need SignalPath remap to SP-AI-001)

**What to build:**
A clean **document library** using `st.tabs()` inside this section. No heavy interactivity needed. The goal is demonstrating organizational depth and EU AI Act Article 9-17 knowledge.

Sub-tabs:
- `Responsible AI Policy`
- `Governance Operating Model` (RACI matrix — could render as styled dataframe)
- `AI Review Process`
- `EU AI Act Conformity Pack` (6 sub-documents as a nested selector or accordion)

**Project 5 remap needed:** Taimur's Project 5 covers NorthStar's "HireAssist Pro" hiring AI. The SignalPath equivalent is SP-AI-001 (real-time ASL interpretation — already classified as High Risk under EU AI Act due to biometric sign language processing). The 6 conformity documents need to be rewritten with SignalPath context before they can be displayed. This is a content task that can happen in parallel with or after the Section 3 build.

---

## 6. Repo Structure Decision (NOT YET IMPLEMENTED — alignment pending)

**Current state:** app.py is in `project-01-ai-system-inventory/`. The repo looks like a multi-project portfolio (which it is).

**The problem:** Streamlit Cloud's "main file" is currently `project-01-ai-system-inventory/app.py`. As we expand to 4 sections, there's no longer a strong argument for app.py living inside a project subfolder — it is the whole platform.

**Two options discussed (decision deferred to next session):**

Option A (low-risk, fast): Move only `app.py` to repo root. Keep all data files in their project subfolders. `BASE_PATH` stays `"project-01-ai-system-inventory"` — zero path changes needed. Update Streamlit Cloud main file setting to `app.py`. The project folders remain visible in GitHub.

Option B (clean but more work): Move `app.py` to root AND restructure supporting files into named subfolders. More file moves, more path updates, bigger window of broken deployment.

**Recommendation:** Do Option A first. After the 4-section expansion is complete and tested, revisit Option B.

**Requirements.txt and config.toml:** Currently in the wrong place (inside project-01 subfolder) but working. Do not move them until Option A or B is executed — moving them in isolation risks breaking deployment.

---

## 7. The Video Strategy (ALIGNED)

**Format:** 5-minute produced walkthrough. Not a raw screen capture — a narrative:
1. Open on GitHub repo — show folder structure, README, 3-project (or 5-project) organization. ~45 seconds.
2. Cut to Streamlit — live deployed URL in browser. Walk each of the 4 sections. ~3.5 minutes.
3. Close with one sentence on why Deaf accessibility AI governance matters and why this project exists. ~30 seconds.

**Distribution:**
- GitHub README: thumbnail image linking to YouTube/Loom embed
- LinkedIn: Featured section + post at launch
- Resume: QR code or hyperlink in projects section
- Cover letters: direct URL

**The video gets recorded AFTER the 4-section build is complete.** Don't record a teaser on a 3-section app if you're about to add more.

---

## 8. Build Sequence for Next Session

**Step 1 — Read the risk-assessment.md file first.** Check whether it contains numeric likelihood and impact scores or whether they need to be extracted/hardcoded. This determines how complex the Risk Heat Map build is.

**Step 2 — Expand the navigation from 3 buttons to 4.** Add "Risk Intelligence" and "Incident Response Simulator" as new session_state views. Rename "Regulatory Framework Mapping" to "Governance Documentation Hub." Update the BANNERS dict. This is a mechanical change to the nav block.

**Step 3 — Build Section 2 (Risk Intelligence).** Start with the heat map visualization. If numeric data is clean in the .md, extract it. If not, hardcode a likelihood/impact dict for all 16 systems.

**Step 4 — Write the SignalPath incident response documents.** Content task: remap Taimur's Project 4 documents from NorthStar Financial to SignalPath/SP-AI-001. The incident: ASL computer vision model producing systematically worse recognition for Black Deaf signers. This is the narrative foundation for Section 3.

**Step 5 — Build Section 3 (Incident Response Simulator).** Phase-by-phase interactive timeline using the new SignalPath documents.

**Step 6 — Build Section 4 (Governance Documentation Hub).** Sub-tabbed document library pulling from Projects 3 and 5. Project 5 remap to SignalPath can happen here or be deferred.

**Step 7 — Repo restructure (Option A).** Move app.py to root. Update Streamlit Cloud main file setting. Test deployment.

**Step 8 — Record the walkthrough video.** Only after all 4 sections are built and deployed.

---

## 9. Working Rules (DO NOT VIOLATE)

1. **Align before coding.** Never write code without explicit "go ahead" from Jon.
2. **Text-only advisory responses** when asked for strategy discussions. No tool calls.
3. **Bash heredoc for full file rewrites** — the Write tool truncates at `**` bold markers in Python strings.
4. **Always verify after writes:** `py_compile` for syntax, `wc -l` for line count, spot-check 3-4 key strings.
5. **Sidebar is sacred.** The current left sidebar filter UX (selectbox + checkbox pattern) is the best version. Never touch it without explicit alignment.
6. **Session state navigation pattern is sacred.** Buttons + `st.session_state.view` + `st.rerun()`. Do not replace with `st.tabs()` at the top level.
7. **No hallucination tolerance.** If uncertain about what a file contains, read it first. Never assume column names, file encodings, or content structure.
8. **Jon uses GitHub Desktop** (not git CLI) for all git operations. Never give git CLI instructions.

---

## 10. Context on Jon's Working Style

- Highly deliberate. Flags AI hallucination risk proactively.
- Requires explicit alignment before any implementation.
- Thinks visually — the recruiter's 30-second impression matters more than technical elegance.
- Domain expert in Deaf accessibility. The SignalPath context is authentic lived experience, not invented.
- Non-technical on git/deployment. Technical on governance content and product thinking.
- Values clean, modern UI (Resend/Vanta/Stripe aesthetic — light theme, soft borders, professional typography).
- Does not want emoji overuse, excessive bullet points, or generic AI-sounding copy in the app.

---

*End of handoff document. The next session starts by reading this file and confirming ingestion.*
