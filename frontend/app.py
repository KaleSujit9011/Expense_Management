
import streamlit as st


from add_update import add_update_tab
from analytics_by_categories import analytics_by_category_tab
from analytics_by_month import analytics_by_month_tab

API_URL = "http://localhost:8000"
st.title("Expense tracking System")
tab1,tab2,tab3 = st.tabs(["Add/Update","Analysis by categories","Analysis by month"])


with tab1:
    add_update_tab()
with tab2:
    analytics_by_category_tab()
with tab3:
    analytics_by_month_tab()