import streamlit as st
import pandas as pd
import os

# ==========================================
# 1. PAGE INITIALIZATION & STATE
# ==========================================
st.set_page_config(page_title="SignalPath AI Center", layout="wide")

if 'view' not in st.session_state:
    st.session_state.view = "Command Center"

st.markdown("### 🛡️ SignalPath AI Governance Control Center")
st.markdown("---")

col_n1, col_n2, col_n3 = st.columns(3)
with col_n1:
    if st.button("🕹️ Operational Command Center", use_container_width=True, type="primary" if st.session_state.view == "Command Center" else "secondary"):
        st.session_state.view = "Command Center"
        st.rerun()
with col_n2:
    if st.button("📋 Active Registry Inventory", use_container_width=True, type="primary" if st.session_state.view == "Registry" else "secondary"):
        st.session_state.view = "Registry"
        st.rerun()
with col_n3:
    if st.button("📚 Regulatory Framework Mapping", use_container_width=True, type="primary" if st.session_state.view == "Docs" else "secondary"):
        st.session_state.view = "Docs"
        st.rerun()

st.markdown("##")

BASE_PATH = "project-01-ai-system-inventory"

@st.cache_data
def load_inventory_data():
    excel_path = os.path.join(BASE_PATH, "ai-system-inventory-signalpath.xlsx")
    df = pd.read_excel(excel_path, engine="openpyxl")
    df.columns = [col.strip() for col in df.columns]
    return df

df_raw = load_inventory_data()

# Sidebar
st.sidebar.markdown("### ⚙️ Registry Filters")
all_bus = sorted(df_raw["business_unit"].dropna().unique())
selected_bu = st.sidebar.selectbox("Active Business Unit", options=["All Units"] + all_bus)
selected_tier = st.sidebar.multiselect("Risk Tiers", options=sorted(df_raw["eu_ai_act_risk_tier"].dropna().unique()))
selected_status = st.sidebar.multiselect("Deployment Status", options=sorted(df_raw["deployment_status"].dropna().unique()))

mask = pd.Series(True, index=df_raw.index)
if selected_bu != "All Units": mask &= df_raw["business_unit"] == selected_bu
if selected_tier: mask &= df_raw["eu_ai_act_risk_tier"].isin(selected_tier)
if selected_status: mask &= df_raw["deployment_status"].isin(selected_status)
df_filtered = df_raw[mask].copy()

# ==========================================
# 2. VIEW ROUTER
# ==========================================
if st.session_state.view == "Command Center":
    st.info("Continuous Control Telemetry Active.")
    cols = st.columns(4)
    with cols[0]: st.metric("Systems", len(df_filtered))
    with cols[1]: st.metric("Efficiency", "-88%")
    with cols[2]: st.metric("High Risk", len(df_filtered[df_filtered['eu_ai_act_risk_tier'] == 'High']))
    with cols[3]: st.metric("NIST Maturity", "2.0")
    
    with st.container(border=True):
        st.markdown("### 🚨 Live Control Monitor")
        conf = st.slider("Model Confidence (%)", 0, 100, 85)
        if conf < 75: st.error("CRITICAL EXCEPTION: Failover initiated.")
        else: st.success(f"Operating Effectively ({conf}%)")

elif st.session_state.view == "Registry":
    st.markdown("### 📋 Active Registry Inventory")
    st.dataframe(df_filtered, use_container_width=True)

elif st.session_state.view == "Docs":
    st.markdown("### 📚 Regulatory Framework Mapping")
    try:
        with open(os.path.join(BASE_PATH, "eu-ai-act-classification-signalpath.md"), "r") as f:
            st.markdown(f.read())
    except: st.error("Documentation not found.")
