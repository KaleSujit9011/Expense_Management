
import streamlit as st
import datetime
import requests

API_URL = "https://expensemanagement.streamlit.app/"

def add_update_tab():
    st.title(" Add and Update Daily Expenses")

    selected_date = st.date_input(
        "Enter Date:",
        datetime.date(2024, 8, 1),
        key="start_date_add_update",
    ).strftime("%Y-%m-%d")

    try:
        response = requests.get(f"{API_URL}/expenses/{selected_date}")
        existing_expenses = []
        if response.status_code == 200 and response.text.strip():
            try:
                existing_expenses = response.json()
            except ValueError:
                st.error("⚠️ Response could not be decoded as JSON.⚠️")
        else:
            st.warning("No existing expenses found for this date.")
    except Exception as e:
        st.error(f"🔌 Network error while fetching expenses: {e}🔌")
    
    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        st.markdown("###  Enter Expenses")

        if existing_expenses:
            st.markdown("#### 📌 Existing Expenses")
            for exp in existing_expenses:
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"₹ {exp['amount']}")
                with col2:
                    st.write(exp['category'])
                with col3:
                    st.write(exp['notes'])

        expenses = []
        st.markdown("#### ➕ Add New Expenses")

        for i in range(5):
            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(
                    label="Amount",
                    min_value=0.0,
                    step=10.0,
                    value=0.0,
                    key=f"amount_{i}",
                    label_visibility="collapsed"
                )
            with col2:
                category_input = st.selectbox(
                    label="Category",
                    options=categories,
                    key=f"category_{i}",
                    label_visibility="collapsed"
                )
            with col3:
                notes_input = st.text_input(
                    label="Notes",
                    value="",
                    key=f"notes_{i}",
                    label_visibility="collapsed"
                )

            if amount_input > 0.0:
                expenses.append({
                    "amount": amount_input,
                    "category": category_input,
                    "notes": notes_input
                })

        submit_button = st.form_submit_button("Submit💾")

        if submit_button:
            if not expenses:
                st.warning("⚠️ Please enter at least one valid expense.⚠️")
                return

            payload = {
                "date": selected_date,
                "expenses": expenses
            }

            try:
                update_response = requests.post(f"{API_URL}/expenses/{selected_date}", json=payload)
                if update_response.status_code == 200:
                    st.success("✅ Expenses updated successfully. ✅")
                else:
                    st.error(f"❌ Failed to update expenses. Status: {update_response.status_code}")
            except Exception as e:
                st.error(f"🔌 Network error: {e} 🔌")

