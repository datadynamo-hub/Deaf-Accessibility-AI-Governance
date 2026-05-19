import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="SignalPath | AI Governance & Risk Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("SignalPath AI Operational Governance Center")
st.caption("Active System Inventory & EU AI Act Compliance Mapping")

# 2. Load Data Pipeline
@st.cache_data
def load_inventory_data():
    # Utilizing your existing excel setup
    df = pd.read_excel("ai-system-inventory-signalpath.xlsx", engine="openpyxl")
    
    # Strip whitespace from column names for robust filtering
    df.columns = [col.strip() for col in df.columns]
    return df

try:
    df_raw = load_inventory_data()
except Exception as e:
    st.error(f"Error loading inventory file: {e}")
    st.stop()

# 3. Sidebar Filtering Implementation
st.sidebar.header("Global Inventory Filters")

# Dynamic filter extractions based on your spreadsheet columns
all_product_lines = sorted(df_raw["Product Line"].dropna().unique()) if "Product Line" in df_raw.columns else []
all_tiers = sorted(df_raw["EU AI Act Classification"].dropna().unique()) if "EU AI Act Classification" in df_raw.columns else []
all_statuses = sorted(df_raw["Compliance Status"].dropna().unique()) if "Compliance Status" in df_raw.columns else []

selected_product = st.sidebar.multiselect("Filter by Product Line", options=all_product_lines, default=all_product_lines)
selected_tier = st.sidebar.multiselect("Filter by EU AI Act Tier", options=all_tiers, default=all_tiers)
selected_status = st.sidebar.multiselect("Filter by Compliance Status", options=all_statuses, default=all_statuses)

# Apply filter masks
mask = (
    df_raw["Product Line"].isin(selected_product) &
    df_raw["EU AI Act Classification"].isin(selected_tier) &
    df_raw["Compliance Status"].isin(selected_status)
)
df_filtered = df_raw[mask].copy()

# 4. Value-Driven High-Level Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Tracked AI Systems", value=len(df_filtered))
with col2:
    high_risk_count = len(df_filtered[df_filtered["Risk Level"].isin(["High", "Critical"])]) if "Risk Level" in df_filtered.columns else 0
    st.metric(label="High/Critical Risk Systems", value=high_risk_count, delta="Requires Audit", delta_color="inverse")
with col3:
    compliance_rate = f"{(len(df_filtered[df_filtered['Compliance Status'] == 'Compliant']) / len(df_filtered) * 100):.1f}%" if len(df_filtered) > 0 else "0%"
    st.metric(label="Governance Alignment Rate", value=compliance_rate)

st.write("---")

# 5. Interactive Table Configuration (Color-Coding & Sorting)
st.subheader("Active Systems Registry")

# Define visual risk mapping to provide a clear UI for recruiters
risk_visuals = {
    "Critical": "🔴 Critical",
    "High": "🟠 High",
    "Medium": "🟡 Medium",
    "Low": "🟢 Low"
}

if "Risk Level" in df_filtered.columns:
    df_filtered["Risk Visual"] = df_filtered["Risk Level"].map(risk_visuals).fillna(df_filtered["Risk Level"])

# Render Interactive Dataframe with st.column_config
st.dataframe(
    df_filtered,
    column_config={
        "System ID": st.column_config.TextColumn("ID", help="Unique system identifier", width="small"),
        "System Name": st.column_config.TextColumn("System Name", width="medium"),
        "Product Line": st.column_config.TextColumn("Product Line", width="medium"),
        "EU AI Act Classification": st.column_config.TextColumn("EU AI Act Tier", width="medium"),
        "Risk Visual": st.column_config.TextColumn("Risk Priority", help="Color-coded risk mapping"),
        "Compliance Status": st.column_config.TextColumn("Status", width="small"),
        "Risk Level": None # Hide raw unmapped text column to keep view clean
    },
    use_container_width=True,
    hide_index=True
)

# 6. Expandable System Classification Rationale
st.write("---")
st.subheader("Deep Dive: System Classification Rationale")

system_list = df_filtered["System Name"].tolist() if "System Name" in df_filtered.columns else []

if system_list:
    selected_system = st.selectbox("Select an AI System to inspect its governance profile:", options=system_list)
    system_profile = df_filtered[df_filtered["System Name"] == selected_system].iloc[0]
    
    with st.expander(f"Governance Profile & Rationale for {selected_system}", expanded=True):
        r_col1, r_col2 = st.columns(2)
        with r_col1:
            st.markdown(f"**System ID:** `{system_profile.get('System ID', 'N/A')}`")
            st.markdown(f"**Classification Tier:** {system_profile.get('EU AI Act Classification', 'N/A')}")
        with r_col2:
            st.markdown(f"**Current Compliance Track:** {system_profile.get('Compliance Status', 'N/A')}")
            st.markdown(f"**Assigned Risk Category:** {system_profile.get('Risk Level', 'N/A')}")
        
        st.write("---")
        st.markdown("**Compliance Rationale & Operational Bounds:**")
        # Handles spreadsheet column named 'Rationale' or 'Description' dynamically
        rationale_text = system_profile.get("Rationale", system_profile.get("Description", "No explicit rationale found in inventory file."))
        st.info(rationale_text)
else:
    st.info("No systems match current filter criteria.")

st.write("---")

# 7. Document Viewers (Your Existing Stable Implementation)
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
