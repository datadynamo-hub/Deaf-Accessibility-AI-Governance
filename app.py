import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go

# ─────────────────────────────────────────────
# 1. PAGE CONFIG & SESSION STATE
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="SignalPath AI Governance Center",
    page_icon=":shield:",
    layout="wide"
)

if "view" not in st.session_state:
    st.session_state.view = "Command Center"
if "selected_system" not in st.session_state:
    st.session_state.selected_system = None

# ─────────────────────────────────────────────
# 2. HEADER
# ─────────────────────────────────────────────
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
    "&nbsp;&middot;&nbsp;Forked from&nbsp;"
    "<a href='https://github.com/taimur-ijlal' target='_blank' "
    "style='color:#555;text-decoration:none;border-bottom:1px solid #ccc;'>Taimur Ijlal</a>"
    "'s AI governance framework"
    "</p></div>",
    unsafe_allow_html=True
)

# ─────────────────────────────────────────────
# 3. SANDBOX BANNER
# ─────────────────────────────────────────────
st.info("Governance Sandbox: All telemetry and control data displayed is simulated in real-time to demonstrate system capabilities and automated guardrails.")
st.markdown("---")

# ─────────────────────────────────────────────
# 4. NAVIGATION
# ─────────────────────────────────────────────
col_n1, col_n2, col_n3, col_n4, col_n5 = st.columns(5)
with col_n1:
    if st.button("Command Center", use_container_width=True,
                 type="primary" if st.session_state.view == "Command Center" else "secondary"):
        st.session_state.view = "Command Center"
        st.rerun()
with col_n2:
    if st.button("Registry", use_container_width=True,
                 type="primary" if st.session_state.view == "Registry" else "secondary"):
        st.session_state.view = "Registry"
        st.rerun()
with col_n3:
    if st.button("Risk Intelligence", use_container_width=True,
                 type="primary" if st.session_state.view == "Risk Intelligence" else "secondary"):
        st.session_state.view = "Risk Intelligence"
        st.rerun()
with col_n4:
    if st.button("Incident Response", use_container_width=True,
                 type="primary" if st.session_state.view == "Incident Response" else "secondary"):
        st.session_state.view = "Incident Response"
        st.rerun()
with col_n5:
    if st.button("Governance Hub", use_container_width=True,
                 type="primary" if st.session_state.view == "Gov Hub" else "secondary"):
        st.session_state.view = "Gov Hub"
        st.rerun()

st.markdown("##")

# ─────────────────────────────────────────────
# 5. PATH CONSTANTS
# ─────────────────────────────────────────────
DATA_PATH      = "data"
RISK_PATH      = os.path.join("content", "risk-assessment")
POLICY_PATH    = os.path.join("content", "policy")
INCIDENT_PATH  = os.path.join("content", "incident-response")
CONFORMITY_PATH = os.path.join("content", "conformity-pack")

# ─────────────────────────────────────────────
# 6. DATA LOADING
# ─────────────────────────────────────────────
@st.cache_data
def load_inventory_data():
    excel_path = os.path.join(DATA_PATH, "ai-system-inventory.xlsx")
    df = pd.read_excel(excel_path, engine="openpyxl")
    df.columns = [col.strip() for col in df.columns]
    return df

try:
    df_raw = load_inventory_data()
except Exception as e:
    st.error(f"Error loading inventory file: {e}")
    st.stop()

# ─────────────────────────────────────────────
# 7. SIDEBAR FILTERS
# ─────────────────────────────────────────────
st.sidebar.markdown("### Registry Filters")
st.sidebar.markdown("---")

has_bu     = "business_unit"        in df_raw.columns
has_tier   = "eu_ai_act_risk_tier"  in df_raw.columns
has_status = "deployment_status"    in df_raw.columns

all_bus      = sorted(df_raw["business_unit"].dropna().unique())       if has_bu     else []
all_tiers    = sorted(df_raw["eu_ai_act_risk_tier"].dropna().unique()) if has_tier   else []
all_statuses = sorted(df_raw["deployment_status"].dropna().unique())   if has_status else []

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

# ─────────────────────────────────────────────
# 8. SHARED SYSTEM HELPERS
# ─────────────────────────────────────────────
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

