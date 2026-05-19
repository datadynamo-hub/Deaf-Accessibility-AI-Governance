import streamlit as st
import pandas as pd
import os

# ==========================================
# 1. PAGE INITIALIZATION & GLOBAL STYLING
# ==========================================
st.set_page_config(
    page_title="SignalPath AI Operational Governance Center",
    page_icon="🛡️",
    layout="wide"
)

# Custom minimal CSS injection to clean up table padding and borders globally
st.markdown("""
    <style>
    [data-testid="stMetric"] {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #e9ecef;
    }
    div.stSlider > div[data-baseweb="slider"] {
        padding-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Executive Header Branding
st.markdown("# 🛡️ SignalPath AI Governance Center")
st.markdown("### *Unified GRC Engineering Portfolio Demo*")
st.caption("Continuous Control Telemetry • System Inventory Registry • Regulatory Alignment Mapping")

BASE_PATH = "project-01-ai-system-inventory"

# ==========================================
# 2. DATA INGESTION & PIPELINE INTEGRITY
# ==========================================
@st.cache_data
def load_inventory_data():
    excel_path = os.path.join(BASE_PATH, "ai-system-inventory-signalpath.xlsx")
    df = pd.read_excel(excel_path, engine="openpyxl")
    # Clean header trailing spaces automatically
    df.columns = [col.strip() for col in df.columns]
    return df

try:
    df_raw = load_inventory_data()
except Exception as e:
    st.error(f"Error loading inventory file: {e}")
    st.stop()

# ==========================================
# 3. GLOBAL SIDEBAR INTERACTIVE FILTERS
# ==========================================
st.sidebar.markdown("## ⚙️ Registry Filters")

has_bu = "business_unit" in df_raw.columns
has_tier = "eu_ai_act_risk_tier" in df_raw.columns
has_status = "deployment_status" in df_raw.columns

all_bus = sorted(df_raw["business_unit"].dropna().unique()) if has_bu else []
all_tiers = sorted(df_raw["eu_ai_act_risk_tier"].dropna().unique()) if has_tier else []
all_statuses = sorted(df_raw["deployment_status"].dropna().unique()) if has_status else []

selected_bu = st.sidebar.multiselect("Business Unit", options=all_bus, default=all_bus)
selected_tier = st.sidebar.multiselect("Regulatory Tier", options=all_tiers, default=all_tiers)
selected_status = st.sidebar.multiselect("Deployment Status", options=all_statuses, default=all_statuses)

# Generate bitwise mask for dynamic state intersection
mask = pd.Series(True, index=df_raw.index)
if has_bu and selected_bu:
    mask &= df_raw["business_unit"].isin(selected_bu)
if has_tier and selected_tier:
    mask &= df_raw["eu_ai_act_risk_tier"].isin(selected_tier)
if has_status and selected_status:
    mask &= df_raw["deployment_status"].isin(selected_status)

df_filtered = df_raw[mask].copy()
is_empty = df_filtered.empty

# ==========================================
# 4. PILLAR 3: QUANTIFIED BUSINESS IMPACT
# ==========================================
st.write("##") 
st.markdown("### 📊 Program Performance & Quantified Business Impact")

# Dynamic calculations protected against empty filter states
total_systems = len(df_filtered)
high_critical_count = 0
avg_maturity = "N/A"

if not is_empty:
    if "eu_ai_act_risk_tier" in df_filtered.columns:
        high_critical_count = len(df_filtered[df_filtered["eu_ai_act_risk_tier"].str.lower().isin(["high", "critical", "high risk", "unacceptable", "unacceptable risk"])])
    if "nist_rmf_maturity_level" in df_filtered.columns:
        # Cast explicitly to ensure numeric calculation path
        valid_maturity = pd.to_numeric(df_filtered["nist_rmf_maturity_level"], errors='coerce').dropna()
        if not valid_maturity.empty:
            avg_maturity = f"{valid_maturity.mean():.1f} / 5.0"

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
with metric_col1:
    st.metric(label="Centralized Oversight", value=f"{total_systems} AI Systems" if not is_empty else "0 Systems", delta=f"{len(df_raw)} Total Tracked")
with metric_col2:
    st.metric(label="Audit Prep Efficiency", value="-88%", delta="From Weeks to Hours")
with metric_col3:
    st.metric(label="High/Critical Risk Vectors", value=high_critical_count, delta="Prioritized for Mitigation", delta_color="inverse")
with metric_col4:
    st.metric(label="Avg NIST Maturity Level", value=avg_maturity, delta="Continuous Improvement Target")

# ==========================================
# 5. PILLAR 2: LIVE OPERATIONAL CONTROL MONITORING
# ==========================================
st.write("##")
with st.container(border=True):
    st.markdown("### 🟢 Live Control Monitor: SignalPath Interpret")
    st.markdown(
        """
        **Continuous Control Loop Target:** Real-time risk mitigation engine for asset **SP-AI-001 SignalPath Interpret**.  
        *Failure Mode:* Computer vision tracking degradation via the 'broken pinky' ASL validation anomaly.
        """
    )
    
    control_col1, control_col2 = st.columns([1, 2])
    
    with control_col1:
        st.write("##") 
        confidence_score = st.slider(
            "Simulated ASL Model Confidence Score (%)",
            min_value=0,
            max_value=100,
            value=85,
            step=1,
            help="Slide below 75% to trigger the continuous control threshold alert."
        )

    with control_col2:
        if confidence_score < 75:
            st.error(
                f"❌ **CRITICAL ALERT: ASL Model Confidence dropped to {confidence_score}% (Threshold: <75%)**\n\n"
                "**Breach Vector:** High probability of 'broken pinky' sign language misclassification detected.\n\n"
                "**Automated Guardrail:** Human Interpreter Override deployed. Production model isolated."
            )
            st.warning(
                "**Incident Escalation Path:**\n"
                "* 📥 **Alert Routing:** Governance Lead, Product Safety Officer, Lead MLOps Engineer\n"
                "* ⏱️ **SLA Registry:** 15-minute response ticket generated automatically in GRC Log."
            )
        else:
            st.success(
                f"✅ **Control Operating Effectively ({confidence_score}%)**\n\n"
                "Model confidence remains within acceptable bounds. No human-in-the-loop interventions required."
            )

# ==========================================
# 6. PILLAR 1: INTERACTIVE AI SYSTEM INVENTORY
# ==========================================
st.write("##")
st.markdown("### 📋 Active Systems Registry")

if is_empty:
    st.info("⚠️ No AI systems match the current sidebar filter parameters. Adjust your selections to review data.")
else:
    # Normalize values for mapping priority color badges in display layer
    risk_visuals = {
        "unacceptable risk": "🔴 Unacceptable Risk", "unacceptable": "🔴 Unacceptable Risk", "critical": "🔴 Unacceptable Risk",
        "high risk": "🟠 High Risk", "high": "🟠 High Risk",
        "specific transparency": "🟡 Medium Risk", "medium risk": "🟡 Medium Risk", "medium": "🟡 Medium Risk",
        "minimal risk": "🟢 Minimal Risk", "minimal": "🟢 Minimal Risk", "low risk": "🟢 Minimal Risk", "low": "🟢 Minimal Risk"
    }
    if "eu_ai_act_risk_tier" in df_filtered.columns:
        df_filtered["Risk Priority"] = df_filtered["eu_ai_act_risk_tier"].astype(str).str.strip().str.lower().map(risk_visuals).fillna(df_filtered["eu_ai_act_risk_tier"])

    # Configure UI display grid to parse clean headers
    ui_configs = {}
    if "system_id" in df_filtered.columns: ui_configs["system_id"] = st.column_config.TextColumn("ID", width="small")
    if "system_name" in df_filtered.columns: ui_configs["system_name"] = st.column_config.TextColumn("System Name", width="medium")
    if has_bu: ui_configs["business_unit"] = st.column_config.TextColumn("Business Unit", width="medium")
    if "Risk Priority" in df_filtered.columns: ui_configs["Risk Priority"] = st.column_config.TextColumn("Regulatory Risk Tier")
    if has_status: ui_configs["deployment_status"] = st.column_config.TextColumn("Deployment Status", width="small")
    if "category" in df_filtered.columns: ui_configs["category"] = st.column_config.TextColumn("Category", width="small")
    if "eu_ai_act_risk_tier" in df_filtered.columns: ui_configs["eu_ai_act_risk_tier"] = None # Suppress raw duplicate column

    st.dataframe(
        df_filtered,
        column_config=ui_configs,
        use_container_width=True,
        hide_index=True
    )

    # ==========================================
    # 7. INTERACTIVE DETAIL PROFILE DEEP DIVE
    # ==========================================
    if "system_name" in df_filtered.columns:
        selected_system = st.selectbox("Select an inventory asset to review its full enterprise profile:", options=df_filtered["system_name"].tolist())
        system_profile = df_filtered[df_filtered["system_name"] == selected_system].iloc[0]
        
        with st.expander(f"Enterprise Profile: {selected_system}", expanded=False):
            # Display layer transformation helper function for null safety
            def get_field(field_name):
                val = system_profile.get(field_name)
                if pd.isna(val) or str(val).strip() == "" or str(val).lower() == "nan":
                    if field_name == "mitigation_strategy":
                        return "*Not yet defined*"
                    return "*Under Review*"
                return str(val)

            col_left, col_right = st.columns(2)
            with col_left:
                st.markdown(f"**Primary Purpose:** {get_field('primary_purpose')}")
                st.markdown(f"**Description:** {get_field('description')}")
                st.markdown(f"**Data Inputs:** `{get_field('data_inputs')}`")
                st.markdown(f"**Outputs:** `{get_field('outputs')}`")
                st.markdown(f"**Geographic Scope:** {get_field('geographic_scope')}")
            with col_right:
                st.markdown(f"**System Owner:** {get_field('system_owner')}")
                st.markdown(f"**Sourcing Origin:** {get_field('vendor_or_internal')}")
                st.markdown(f"**Affected Persons:** {get_field('affected_persons')}")
                st.markdown(f"**NIST RMF Maturity Level:** `{get_field('nist_rmf_maturity_level')}`")
                st.markdown(f"**FCC Regulatory Exposure:** {get_field('fcc_regulatory_exposure')}")
            
            st.markdown("---")
            st.markdown(f"**Operational Mitigation Strategy:** \n{get_field('mitigation_strategy')}")
            st.markdown(f"*Audit Notes:* {get_field('notes')}")

# ==========================================
# 8. LOCAL COMPLIANCE BASELINE REFERENCES
# ==========================================
st.write("##")
st.markdown("### 📚 Framework Documentation Reference")

tab1, tab2 = st.tabs(["EU AI Act Classification", "NIST RMF Mapping"])

with tab1:
    try:
        md_path1 = os.path.join(BASE_PATH, "eu-ai-act-classification-signalpath.md")
        with open(md_path1, "r", encoding="utf-8", errors="ignore") as f:
            st.markdown(f.read())
    except Exception as e:
        st.error(f"Error reading EU AI Act file: {e}")

with tab2:
    try:
        md_path2 = os.path.join(BASE_PATH, "nist-rmf-mapping-signalpath.md")
        # Explicitly matching the local file encoding format found in previous iterations
        with open(md_path2, "r", encoding="utf-16", errors="ignore") as f:
            st.markdown(f.read())
    except Exception as e:
        st.error(f"Error reading NIST RMF file: {e}")
