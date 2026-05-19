import streamlit as st
import pandas as pd
import os

# ==========================================
# 1. PAGE INITIALIZATION
# ==========================================
st.set_page_config(
    page_title="SignalPath AI Operational Governance Center",
    page_icon="🛡️",
    layout="wide"
)

# Custom premium layout header
st.markdown("### 🛡️ SignalPath AI Governance Control Center")
st.markdown("---")

# Navigation as high-end command buttons
col_n1, col_n2, col_n3 = st.columns(3)
with col_n1:
    st.button("🕹️ Operational Command Center", use_container_width=True, type="primary")
with col_n2:
    st.button("📋 Active Registry Inventory", use_container_width=True)
with col_n3:
    st.button("📚 Regulatory Framework Mapping", use_container_width=True)

st.markdown("##")

BASE_PATH = "project-01-ai-system-inventory"

# ==========================================
# 2. DATA INGESTION
# ==========================================
@st.cache_data
def load_inventory_data():
    excel_path = os.path.join(BASE_PATH, "ai-system-inventory-signalpath.xlsx")
    df = pd.read_excel(excel_path, engine="openpyxl")
    df.columns = [col.strip() for col in df.columns]
    return df

df_raw = load_inventory_data()

# ==========================================
# 3. GLOBAL SIDEBAR (Cleaned)
# ==========================================
st.sidebar.markdown("### ⚙️ Registry Filters")
st.sidebar.markdown("---")

# Use a selectbox instead of massive multi-select to save sidebar real estate
all_bus = sorted(df_raw["business_unit"].dropna().unique())
selected_bu = st.sidebar.selectbox("Active Business Unit", options=["All Units"] + all_bus)

# Cleaned multiselects with reduced clutter
selected_tier = st.sidebar.multiselect("Risk Tiers", options=sorted(df_raw["eu_ai_act_risk_tier"].dropna().unique()), default=[])
selected_status = st.sidebar.multiselect("Deployment Status", options=sorted(df_raw["deployment_status"].dropna().unique()), default=[])

# Logic
mask = pd.Series(True, index=df_raw.index)
if selected_bu != "All Units":
    mask &= df_raw["business_unit"] == selected_bu
if selected_tier:
    mask &= df_raw["eu_ai_act_risk_tier"].isin(selected_tier)
if selected_status:
    mask &= df_raw["deployment_status"].isin(selected_status)

df_filtered = df_raw[mask].copy()

# ==========================================
# 4. COMMAND CENTER INTERFACE
# ==========================================
st.info("👉 **Operational Status:** System telemetry is active. Adjust sidebar parameters to refine focus.")

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
with metric_col1:
    with st.container(border=True):
        st.metric("Systems Monitored", len(df_filtered))
with metric_col2:
    with st.container(border=True):
        st.metric("Audit Efficiency", "-88%")
with metric_col3:
    with st.container(border=True):
        st.metric("Risk Vectors", len(df_filtered[df_filtered['eu_ai_act_risk_tier'] == 'High']))
with metric_col4:
    with st.container(border=True):
        st.metric("NIST Maturity", "2.0 / 5.0")

st.write("##")

with st.container(border=True):
    st.markdown("### 🚨 Live Control Monitor: SignalPath Interpret")
    control_col1, control_col2 = st.columns([1, 2])
    
    with control_col1:
        conf = st.slider("Model Confidence Score (%)", 0, 100, 85)
    
    with control_col2:
        if conf < 75:
            st.error("CRITICAL EXCEPTION: Confidence below 75% threshold. Failover initiated.")
        else:
            st.success(f"Continuous Control Operating Effectively ({conf}%)")
