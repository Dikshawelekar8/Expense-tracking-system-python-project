import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_category_tab

API_url = "http://localhost:8000"

st.title("Monthly Expense Tracking")
tab1, tab2 = st.tabs(["Add/update", "Analytics by Category"])

with tab1:
    add_update_tab()
with tab2:
    analytics_category_tab()

