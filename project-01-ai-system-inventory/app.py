import streamlit as st
import pandas as pd
import os

# 1. PAGE CONFIG & STATE
st.set_page_config(page_title="SignalPath AI Governance Center", page_icon=":shield:", layout="wide")

if "view" not in st.session_state:
    st.session_state.view = "Command Center"
if "selected_system" not in st.session_state:
    st.session_state.selected_system = None

# 2. HEADER
st.markdown(
    "<div style='padding:1rem 0 0.4rem 0;'>"
    "<h1 style='font-size:2rem;font-weight:700;color:#1a1a2e;margin-bottom:0.3rem;'>"
    "SignalPath AI Governance Center</h1>"
    "<p style='font-size:0.92rem;color:#444;line-height:1.55;margin-bottom:0.4rem;'>"
    "SignalPath, a fictional Deaf Services company, captures the exact regulatory pressure "
    "real accessibility tech faces right now. AI governance isn't paperwork &mdash; it's an "
    "operational system you can monitor, filter, and stress-test.</p>"
    "<p style='font-size:0.78rem;color:#888;margin:0;'>"
    "Built by&nbsp;"
    "<a href='https://github.com/datadynamo-hub' target='_blank' "
    "style='color:#555;text-decoration:none;border-bottom:1px solid #ccc;'>Jon Khan</a>"
    "&nbsp;&middot;&nbsp;"
    "<a href='https://www.linkedin.com/in/jonathan-k-184393120/' target='_blank' "
    "style='color:#555;text-decoration:none;border-bottom:1px solid #ccc;'>LinkedIn</a>"
    "</p></div>",
    unsafe_allow_html=True
)

# 3. GOVERNANCE SANDBOX BANNER
st.info("Governance Sandbox: All telemetry and control data displayed is simulated in real-time to demonstrate system capabilities and automated guardrails.")
st.markdown("---")

# 4. NAVIGATION
col_n1, col_n2, col_n3 = st.columns(3)
with col_n1:
    if st.button("Operational Command Center", use_container_width=True,
                 type="primary" if st.session_state.view == "Command Center" else "secondary"):
        st.session_state.view = "Command Center"
        st.rerun()
with col_n2:
    if st.button("Active Registry Inventory", use_container_width=True,
                 type="primary" if st.session_state.view == "Registry" else "secondary"):
        st.session_state.view = "Registry"
        st.rerun()
with col_n3:
    if st.button("Regulatory Framework Mapping", use_container_width=True,
                 type="primary" if st.session_state.view == "Docs" else "secondary"):
        st.session_state.view = "Docs"
        st.rerun()

st.markdown("##")

# 5. DATA LOADING
BASE_PATH = "project-01-ai-system-inventory"

@st.cache_data
def load_inventory_data():
    excel_path = os.path.join(BASE_PATH, "ai-system-inventory-signalpath.xlsx")
    df = pd.read_excel(excel_path, engine="openpyxl")
    df.columns = [col.strip() for col in df.columns]
    return df

try:
    df_raw = load_inventory_data()
except Exception as e:
    st.error(f"Error loading inventory file: {e}")
    st.stop()

# 6. SIDEBAR
st.sidebar.markdown("### Registry Filters")
st.sidebar.markdown("---")

has_bu     = "business_unit"       in df_raw.columns
has_tier   = "eu_ai_act_risk_tier"  in df_raw.columns
has_status = "deployment_status"    in df_raw.columns

all_bus      = sorted(df_raw["business_unit"].dropna().unique())       if has_bu     else []
all_tiers    = sorted(df_raw["eu_ai_act_risk_tier"].dropna().unique())  if has_tier   else []
all_statuses = sorted(df_raw["deployment_status"].dropna().unique())    if has_status else []

if has_bu:
    bu_choice   = st.sidebar.selectbox("Active Business Unit", options=["All Units"] + all_bus)
    selected_bu = all_bus if bu_choice == "All Units" else [bu_choice]
else:
    selected_bu = []

st.sidebar.markdown("##")

if has_tier:
    all_tiers_active = st.sidebar.checkbox("All Risk Tiers", value=True)
    selected_tier    = all_tiers if all_tiers_active else st.sidebar.multiselect("Select Risk Tiers", options=all_tiers)
else:
    selected_tier = []

