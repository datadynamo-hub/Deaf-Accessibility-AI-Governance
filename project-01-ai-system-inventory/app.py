import streamlit as st
import pandas as pd
import os

st.title("Deaf Accessibility AI Governance Project")
st.header("AI System Inventory")

# Locate the Excel file in the same subfolder
file_name = "ai-system-inventory-signalpath.xlsx"

if os.path.exists(file_name):
    # Read the Excel data
    df = pd.read_excel(file_name)
    
    # Display the data table in Streamlit
    st.dataframe(df, use_container_width=True)
else:
    st.error(f"Could not find data file: {file_name}")