# ─────────────────────────────────────────────
# 9. SYSTEM CONTROLS (per-system breach/guardrail data)
# ─────────────────────────────────────────────
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

# ─────────────────────────────────────────────
# 10. DYNAMIC BANNER
# ─────────────────────────────────────────────
BANNERS = {
    "Command Center":   "**Operational Command Center**: Continuous Control Telemetry Active",
    "Registry":         "**Active Registry Inventory**: System Registry Active",
    "Risk Intelligence":"**Risk Intelligence**: SP-AI-001 Deep-Dive Risk Analysis",
    "Incident Response":"**Incident Response Simulator**: SP-AI-001 Skin Tone Disparity Incident Walkthrough",
    "Gov Hub":          "**Governance Documentation Hub**: Policy and Compliance Library",
}
st.info(BANNERS[st.session_state.view])

# ─────────────────────────────────────────────
# 11. COMMAND CENTER VIEW
# ─────────────────────────────────────────────
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

    if system_options:
        cur_idx = system_options.index(st.session_state.selected_system) if st.session_state.selected_system in system_options else 0
        chosen  = st.selectbox("Active System: Live Control Target:", options=system_options, index=cur_idx, key="cc_sys")
        if chosen != st.session_state.selected_system:
            st.session_state.selected_system = chosen
            st.rerun()

    ap     = get_system_profile(st.session_state.selected_system)
    s_name = get_field(ap, "system_name")
    s_id   = get_field(ap, "system_id")
    s_purp = get_field(ap, "primary_purpose")
    ctrl   = SYSTEM_CONTROLS.get(s_id, DEFAULT_CONTROLS)

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

# ─────────────────────────────────────────────
# 12. REGISTRY VIEW
# ─────────────────────────────────────────────
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

