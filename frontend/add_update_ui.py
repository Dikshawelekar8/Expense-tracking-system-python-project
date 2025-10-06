import streamlit as st
import requests
from datetime import datetime

API_url = "http://localhost:8000"

def add_update_tab():
    selected_date = st.date_input("Enter the date", datetime(2024, 8, 1), label_visibility="collapsed")
    response = requests.get(f"{API_url}/expenses/{selected_date}")

    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.write("Failed to fetch the expenses")
        existing_expenses = []

    # ✅ Show error if no data exists for the selected date
    if not existing_expenses:
        st.error(f"No expense data available for {selected_date.strftime('%Y-%m-%d')}.")

    category_options = ["None","Rent","Food", "Shopping", "Entertainment", "Other"]

    for exp in existing_expenses:
        cat = exp.get("category", "None")
        if cat not in category_options:
            category_options.append(cat)

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
             st.text("Amount")
        with col2:
            st.text("Categories")
        with col3:
            st.text("Expenses")

        expenses = []

        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "None"
                notes = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(
                    label="Amount", min_value=0.0, step=1.0, value=amount,
                    key=f"amount_{i}", label_visibility="collapsed"
                )
            with col2:
                index = category_options.index(category) if category in category_options else 0
                category_input = st.selectbox(
                    label="Category", options=category_options, index=index,
                    key=f"category_{i}", label_visibility="collapsed"
                )
            with col3:
                notes_input = st.text_input(
                    label="Notes", value=notes, key=f"notes_{i}", label_visibility="collapsed"
                )

            # ✅ append inside loop
            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input,
            })

        add = st.form_submit_button("Save Expenses")
        if add:
            filtered_expenses = [ exp for exp in expenses if exp["amount"] > 0 ]

            if filtered_expenses:
                res = requests.post(f"{API_url}/expenses/{selected_date}", json=filtered_expenses)
                if res.status_code == 200:
                    st.success("Expenses saved successfully!")
                else:
                    st.error(f"Failed to save expenses. Status: {res.status_code}")
            else:
                st.warning("No valid expenses to save.")