st.sidebar.markdown("##")

if has_status:
    all_status_active = st.sidebar.checkbox("All Deployment Statuses", value=True)
    selected_status   = all_statuses if all_status_active else st.sidebar.multiselect("Select Deployment Statuses", options=all_statuses)
else:
    selected_status = []

mask = pd.Series(True, index=df_raw.index)
if has_bu     and selected_bu:     mask &= df_raw["business_unit"].isin(selected_bu)
if has_tier   and selected_tier:   mask &= df_raw["eu_ai_act_risk_tier"].isin(selected_tier)
if has_status and selected_status: mask &= df_raw["deployment_status"].isin(selected_status)

df_filtered = df_raw[mask].copy()
is_empty    = df_filtered.empty

# 7. SHARED SYSTEM LIST
system_options = (
    df_filtered["system_name"].tolist()
    if "system_name" in df_filtered.columns and not is_empty else []
)
if system_options:
    if st.session_state.selected_system not in system_options:
        st.session_state.selected_system = system_options[0]
else:
    st.session_state.selected_system = None

def get_system_profile(system_name):
    if system_name is None or is_empty or "system_name" not in df_filtered.columns:
        return None
    matches = df_filtered[df_filtered["system_name"] == system_name]
    return matches.iloc[0] if not matches.empty else None

def get_field(profile, field_name):
    if profile is None:
        return "*Under Review*"
    val = profile.get(field_name, None)
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return "*Not yet defined*" if field_name == "mitigation_strategy" else "*Under Review*"
    text = str(val).strip()
    if text == "" or text.lower() == "nan":
        return "*Not yet defined*" if field_name == "mitigation_strategy" else "*Under Review*"
    return text


