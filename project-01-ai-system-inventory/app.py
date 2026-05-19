import streamlit as st
import pandas as pd
import os

# 1. Page Configuration (Wide layout for a professional dashboard feel)
st.set_page_config(
    page_title="SignalPath AI Operational Governance Center",
    page_icon="🛡️",
    layout="wide"
)

st.title("SignalPath AI Operational Governance Center")
st.caption("Unified GRC Engineering Demo: Continuous Monitoring, Inventory & Regulatory Mapping")

BASE_PATH = "project-01-ai-system-inventory"

# 2. Data Pipeline
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

# --- PILLAR 3: QUANTIFIED BUSINESS IMPACT (Top-Level Metrics Hierarchy) ---
st.write("---")
st.subheader("📊 Program Performance & Quantified Business Impact")

# Dynamic calculations for impact tracking
total_systems = len(df_raw)
high_critical_count = len(df_raw[df_raw["Risk Level"].isin(["High", "Critical"])]) if "Risk Level" in df_raw.columns else 0

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
with metric_col1:
    st.metric(label="Centralized Oversight", value=f"{total_systems} AI Systems", delta="16 Identified Lack of Oversight")
with metric_col2:
    st.metric(label="Audit Prep Efficiency", value="-88%", delta="From Weeks to Hours")
with metric_col3:
    st.metric(label="High/Critical Risk Vectors", value=high_critical_count, delta="Prioritized for Mitigation", delta_color="inverse")
with metric_col4:
    st.metric(label="Regulatory Alignment Rate", value="100%", delta="EU AI Act / NIST RMF Verified")

# --- PILLAR 2: SIMULATED OPERATIONAL CONTROL MONITORING ---
st.write("---")
st.subheader("🚨 Live Operational Control Monitoring")
st.markdown(
    """
    **Continuous Control Loop Demo:** Real-time risk telemetry for **SP-AI-001 SignalPath Interpret**. 
    *Failure Mode Simulator:* Computer vision degradation via the 'broken pinky' ASL tracking anomaly.
    """
)

control_col1, control_col2 = st.columns([1, 2])

with control_col1:
    # Interactive widget simulating live production telemetry
    confidence_score = st.slider(
        "Simulated ASL Model Confidence Score (%)",
        min_value=0,
        max_value=100,
        value=85,
        step=1,
        help="Slide below 75% to trigger the continuous control threshold alert."
    )

with control_col2:
    # Threshold-based alerting logic
    if confidence_score < 75:
        st.error(
            f"❌ **CRITICAL ALERT: ASL Model Confidence dropped to {confidence_score}% (Threshold: <75%)**\n\n"
            "**Breach Vector:** High probability of 'broken pinky' sign language misclassification detected.\n\n"
            "**Automated Guardrail:** Human Interpreter Override deployed. Production model isolated."
        )
        # Incident response escalation matrix
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


# --- PILLAR 1: INTERACTIVE AI SYSTEM INVENTORY ---
st.write("---")
st.subheader("📋 Active Systems Registry")

# Sidebar Filters (Scoped into columns for clean view control if preferred, keeping sidebar focused)
st.sidebar.header("Inventory Filters")

all_product_lines = sorted(df_raw["Product Line"].dropna().unique()) if "Product Line" in df_raw.columns else []
all_tiers = sorted(df_raw["EU AI Act Classification"].dropna().unique()) if "EU AI Act Classification" in df_raw.columns else []
all_statuses = sorted(df_raw["Compliance Status"].dropna().unique()) if "Compliance Status" in df_raw.columns else []

selected_product = st.sidebar.multiselect("Product Line", options=all_product_lines, default=all_product_lines)
selected_tier = st.sidebar.multiselect("EU AI Act Tier", options=all_tiers, default=all_tiers)
selected_status = st.sidebar.multiselect("Compliance Status", options=all_statuses, default=all_statuses)

# Apply Filters
mask = (
    df_raw["Product Line"].isin(selected_product) &
    df_raw["EU AI Act Classification"].isin(selected_tier) &
    df_raw["Compliance Status"].isin(selected_status)
)
df_filtered = df_raw[mask].copy()

# Map Categorical Risk Levels to Stable UI Badges
risk_visuals = {
    "Critical": "🔴 Critical",
    "High": "🟠 High",
    "Medium": "🟡 Medium",
    "Low": "🟢 Low"
}
if "Risk Level" in df_filtered.columns:
    df_filtered["Risk Priority"] = df_filtered["Risk Level"].map(risk_visuals).fillna(df_filtered["Risk Level"])

# Interactive Dataframe Configuration
st.dataframe(
    df_filtered,
    column_config={
        "System ID": st.column_config.TextColumn("ID", width="small"),
        "System Name": st.column_config.TextColumn("System Name", width="medium"),
        "Product Line": st.column_config.TextColumn("Product Line", width="medium"),
        "EU AI Act Classification": st.column_config.TextColumn("EU AI Act Tier", width="medium"),
        "Risk Priority": st.column_config.TextColumn("Risk Priority", help="Risk matrix categorization"),
        "Compliance Status": st.column_config.TextColumn("Status", width="small"),
        "Risk Level": None # Suppress the raw column
    },
    use_container_width=True,
    hide_index=True
)

# Expandable System Rationale Deep Dive
if "System Name" in df_filtered.columns and not df_filtered.empty:
    selected_system = st.selectbox("Select a system to review its governance rationale:", options=df_filtered["System Name"].tolist())
    system_profile = df_filtered[df_filtered["System Name"] == selected_system].iloc[0]
    
    with st.expander(f"Regulatory Profile Rationale: {selected_system}", expanded=False):
        rationale_text = system_profile.get("Rationale", system_profile.get("Description", "No explicit justification file mapped."))
        st.info(rationale_text)


# --- DOCUMENTATION REFERENCE (Your Existing Stable Section) ---
st.write("---")
st.subheader("📚 Framework Documentation Reference")
doc_col1, doc_col2 = st.columns(2)

with doc_col1:
    st.markdown("### EU AI Act Classification")
    try:
        md_path1 = os.path.join(BASE_PATH, "eu-ai-act-classification-signalpath.md")
        with open(md_path1, "r", encoding="utf-8", errors="ignore") as f:
            st.markdown(f.read())
    except Exception as e:
        st.error(f"Error reading EU AI Act file: {e}")

with doc_col2:
    st.markdown("### NIST RMF Mapping")
    try:
        md_path2 = os.path.join(BASE_PATH, "nist-rmf-mapping-signalpath.md")
        with open(md_path2, "r", encoding="utf-16", errors="ignore") as f:
            st.markdown(f.read())
    except Exception as e:
        st.error(f"Error reading NIST RMF file: {e}")