# ─────────────────────────────────────────────
# 13. RISK INTELLIGENCE VIEW
# ─────────────────────────────────────────────
elif st.session_state.view == "Risk Intelligence":

    st.markdown("### SP-AI-001 Risk Analysis: SignalPath Interpret")
    st.markdown(
        "The risk assessment below covers SignalPath Interpret (SP-AI-001), "
        "SignalPath's real-time ASL interpretation AI for Video Relay Service calls. "
        "This is a pre-production governance gate assessment. Six risks were evaluated before any production deployment. "
        "The heat map shows both inherent risk (before controls) and residual risk (after controls are applied)."
    )

    # Risk data — sourced from risk-assessment.md
    RISKS = {
        "RISK-001": {
            "label": "RISK-001",
            "name": "Signer Variation & Demographic Bias",
            "inherent_l": 4, "inherent_i": 4, "inherent_score": 16, "inherent_level": "High",
            "residual_l": 2, "residual_i": 4, "residual_score": 8, "residual_level": "Medium",
            "summary": "Training data skewed toward narrow signer demographics produces systematic failures for users with physical limitations, regional dialect variation, non-native ASL, oral Deaf users, and older signers.",
            "control_owner": "Chief Product Officer and AI Governance Program Office",
        },
        "RISK-002": {
            "label": "RISK-002",
            "name": "Emergency Call Failure: No Human Override Architecture",
            "inherent_l": 3, "inherent_i": 5, "inherent_score": 15, "inherent_level": "High",
            "residual_l": 2, "residual_i": 3, "residual_score": 6, "residual_level": "Low",
            "summary": "No human-in-the-loop architecture defined for emergency relay calls. Misinterpretation during a 911 relay with no override path is a life-safety event and a direct FCC Part 64 violation.",
            "control_owner": "Chief Product Officer and Head of VRS Operations",
        },
        "RISK-003": {
            "label": "RISK-003",
            "name": "No Conformity Assessment Before Production Deployment",
            "inherent_l": 5, "inherent_i": 4, "inherent_score": 20, "inherent_level": "Critical",
            "residual_l": 2, "residual_i": 4, "residual_score": 8, "residual_level": "Medium",
            "summary": "SP-AI-001 is classified High Risk under EU AI Act Annex III. No conformity assessment initiated. Deployment without conformity assessment is direct non-compliance regardless of US headquarters.",
            "control_owner": "AI Governance Program Office and General Counsel",
        },
        "RISK-004": {
            "label": "RISK-004",
            "name": "Biometric Data Processing Without Consent Framework",
            "inherent_l": 4, "inherent_i": 4, "inherent_score": 16, "inherent_level": "High",
            "residual_l": 2, "residual_i": 3, "residual_score": 6, "residual_level": "Low",
            "summary": "System processes hand shape, facial expression, and body position: biometric data under GDPR Article 9. No explicit consent framework or opt-out mechanism exists. Deaf users traveling internationally are covered by GDPR regardless of account origin.",
            "control_owner": "Chief Privacy Officer and Legal",
        },
        "RISK-005": {
            "label": "RISK-005",
            "name": "Deaf Community Excluded from Governance",
            "inherent_l": 5, "inherent_i": 3, "inherent_score": 15, "inherent_level": "High",
            "residual_l": 2, "residual_i": 3, "residual_score": 6, "residual_level": "Low",
            "summary": "No Deaf person holds a seat in the governance structure. Accuracy thresholds and failure mode priorities are set by people who have not experienced a failed interpretation in a medical appointment or 911 call. This is a governance risk, not a diversity statement.",
            "control_owner": "Chief Executive and AI Governance Program Office",
        },
        "RISK-006": {
            "label": "RISK-006",
            "name": "Model Accuracy Degradation After Deployment",
            "inherent_l": 3, "inherent_i": 3, "inherent_score": 9, "inherent_level": "Medium",
            "residual_l": 1, "residual_i": 3, "residual_score": 3, "residual_level": "Low",
            "summary": "ASL is a living language. A model trained on 2024 signing data will encounter patterns in 2026 and beyond that were not in training. Without ongoing monitoring the degradation goes undetected until users are harmed.",
            "control_owner": "Chief Product Officer and Engineering Lead",
        },
    }

    # Color helper
    def risk_color(score):
        if score >= 20: return "#d62728"   # Critical — red
        if score >= 15: return "#ff7f0e"   # High — orange
        if score >= 7:  return "#f7d060"   # Medium — yellow
        return "#2ca02c"                    # Low — green

    def risk_bg(score):
        if score >= 20: return "#fff0f0"
        if score >= 15: return "#fff4e6"
        if score >= 7:  return "#fffbe6"
        return "#f0fff4"

    st.write("##")
    view_mode = st.radio("Risk Position", ["Inherent Risk (before controls)", "Residual Risk (after controls)"],
                         horizontal=True)
    show_residual = "Residual" in view_mode

    # Build Plotly heat map
    # Background zone matrix (5x5, value = L*I for coloring)
    zone_z = [[i*l for l in range(1,6)] for i in range(1,6)]

    fig = go.Figure()

    # Colored background
    fig.add_trace(go.Heatmap(
        z=zone_z,
        x=[1,2,3,4,5],
        y=[1,2,3,4,5],
        colorscale=[
            [0.0,  "#e8f5e9"],  # 1  — green
            [0.24, "#c8e6c9"],  # 6  — green
            [0.25, "#fff9c4"],  # 7  — yellow
            [0.55, "#ffe082"],  # 14 — yellow
            [0.56, "#ffcc80"],  # 15 — orange
            [0.75, "#ff8a65"],  # 19 — orange
            [0.76, "#ef9a9a"],  # 20 — red
            [1.0,  "#b71c1c"],  # 25 — red
        ],
        showscale=False,
        hoverinfo="skip",
        zmin=1, zmax=25,
        opacity=0.6,
    ))

    # Risk points
    risk_list = list(RISKS.values())
    px = [r["residual_l"] if show_residual else r["inherent_l"] for r in risk_list]
    py = [r["residual_i"] if show_residual else r["inherent_i"] for r in risk_list]
    labels = [r["label"] for r in risk_list]
    scores = [r["residual_score"] if show_residual else r["inherent_score"] for r in risk_list]
    levels = [r["residual_level"] if show_residual else r["inherent_level"] for r in risk_list]
    names  = [r["name"] for r in risk_list]
    colors = [risk_color(s) for s in scores]
    hovers = [f"<b>{labels[i]}</b><br>{names[i]}<br>Likelihood: {px[i]} | Impact: {py[i]}<br>Score: {scores[i]}: {levels[i]}" for i in range(len(risk_list))]

    fig.add_trace(go.Scatter(
        x=px, y=py,
        mode="markers+text",
        marker=dict(size=28, color=colors, line=dict(width=2, color="white")),
        text=labels,
        textposition="middle center",
        textfont=dict(size=10, color="white", family="monospace"),
        hovertext=hovers,
        hoverinfo="text",
    ))

    fig.update_layout(
        xaxis=dict(title="Likelihood (1–5)", tickvals=[1,2,3,4,5], range=[0.5,5.5], gridcolor="#eee"),
        yaxis=dict(title="Impact (1–5)", tickvals=[1,2,3,4,5], range=[0.5,5.5], gridcolor="#eee"),
        height=440,
        margin=dict(l=60, r=40, t=30, b=60),
        plot_bgcolor="white",
        paper_bgcolor="white",
    )

    # Zone legend
    leg1, leg2, leg3, leg4 = st.columns(4)
    with leg1: st.markdown("<span style='background:#e8f5e9;padding:4px 10px;border-radius:4px;font-size:0.8rem;'>Low (1–6)</span>", unsafe_allow_html=True)
    with leg2: st.markdown("<span style='background:#fff9c4;padding:4px 10px;border-radius:4px;font-size:0.8rem;'>Medium (7–14)</span>", unsafe_allow_html=True)
    with leg3: st.markdown("<span style='background:#ffcc80;padding:4px 10px;border-radius:4px;font-size:0.8rem;'>High (15–19)</span>", unsafe_allow_html=True)
    with leg4: st.markdown("<span style='background:#ef9a9a;padding:4px 10px;border-radius:4px;font-size:0.8rem;'>Critical (20–25)</span>", unsafe_allow_html=True)

    st.plotly_chart(fig, use_container_width=True)

    # Risk detail panel
    st.write("##")
    st.markdown("#### Risk Detail")
    selected_risk_key = st.selectbox(
        "Select a risk to review:",
        options=list(RISKS.keys()),
        format_func=lambda k: f"{k}: {RISKS[k]['name']}"
    )
    rd = RISKS[selected_risk_key]
    score_show = rd["residual_score"] if show_residual else rd["inherent_score"]
    level_show = rd["residual_level"] if show_residual else rd["inherent_level"]
    bg = risk_bg(score_show)

    with st.container(border=True):
        st.markdown(f"<div style='background:{bg};padding:1rem;border-radius:6px;'>", unsafe_allow_html=True)
        hc1, hc2, hc3 = st.columns(3)
        with hc1: st.metric("Risk Score", score_show)
        with hc2: st.metric("Risk Level", level_show)
        with hc3: st.metric("Control Owner", rd["control_owner"][:35] + "...")
        st.markdown(f"**{rd['name']}**")
        st.markdown(rd["summary"])
        st.markdown("</div>", unsafe_allow_html=True)

    # Governance memo
    st.write("##")
    with st.expander("Board Governance Review Memo: SP-AI-001 Deployment Decision"):
        try:
            with open(os.path.join(RISK_PATH, "governance-review-memo.md"), "r", encoding="utf-8", errors="ignore") as f:
                st.markdown(f.read())
        except Exception as e:
            st.error(f"Could not load governance memo: {e}")

