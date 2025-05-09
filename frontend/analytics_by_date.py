import streamlit as st
from datetime import datetime
import requests
import pandas as pd


API_URL = "http://localhost:8000"


def analytics_days_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start date", datetime(2024, 8, 1))

    with col2:
        end_date = st.date_input("End date", datetime(2024, 8, 5))

    if start_date > end_date:
        st.error("Start date must be earlier than or equal to end date.")
        return
    if st.button("Submit",key="day_submit_btn"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/daily_summary/", json=payload)
        response = response.json()
        # st.info(response)
        if response == None or response == []:
            st.info("No expenses for the selected dates")
            return
        df=pd.DataFrame(response, index=range(len(response)))
        

        st.line_chart(data=df, x='expense_day', y='total', x_label="Date", y_label="Expense", use_container_width=True)
        df.sort_values(by=['expense_day'],inplace=True)
        df['total'] = df["total"].map("{:.2f}".format)
        st.table(df)
        
    
