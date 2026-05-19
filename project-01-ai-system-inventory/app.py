import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")

st.title("Deaf Accessibility AI Governance Project")
st.header("AI System Inventory Dashboard")

# Base paths for project files
folder_prefix = "project-01-ai-system-inventory"
excel_file = f"{folder_prefix}/ai-system-inventory-signalpath.xlsx"
eu_file = f"{folder_prefix}/eu-ai-act-classification-signalpath.md"
nist_file = f"{folder_prefix}/nist-rmf-mapping-signalpath.md"

# 1. Display the Excel Data
if os.path.exists(excel_file):
    df = pd.read_excel(excel_file)
    st.dataframe(df, use_container_width=True)
else:
    st.error(f"Could not find data file: {excel_file}")

st.markdown("---")

# 2. Display Governance Frameworks Side-by-Side
col1, col2 = st.columns(2)

with col1:
    st.subheader("EU AI Act Classification")
    if os.path.exists(eu_file):
        with open(eu_file, "r", encoding="utf-8", errors="ignore") as f:
            st.markdown(f.read())
    else:
        st.warning(f"Could not find: {eu_file}")

with col2:
    st.subheader("NIST RMF Mapping")
    if os.path.exists(nist_file):
        with open(nist_file, "r", encoding="utf-16", errors="ignore") as f:
            st.markdown(f.read())
    else:
        st.warning(f"Could not find: {nist_file}")
