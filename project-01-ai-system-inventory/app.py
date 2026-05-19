import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")

st.title("SignalPath AI Operational Governance Center")

# Define the correct path prefix based on your repository setup
BASE_PATH = "project-01-ai-system-inventory"

# 1. Load Data Pipeline
@st.cache_data
def load_inventory_data():
    excel_path = os.path.join(BASE_PATH, "ai-system-inventory-signalpath.xlsx")
    df = pd.read_excel(excel_path, engine="openpyxl")
    df.columns = [col.strip() for col in df.columns]
    return df

try:
    df_raw = load_inventory_data()
    st.success("Inventory data loaded successfully.")
    # Standard dataframe display
    st.dataframe(df_raw, use_container_width=True)
except Exception as e:
    st.error(f"Error loading inventory file: {e}")

st.write("---")

# 2. Document Viewers (Restored Stable Side-by-Side Layout)
st.subheader("Framework Documentation Reference")
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
