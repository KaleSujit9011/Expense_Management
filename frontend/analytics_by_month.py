import streamlit as st
import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_by_month_tab():
    st.title(" Monthly Expense Analysis")

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("Start Date", datetime.date(2024, 8, 1), key="start_date_analytics")
        with col2:
            end_date = st.date_input("End Date", datetime.date(2025, 8, 1), key="end_date_analytics")

    if st.button("Get Monthly Analysis"):
        payload = {
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat()
        }

        with st.spinner("Fetching data..."):
            response = requests.post(f"{API_URL}/analytic/month/", json=payload)

        if response.status_code == 200:
            data = response.json()

            if isinstance(data, list) and data:
                results = [
                    {"Month": row["month"], "Total (₹)": row["total"]}
                    for row in data
                    if isinstance(row, dict) and "month" in row and "total" in row
                ]

                if results:
                    df = pd.DataFrame(results).sort_values(by="Month")

                    st.subheader("Monthly Expenses Overview")
                    st.bar_chart(df.set_index("Month")["Total (₹)"])

                    with st.expander("Detailed Table View", expanded=True):
                        st.dataframe(df.style.format({"Total (₹)": "₹{:.2f}"}), use_container_width=True)
                else:
                    st.warning("⚠No valid data entries found.")
            else:
                st.warning("⚠No data returned from API.")
        else:
            st.error(f"Failed to fetch data. Status code: {response.status_code}")

