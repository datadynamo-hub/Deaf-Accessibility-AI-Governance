import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("SignalPath AI Operational Governance Center")

# --- PLACEHOLDER FOR THE DATA LOAD ---
st.warning("Data load pending path confirmation below.")

st.write("---")

# Your stable markdown document layout restored
st.subheader("Framework Documentation Reference")
doc_col1, doc_col2 = st.columns(2)

with doc_col1:
    st.markdown("### EU AI Act Classification")
    try:
        with open("eu-ai-act-classification-signalpath.md", "r", encoding="utf-8", errors="ignore") as f:
            st.markdown(f.read())
    except Exception as e:
        st.error(f"Error reading EU AI Act file: {e}")

with doc_col2:
    st.markdown("### NIST RMF Mapping")
    try:
        with open("nist-rmf-mapping-signalpath.md", "r", encoding="utf-16", errors="ignore") as f:
            st.markdown(f.read())
    except Exception as e:
        st.error(f"Error reading NIST RMF file: {e}")