# ─────────────────────────────────────────────
# 14. INCIDENT RESPONSE VIEW
# ─────────────────────────────────────────────
elif st.session_state.view == "Incident Response":

    st.markdown("### Incident Response Simulator: SP-INC-2026-001")

    with st.container(border=True):
        st.markdown(
            "**What triggered this incident:** In the Operational Command Center, the Live Control Monitor "
            "tracks SP-AI-001's real-time confidence score. Demographic monitoring revealed a systematic "
            "confidence gap correlated with skin tone. This disparity was invisible to aggregate metrics. "
            "This walkthrough shows what a well-governed organization does when that signal fires."
        )

    st.write("##")

    PHASES = [
        "Phase 0: Detection",
        "Phase 1: Triage",
        "Phase 2: Containment",
        "Phase 3: Investigation",
        "Phase 4: Remediation Planning",
        "Phase 5: Regulatory Reporting",
        "Phase 6: Post-Incident Review",
    ]

    selected_phase = st.select_slider("Incident Phase", options=PHASES)
    phase_idx = PHASES.index(selected_phase)

    st.write("##")

    PHASE_CONTENT = [
        {
            "title": "Phase 0: Detection",
            "timeframe": "Day 1 · 4 May 2026",
            "trigger": "Deaf Community Advisory Panel member report",
            "description": (
                "A Deaf Community Advisory Panel member submits a written report to the AI Governance Program Office (AGPO). "
                "She and several members of her network (all SP-AI-001 POC participants) have been experiencing elevated interpretation errors. "
                "The errors are not random: they are concentrated in the same group of users. The report reaches the AGPO on a Sunday. "
                "Engineering is tasked with log analysis for Monday morning."
            ),
            "key_decision": "AGPO prioritizes the report for immediate triage rather than routing it through standard intake. The Advisory Panel's governance role means its reports are treated as first-tier signals, not complaints.",
            "notifications": "None yet. Triage first.",
            "governance_log": "Advisory Panel report SP-2026-0504-001 received and logged. Engineering triage initiated.",
        },
        {
            "title": "Phase 1: Triage",
            "timeframe": "Days 2–3 · 5–6 May 2026",
            "trigger": "Engineering confidence score analysis",
            "description": (
                "Engineering pulls confidence score logs and segments them by video luminance proxy. "
                "The result is unambiguous: users in the lower luminance quartile (darker skin tones) show confidence scores "
                "averaging 17 percentage points below the upper quartile. Their automatic human interpreter handoff rate is 3.2x higher. "
                "The AGPO classifies this as Severity 1 incident SP-INC-2026-001 on Day 3."
            ),
            "key_decision": "Severity 1 classification triggers the full incident response protocol: 24-hour CRO notification, 48-hour Board notification, Legal and Compliance immediate involvement.",
            "notifications": "Chief Risk Officer notified (Day 3, within 24h). General Counsel notified. Chief Privacy Officer notified. Chief Information Security Officer notified.",
            "governance_log": "Incident SP-INC-2026-001 created. Severity 1 declared. Incident document drafted and circulated internally.",
        },
        {
            "title": "Phase 2: Containment",
            "timeframe": "Day 4 · 7 May 2026",
            "trigger": "CRO approval of containment recommendation",
            "description": (
                "The AI interpretation pipeline is suspended for all POC calls. All VRS calls route to human interpreters. "
                "POC participants receive notification of a temporary service change, framed as a planned system review. "
                "Legal reviews all external communications language before send. "
                "Board Risk and Audit Committee Chair is notified by the Chief Risk Officer within the 48-hour requirement. "
                "An extraordinary AI Governance Committee session is scheduled for 9 May."
            ),
            "key_decision": "Full POC suspension rather than targeted suspension for affected users only. Rationale: the demographic boundary cannot be perfectly identified in real time; full suspension is the only way to ensure no affected user continues to receive degraded service.",
            "notifications": "Board Risk and Audit Committee Chair notified (within 48h). AI Governance Committee extraordinary session scheduled.",
            "governance_log": "SP-AI-001 pipeline suspended. Human interpreter routing activated across all POC calls. External communication sent to POC participants.",
        },
        {
            "title": "Phase 3: Investigation",
            "timeframe": "Weeks 1–3 · 9 May – 22 May 2026",
            "trigger": "AI Governance Committee extraordinary session approval of investigation plan",
            "description": (
                "Engineering conducts a full training dataset audit: skin tone distribution, luminance representation, demographic composition. "
                "An external AI fairness specialist is engaged and confirms the engineering finding. "
                "The Deaf Community Advisory Panel is briefed directly on the incident and raises a critical scope expansion: "
                "skin tone is one dimension; the training data likely has other unaudited demographic gaps including age-related hand morphology, "
                "physical limitation variation, and regional dialect representation. "
                "The external specialist's preliminary analysis supports the Panel's concern."
            ),
            "key_decision": "The AI Governance Committee accepts the Panel's expanded scope recommendation. The remediation will address comprehensive demographic representativeness, not only the skin tone disparity that triggered the incident.",
            "notifications": "Advisory Panel briefed (14 May). External specialist preliminary findings shared with Committee (21 May).",
            "governance_log": "Training dataset audit underway. External specialist engaged. Panel input documented and accepted by Committee. Expanded remediation scope approved.",
        },
        {
            "title": "Phase 4: Remediation Planning",
            "timeframe": "Weeks 4–5 · 25 May – 5 June 2026",
            "trigger": "Full investigation findings confirmed",
            "description": (
                "The AI Governance Committee approves a remediation plan addressing the full demographic scope. "
                "Supplemental training data collection will recruit consenting participants from underrepresented demographic groups "
                "across: skin tone, age-related hand morphology, physical limitation variation, BASL (Black American Sign Language) phonological features, "
                "regional dialect variation, and oral Deaf signer variation. "
                "The normalization algorithm will be redesigned and recalibrated on a demographically balanced evaluation set. "
                "Target for POC resumption: November 2026, contingent on independent fairness audit completion."
            ),
            "key_decision": "No deployment resumption without completed independent fairness audit across all demographic dimensions. The gate condition is completion, not commissioning. This is the exact gap the original governance structure failed to enforce.",
            "notifications": "Remediation plan shared with Advisory Panel. Chief Product Officer accountable for supplemental data collection timeline.",
            "governance_log": "Remediation plan approved by AI Governance Committee. Timelines documented. Monitoring framework demographic segmentation layer scheduled for operational readiness before POC resumption.",
        },
        {
            "title": "Phase 5: Regulatory Reporting",
            "timeframe": "Weeks 3–5 · 22 May – 5 June 2026",
            "trigger": "Legal and Compliance regulatory disclosure assessment complete",
            "description": (
                "Legal confirms regulatory disclosure obligations and the Chief Risk Officer approves notifications. "
                "FCC is notified of a potential functional equivalency concern under FCC Part 64: "
                "the system delivered systematically lower-quality interpretation to a segment of Deaf users. "
                "Assessment of EU AI Act Article 73 obligations is conducted: "
                "if any POC participants held EU data subject status during calls (Deaf users accessing VRS while traveling in the EU), "
                "this may constitute a serious incident requiring national authority notification. "
                "Illinois Biometric Information Privacy Act (BIPA) exposure is assessed for Illinois-resident POC participants."
            ),
            "key_decision": "Proactive FCC informal notification rather than waiting for a formal complaint. Rationale: the FCC functional equivalency standard was materially breached; proactive disclosure is more defensible than reactive compliance.",
            "notifications": "FCC informal notification submitted (22 May). EU AI Act Article 73 assessment ongoing. BIPA assessment in progress.",
            "governance_log": "Regulatory disclosure log created. FCC notification documented. EU AI Act and BIPA assessments recorded with owners and timelines.",
        },
        {
            "title": "Phase 6: Post-Incident Review",
            "timeframe": "Weeks 6–8 · 8–26 June 2026",
            "trigger": "Root cause analysis complete and approved",
            "description": (
                "The formal root cause analysis is completed using the Five Whys method. "
                "The root cause is identified: the gate condition for bias audit completion was insufficient. "
                "Requiring that an audit be commissioned (but not completed) allowed deployment to proceed while the exact failure mode the audit was designed to catch remained undetected. "
                "Five contributing factors are documented including: demographic monitoring not operational at POC launch, "
                "audit scope defined without Advisory Panel input, and training data composition undocumented. "
                "The corrective action plan is approved by the AI Governance Committee. "
                "The Advisory Panel receives a full incident summary including the impact of their own detection role."
            ),
            "key_decision": "Gate conditions are revised system-wide: 'bias audit commissioned' becomes 'bias audit completed with Panel-reviewed scope' for any deployment involving real users. This change applies to all future high-risk system reviews, not only SP-AI-001.",
            "notifications": "Full incident summary delivered to Advisory Panel (26 June). Board Risk and Audit Committee receives closure update.",
            "governance_log": "RCA approved by AI Governance Committee (19 June). Corrective action plan documented with owners and due dates. Lessons learned distributed to AI governance program.",
        },
    ]

    pc = PHASE_CONTENT[phase_idx]

    with st.container(border=True):
        st.markdown(f"### {pc['title']}")
        st.caption(f"Timeframe: {pc['timeframe']}  |  Trigger: {pc['trigger']}")
        st.markdown("---")
        st.markdown(pc["description"])

    st.write("##")
    dc1, dc2, dc3 = st.columns(3)
    with dc1:
        with st.container(border=True):
            st.markdown("**Key Decision**")
            st.markdown(pc["key_decision"])
    with dc2:
        with st.container(border=True):
            st.markdown("**Notifications Issued**")
            st.markdown(pc["notifications"])
    with dc3:
        with st.container(border=True):
            st.markdown("**Governance Log Entry**")
            st.markdown(pc["governance_log"])

    st.write("##")
    with st.expander("View Full Incident Scenario Document"):
        try:
            with open(os.path.join(INCIDENT_PATH, "incident-scenario.md"), "r", encoding="utf-8", errors="ignore") as f:
                st.markdown(f.read())
        except Exception as e:
            st.error(f"Could not load incident scenario: {e}")

    with st.expander("View Full Incident Timeline"):
        try:
            with open(os.path.join(INCIDENT_PATH, "incident-timeline.md"), "r", encoding="utf-8", errors="ignore") as f:
                st.markdown(f.read())
        except Exception as e:
            st.error(f"Could not load incident timeline: {e}")

    with st.expander("View Full Root Cause Analysis"):
        try:
            with open(os.path.join(INCIDENT_PATH, "root-cause-analysis.md"), "r", encoding="utf-8", errors="ignore") as f:
                st.markdown(f.read())
        except Exception as e:
            st.error(f"Could not load root cause analysis: {e}")