# 8. SYSTEM CONTROLS — per-system breach, guardrail, SLA, and escalation text
SYSTEM_CONTROLS = {
    "SP-AI-001": {
        "breach_vector": "Spatial tracking degradation in localized extremity nodes (Digit 5 Occlusion Anomaly). Computer vision confidence below structural validation baseline.",
        "guardrail": "ASL interpretation pipeline isolated. Live call traffic hot-swapped to standby human interpreter stream (0ms latency).",
        "target_metric": "Computer-vision confidence >= 94%",
        "response_sla": "0ms (immediate hot-swap)",
        "escalation_1": "P1 Incident payload routed via API webhook to PagerDuty/MLOps On-Call Engineer (Instant Page)",
        "escalation_2": "FCC compliance log created -- interpreter service continuity event recorded in GRC Registry",
    },
    "SP-AI-002": {
        "breach_vector": "Real-time transcription accuracy degraded. Word Error Rate exceeds 5% threshold for Deaf user communication.",
        "guardrail": "Caption generation pipeline suspended. Session flagged for manual review; user notified of service interruption.",
        "target_metric": "Word Error Rate <= 5%",
        "response_sla": "1 hour",
        "escalation_1": "P2 Alert routed to CaptionLine Operations team (1-hour review window)",
        "escalation_2": "ADA compliance event logged -- captioning accuracy incident recorded in GRC Registry",
    },
    "SP-AI-003": {
        "breach_vector": "Interpreter-to-caller matching failure rate exceeded threshold. ML routing model producing suboptimal assignments below 95% success rate.",
        "guardrail": "ML routing suspended. Call queue reverted to manual dispatcher assignment protocol.",
        "target_metric": "Interpreter-caller matching success >= 95%",
        "response_sla": "2 hours",
        "escalation_1": "P2 Alert sent to Call Operations Management (2-hour review window)",
        "escalation_2": "SLA compliance event logged in GRC Registry -- routing degradation incident recorded",
    },
    "SP-AI-004": {
        "breach_vector": "Caption accuracy below FCC Part 64 functional equivalency standard. Home user communication accuracy compromised below 99% threshold.",
        "guardrail": "Automated captioning suspended. FCC-mandated manual captioning backup activated immediately.",
        "target_metric": "Caption accuracy >= 99% (FCC Part 64 standard)",
        "response_sla": "30 minutes",
        "escalation_1": "P1 FCC compliance alert -- functional equivalency breach notification to Regulatory Affairs (30-min window)",
        "escalation_2": "FCC Part 64 compliance event logged; regulatory disclosure timeline initiated in GRC Registry",
    },
    "SP-AI-005": {
        "breach_vector": "AI-generated content accuracy degradation detected across M365 workflows. Output reliability below 90% acceptable threshold.",
        "guardrail": "Copilot AI suggestions suspended for affected accounts. Users redirected to standard M365 manual workflow.",
        "target_metric": "Output accuracy >= 90% across M365 workloads",
        "response_sla": "4 hours",
        "escalation_1": "P3 IT Operations alert -- Copilot service degradation notification sent (4-hour review window)",
        "escalation_2": "Productivity impact event logged; data governance audit trail preserved in GRC Registry",
    },
    "SP-AI-006": {
        "breach_vector": "HR analytics and staffing prediction accuracy below threshold. Interpreter workforce optimization outputs exceeding +/-10% forecast variance.",
        "guardrail": "AI-generated staffing recommendations suspended. HR decisions reverted to manual analyst review workflow.",
        "target_metric": "Forecast accuracy within +/-10% of actual staffing needs",
        "response_sla": "24 hours",
        "escalation_1": "P2 HR Operations alert -- Workday AI degradation notification to HR Systems team (24-hour review window)",
        "escalation_2": "Workforce management incident logged; HR compliance audit trail preserved in GRC Registry",
    },
    "SP-AI-007": {
        "breach_vector": "Scheduling model producing compliance-violating shift assignments. Demand forecasting accuracy degraded; labor law violation risk elevated.",
        "guardrail": "Automated shift generation suspended. Manual scheduling review required before any shift deployment.",
        "target_metric": "Zero compliance-violating shift assignments",
        "response_sla": "12 hours (before next shift boundary)",
        "escalation_1": "P2 Operations alert -- UKG AI degradation notification to Workforce Management team (12-hour window)",
        "escalation_2": "Labor compliance event logged -- scheduling audit trail preserved in GRC Registry",
    },
    "SP-AI-008": {
        "breach_vector": "Support ticket misclassification rate exceeds 5% threshold. Deaf/HoH accessibility requests at risk of incorrect routing.",
        "guardrail": "AI triage suspended. All incoming tickets routed to human support queue for manual classification.",
        "target_metric": "Ticket classification accuracy >= 95% for Deaf/HoH queues",
        "response_sla": "1 hour",
        "escalation_1": "P2 Customer Support alert -- Zendesk AI degradation notification (1-hour review window)",
        "escalation_2": "Customer experience event logged; accessibility support continuity tracked in GRC Registry",
    },
    "SP-AI-009": {
        "breach_vector": "AI-generated proposal content accuracy below threshold. Compliance claims and technical specifications unreliable; bid integrity at risk.",
        "guardrail": "Automated RFP generation suspended. All proposals flagged for mandatory human legal and technical review before submission.",
        "target_metric": "Compliance-claim accuracy >= 95%",
        "response_sla": "24 hours",
        "escalation_1": "P2 Sales Operations alert -- RFP content accuracy degradation notification (24-hour review window)",
        "escalation_2": "Contract risk event logged; proposal audit trail preserved in GRC Registry",
    },
    "SP-AI-010": {
        "breach_vector": "Lead scoring and contact data accuracy degradation. Lead-score correlation with conversion below 0.7 threshold; pipeline prioritization unreliable.",
        "guardrail": "AI-generated lead scores suspended. Sales team notified to revert to manual prospecting validation.",
        "target_metric": "Lead-score correlation with conversion > 0.7",
        "response_sla": "4 hours",
        "escalation_1": "P3 Sales Operations alert -- ZoomInfo AI data quality degradation notification (4-hour review window)",
        "escalation_2": "Data accuracy event logged; CCPA/GDPR compliance audit trail preserved in GRC Registry",
    },
    "SP-AI-011": {
        "breach_vector": "Sales call analysis accuracy degradation detected. Coaching recommendation accuracy below 85% threshold; pipeline insights unreliable.",
        "guardrail": "AI-generated coaching flags suspended. Active pipeline analysis paused pending manual review.",
        "target_metric": "Coaching recommendation accuracy >= 85%",
        "response_sla": "2 hours",
        "escalation_1": "P3 Sales Leadership alert -- Gong AI degradation notification (2-hour review window)",
        "escalation_2": "Data handling event logged; call recording compliance audit preserved in GRC Registry",
    },
    "SP-AI-012": {
        "breach_vector": "Code suggestion quality degradation detected. CVSS vulnerability score exceeds 3.9 (Low severity) threshold; security risk elevated in AI-generated code.",
        "guardrail": "GitHub Copilot suggestions disabled across all active repositories. Engineering team notified to conduct manual security review of recent AI-generated code.",
        "target_metric": "CVSS vulnerability score <= 3.9 (Low severity)",
        "response_sla": "4 hours",
        "escalation_1": "P2 Engineering Security alert -- Copilot code quality degradation; manual commit review initiated (4-hour window)",
        "escalation_2": "Code security event logged; engineering compliance audit trail preserved in GRC Registry",
    },
    "SP-AI-013": {
        "breach_vector": "Legal research accuracy and contract analysis confidence below 98% threshold. Regulatory filing review outputs unreliable; legal exposure risk elevated.",
        "guardrail": "Harvey AI outputs suspended. All active legal matters escalated to manual outside counsel review immediately.",
        "target_metric": "Legal-research accuracy >= 98%",
        "response_sla": "4 hours",
        "escalation_1": "P1 Legal Operations alert -- Harvey AI accuracy degradation; outside counsel notified immediately (4-hour window)",
        "escalation_2": "Legal risk event logged; attorney-client privilege and compliance audit trail preserved in GRC Registry",
    },
    "SP-AI-014": {
        "breach_vector": "Regulatory change detection accuracy degradation below 99% threshold. FCC filings and rule changes at risk of missed alerting.",
        "guardrail": "Automated regulatory monitoring suspended. Manual FCC docket review assigned to Regulatory Affairs team immediately.",
        "target_metric": "Regulatory-change detection accuracy >= 99%",
        "response_sla": "1 hour",
        "escalation_1": "P1 Regulatory Affairs alert -- FCC monitoring degradation; manual docket review protocol activated (1-hour window)",
        "escalation_2": "Regulatory compliance event logged; FCC monitoring gap documented in GRC Registry",
    },
    "SP-AI-015": {
        "breach_vector": "Threat detection accuracy below acceptable threshold. False-negative rate exceeds 1%; security anomalies at risk of suppression or misclassification.",
        "guardrail": "AI threat scoring suspended. Security Operations Center (SOC) placed on 24/7 manual monitoring protocol immediately.",
        "target_metric": "False-negative rate <= 1%",
        "response_sla": "1 hour",
        "escalation_1": "P1 SOC alert -- Sentinel AI degradation; 24/7 manual monitoring activated immediately (1-hour window)",
        "escalation_2": "Security incident event logged; SOC compliance and incident response audit trail preserved in GRC Registry",
    },
    "SP-AI-016": {
        "breach_vector": "Unauthorized AI tool processing detected on corporate or Deaf community personal data. Data exfiltration risk score elevated; PII breach protocol triggered.",
        "guardrail": "Network traffic to unauthorized AI endpoints blocked immediately. Affected user sessions flagged for HR and Legal review. Review initiated within 1 hour.",
        "target_metric": "Unauthorized AI endpoint detection rate >= 95%",
        "response_sla": "1 hour (traffic blocked; joint HR/Legal review initiated)",
        "escalation_1": "P1 Security and Legal alert -- Shadow AI data exposure event; immediate investigation protocol activated (1-hour window)",
        "escalation_2": "Data privacy incident logged; GDPR/CCPA breach assessment timeline initiated in GRC Registry",
    },
}

