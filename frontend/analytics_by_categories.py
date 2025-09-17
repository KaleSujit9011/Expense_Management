import streamlit as st
import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_by_category_tab():
    st.title("Expense Analytics by Category")

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("->Start Date", datetime.date(2024, 8, 1), key="start_date_analytics_tab")
        with col2:
            end_date = st.date_input("<-End Date", datetime.date(2025, 8, 1), key="end_date_analytics_tab")

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat()
        }

        with st.spinner("Fetching analytics..."):
            response = requests.post(f"{API_URL}/analytic/category/", json=payload)

        if response.status_code == 200:
            data = response.json()

            if not data:
                st.warning("⚠No expense data found for the selected date range.")
                return

            df = pd.DataFrame({
                "Category": list(data.keys()),
                "Total (₹)": [data[cat]["total"] for cat in data],
                "Percentage (%)": [data[cat]["percentage"] for cat in data]
            })

            df_sorted = df.sort_values(by="Percentage (%)", ascending=False)

            st.subheader("Category-wise Expense Distribution")
            st.bar_chart(data=df_sorted.set_index("Category")["Percentage (%)"])

            with st.expander("Detailed Table", expanded=True):
                st.dataframe(df_sorted.style.format({
                    "Total (₹)": "₹{:.2f}",
                    "Percentage (%)": "{:.2f}%"
                }))
        else:
            st.error(f"---Error: {response.status_code} - {response.text}")