# ─────────────────────────────────────────────
# 15. GOVERNANCE HUB VIEW
# ─────────────────────────────────────────────
elif st.session_state.view == "Gov Hub":

    st.markdown("### Governance Documentation Hub")
    st.markdown(
        "SignalPath's AI governance library: responsible AI policy, operating model, review process, "
        "and regulatory framework documentation. These documents demonstrate organizational governance depth "
        "across EU AI Act, NIST AI RMF, FCC Part 64, and ADA Title IV."
    )

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Responsible AI Policy",
        "Governance Operating Model",
        "AI Review Process",
        "EU AI Act Classification",
        "NIST RMF Mapping",
        "EU AI Act Conformity Pack",
    ])

    with tab1:
        try:
            with open(os.path.join(POLICY_PATH, "responsible-ai-policy.md"), "r", encoding="utf-8", errors="ignore") as f:
                st.markdown(f.read())
        except Exception as e:
            st.error(f"Could not load Responsible AI Policy: {e}")

    with tab2:
        try:
            with open(os.path.join(POLICY_PATH, "governance-operating-model.md"), "r", encoding="utf-8", errors="ignore") as f:
                st.markdown(f.read())
        except Exception as e:
            st.error(f"Could not load Governance Operating Model: {e}")

    with tab3:
        try:
            with open(os.path.join(POLICY_PATH, "ai-review-process.md"), "r", encoding="utf-8", errors="ignore") as f:
                st.markdown(f.read())
        except Exception as e:
            st.error(f"Could not load AI Review Process: {e}")

    with tab4:
        try:
            with open(os.path.join(POLICY_PATH, "eu-ai-act-classification.md"), "r", encoding="utf-8", errors="ignore") as f:
                st.markdown(f.read())
        except Exception as e:
            st.error(f"Could not load EU AI Act Classification: {e}")

    with tab5:
        try:
            with open(os.path.join(POLICY_PATH, "nist-rmf-mapping.md"), "r", encoding="utf-16", errors="ignore") as f:
                st.markdown(f.read())
        except Exception as e:
            st.error(f"Could not load NIST RMF Mapping: {e}")

    with tab6:
        st.markdown("#### EU AI Act Conformity Pack: SP-AI-001 SignalPath Interpret")
        st.info(
            "The EU AI Act Conformity Pack documents SignalPath Interpret's compliance with EU AI Act "
            "Articles 9–17 for High Risk AI systems. This pack covers intended purpose, risk management, "
            "data governance, human oversight, logging and traceability, and performance monitoring. "
            "This section is under active development. See SESSION-HANDOFF-PROJECT5.md for the research architecture."
        )
        conformity_docs = [
            "01: Intended Purpose and System Description (Article 11, Annex IV)",
            "02: Risk Management Summary (Article 9)",
            "03: Data Governance (Article 10)",
            "04: Human Oversight Mechanisms (Article 14)",
            "05: Logging and Traceability (Article 12)",
            "06: Performance Monitoring Plan (Articles 15 + 17)",
        ]
        st.selectbox("Document", options=conformity_docs, disabled=True)
        st.caption("Conformity pack documents will appear here when Project 5 is complete.")
