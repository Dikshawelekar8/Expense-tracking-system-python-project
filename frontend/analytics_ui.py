import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_url = "http://localhost:8000"

def analytics_category_tab():
        col1, col2 = st.columns(2)
        with col1:
                start_date = st.date_input("**Start date**", datetime(2024, 8, 1))
        with col2:
                end_date = st.date_input("**End date**", datetime(2024, 8, 30))

        if "start_date" not in st.session_state:
            st.session_state["start_date"] = start_date
        if "end_date" not in st.session_state:
            st.session_state["end_date"] = end_date

        if st.button("Analytics"):
                if end_date <= start_date:
                        st.error("❌ End date must be later than Start date.")
                else:
                        # Safe to build payload here
                        payload = {
                                "start_date": start_date.strftime("%Y-%m-%d"),
                                "end_date": end_date.strftime("%Y-%m-%d")
                        }

                        response = requests.post(f"{API_url}/analytics/", json=payload)
                        response = response.json()

                        data = {
                                "Category": list(response.keys()),
                                "Total": [response[category]["total"] for category in response],
                                "Percentage": [response[category]["percentage"] for category in response]
                        }

                        df = pd.DataFrame(data)
                        df_sorted = df.sort_values(by="Percentage", ascending=False)

                        # Round numerically
                        df_sorted["Total"] = df_sorted["Total"].round(2)
                        df_sorted["Percentage"] = df_sorted["Percentage"].round(2)

                        st.header("Expense breakdown by category")
                        st.bar_chart(df_sorted.set_index("Category")["Percentage"])
                        st.table(
                                df_sorted.set_index("Category").style.format({
                                        "Total": "{:.2f}",
                                        "Percentage": "{:.2f}%"
                                })
                        )