DEFAULT_CONTROLS = {
    "breach_vector": "Performance degradation detected. Model outputs below acceptable threshold.",
    "guardrail": "System pipeline isolated. Traffic rerouted to manual review workflow.",
    "target_metric": "System-specific performance threshold",
    "response_sla": "4 hours",
    "escalation_1": "P2 Incident payload routed to On-Call Engineer",
    "escalation_2": "Compliance tracking payload pushed to GRC Registry",
}

# 9. DYNAMIC BANNER
BANNERS = {
    "Command Center": "**Operational Command Center** - Continuous Control Telemetry Active",
    "Registry":       "**Active Registry Inventory** - System Registry Tab Active",
    "Docs":           "**Regulatory Framework Mapping** - Regulatory Alignment Mapping Tab Active",
}
st.info(BANNERS[st.session_state.view])

# 9. COMMAND CENTER VIEW
if st.session_state.view == "Command Center":

    with st.expander("Click here for a video walkthrough of this project architecture"):
        st.write("Video walkthrough coming soon.")

    st.write("##")

    total_systems       = len(df_filtered)
    high_critical_count = 0
    avg_maturity        = "N/A"

    if not is_empty:
        if "eu_ai_act_risk_tier" in df_filtered.columns:
            high_critical_count = len(df_filtered[
                df_filtered["eu_ai_act_risk_tier"].astype(str).str.strip().str.lower()
                .isin(["high", "high risk", "high-risk", "critical", "unacceptable", "unacceptable risk"])
            ])
        if "nist_rmf_maturity_level" in df_filtered.columns:
            valid_mat = pd.to_numeric(df_filtered["nist_rmf_maturity_level"], errors="coerce").dropna()
            if not valid_mat.empty:
                avg_maturity = f"{valid_mat.mean():.1f} / 5.0"

    mc1, mc2, mc3, mc4 = st.columns(4)
    with mc1:
        with st.container(border=True):
            st.metric("Centralized Oversight",
                      f"{total_systems} AI Systems" if not is_empty else "0 Systems",
                      f"{len(df_raw)} Total Tracked")
    with mc2:
        with st.container(border=True):
            st.metric("Audit Prep Efficiency", "-88%", "From Weeks to Hours")
    with mc3:
        with st.container(border=True):
            st.metric("High/Critical Risk Vectors", high_critical_count,
                      "Prioritized for Mitigation", delta_color="inverse")
    with mc4:
        with st.container(border=True):
            st.metric("Avg NIST Maturity Level", avg_maturity, "Continuous Improvement Target")

    st.write("##")

    # System selector synced across tabs
    if system_options:
        cur_idx = system_options.index(st.session_state.selected_system) if st.session_state.selected_system in system_options else 0
        chosen  = st.selectbox("Active System - Live Control Target:", options=system_options, index=cur_idx, key="cc_sys")
        if chosen != st.session_state.selected_system:
            st.session_state.selected_system = chosen
            st.rerun()

    ap      = get_system_profile(st.session_state.selected_system)
    ap      = get_system_profile(st.session_state.selected_system)
    s_name  = get_field(ap, "system_name")
    s_id    = get_field(ap, "system_id")
    s_purp  = get_field(ap, "primary_purpose")
    ctrl    = SYSTEM_CONTROLS.get(s_id, DEFAULT_CONTROLS)

    with st.container(border=True):
        st.markdown(f"### Live Control Monitor: {s_name} ({s_id})")
        st.markdown(f"**Control Loop Target:** {s_purp}")
        st.markdown("---")
        c1, c2 = st.columns([1, 2])
        with c1:
            score = st.slider("Simulated Ingestion Model Confidence Score (%)", 0, 100, 85, 1,
                              help="75% is the engineered Lower Control Limit (LCL). Drop below to trigger the safety interlock.")
            st.caption(f"Target: {ctrl['target_metric']}  |  Response SLA: {ctrl['response_sla']}")
        with c2:
            if score < 75:
                st.error(
                    f"CRITICAL EXCEPTION: Model Confidence at {score}% (LCL <75%)\n\n"
                    f"Breach Vector: {ctrl['breach_vector']}\n\n"
                    f"Automated Guardrail (0ms): {ctrl['guardrail']}\n\n"
                    f"Response SLA: {ctrl['response_sla']}"
                )
                st.warning(
                    f"Incident Escalation Logs:\n"
                    f"* Technical Alert: {ctrl['escalation_1']}\n"
                    f"* Audit Log: {ctrl['escalation_2']}"
                )
            else:
                st.success(
                    f"Continuous Control Operating Effectively ({score}%)\n\n"
                    "Model tracking parameters within baseline statistical variances. "
                    "No human-in-the-loop interlocks required.\n\n"
                    f"Target: {ctrl['target_metric']}"
                )


