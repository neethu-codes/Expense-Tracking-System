import streamlit as st
from add_update_ui import add_update_tab
from analytics_by_category import analytics_category_tab
from analytics_by_month import analytics_month_tab
from analytics_by_date import analytics_days_tab

st.title("Expense Management System")
tab1,tab2,tab3,tab4 = st.tabs(["Add/Update","Analytics by Category","Analytics by Month", "Analytics by Days"])

with tab1:
    add_update_tab()

with tab2:
    analytics_category_tab()

with tab3:
    analytics_month_tab()

with tab4:
    analytics_days_tab()