# 10. REGISTRY VIEW
elif st.session_state.view == "Registry":

    st.markdown("### Active Systems Risk Register")

    if is_empty:
        st.info("No AI systems match the current sidebar filter parameters. Adjust your selections to review data.")
    else:
        risk_map = {
            "unacceptable risk": "Unacceptable Risk", "unacceptable": "Unacceptable Risk", "critical": "Unacceptable Risk",
            "high risk": "High Risk", "high": "High Risk", "high-risk": "High Risk",
            "limited risk": "Limited Risk", "specific transparency": "Limited Risk", "medium risk": "Limited Risk", "medium": "Limited Risk",
            "minimal risk": "Minimal Risk", "minimal": "Minimal Risk", "low risk": "Minimal Risk", "low": "Minimal Risk",
        }
        if "eu_ai_act_risk_tier" in df_filtered.columns:
            df_filtered["Risk Priority"] = (
                df_filtered["eu_ai_act_risk_tier"].astype(str).str.strip().str.lower()
                .map(risk_map).fillna(df_filtered["eu_ai_act_risk_tier"])
            )

        vis_cols = [c for c in ["system_id","system_name","business_unit","Risk Priority","deployment_status","category"] if c in df_filtered.columns]
        col_cfg  = {
            "system_id":         st.column_config.TextColumn("ID",               width="small"),
            "system_name":       st.column_config.TextColumn("System Name",       width="medium"),
            "business_unit":     st.column_config.TextColumn("Business Unit",     width="medium"),
            "Risk Priority":     st.column_config.TextColumn("Risk Tier",         width="medium"),
            "deployment_status": st.column_config.TextColumn("Deployment Status", width="medium"),
            "category":          st.column_config.TextColumn("Category",          width="medium"),
        }
        st.dataframe(df_filtered[vis_cols], column_config=col_cfg, use_container_width=True, hide_index=True)

        st.write("##")

        if system_options:
            cur_idx = system_options.index(st.session_state.selected_system) if st.session_state.selected_system in system_options else 0
            chosen  = st.selectbox("Select an inventory asset to review its full enterprise profile:",
                                   options=system_options, index=cur_idx, key="reg_sys")
            if chosen != st.session_state.selected_system:
                st.session_state.selected_system = chosen
                st.rerun()

            rp = get_system_profile(st.session_state.selected_system)
            if rp is not None:
                with st.container(border=True):
                    st.markdown(f"#### Governance Profile: {st.session_state.selected_system}")
                    st.markdown("---")
                    cl, cr = st.columns(2)
                    with cl:
                        st.markdown("**Primary Purpose:** " + get_field(rp, "primary_purpose"))
                        st.markdown("**Description:** "     + get_field(rp, "description"))
                        st.markdown("**Data Inputs:** "     + get_field(rp, "data_inputs"))
                        st.markdown("**Outputs:** "         + get_field(rp, "outputs"))
                        st.markdown("**Geographic Scope:** "+ get_field(rp, "geographic_scope"))
                    with cr:
                        st.markdown("**System Owner:** "        + get_field(rp, "system_owner"))
                        st.markdown("**Sourcing Origin:** "     + get_field(rp, "vendor_or_internal"))
                        st.markdown("**Affected Persons:** "    + get_field(rp, "affected_persons"))
                        st.markdown("**NIST RMF Maturity:** "   + get_field(rp, "nist_rmf_maturity_level"))
                        st.markdown("**FCC Exposure:** "        + get_field(rp, "fcc_regulatory_exposure"))
                    st.markdown("---")
                    st.markdown("**Mitigation Strategy:**\n\n" + get_field(rp, "mitigation_strategy"))
                    st.markdown("*Audit Notes:* "              + get_field(rp, "notes"))

# 11. DOCS VIEW
elif st.session_state.view == "Docs":

    st.markdown("### Compliance Documentation Baselines")
    tab1, tab2 = st.tabs(["EU AI Act Classification Framework", "NIST RMF Mapping Core"])

    with tab1:
        try:
            with open(os.path.join(BASE_PATH, "eu-ai-act-classification-signalpath.md"), "r", encoding="utf-8", errors="ignore") as f:
                st.markdown(f.read())
        except Exception as e:
            st.error(f"Could not load EU AI Act document: {e}")

    with tab2:
        try:
            with open(os.path.join(BASE_PATH, "nist-rmf-mapping-signalpath.md"), "r", encoding="utf-16", errors="ignore") as f:
                st.markdown(f.read())
        except Exception as e:
            st.error(f"Could not load NIST RMF document: {e}")
