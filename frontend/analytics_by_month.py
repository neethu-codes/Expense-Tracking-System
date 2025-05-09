import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_month_tab():
    response = requests.get(f"{API_URL}/monthly_summary/")
    if response.status_code == 200:
        data_list = response.json()
        
        data_list_new = [{"Month Name": expense['month_name'],"Total":expense['total'],"Month Number":expense['expense_month']} for expense in data_list]
        
        df = pd.DataFrame(data_list_new)
        df_sorted = df.sort_values(by="Month Number",ascending=True)
        
        st.subheader("Expense breakdown by month")
        st.bar_chart(data=df_sorted.set_index("Month Name")['Total'],width=0,height=0, use_container_width = True)

        df_sorted['Total'] = df_sorted["Total"].map("{:.2f}".format)
        st.table(df_sorted[['Month Name','Total']].reset_index(drop=True))



    # response = requests.get(f"{API_URL}/analytics")
    # monthly_summary = response.json()

    # df = pd.DataFrame(monthly_summary)
    # df.rename(columns={
    #     "month_number": "Month Number",
    #     "month_name": "Month Name",
    #     "total": "Total"
    # }, inplace=True)
    # df_sorted = df.sort_values(by="Month Number", ascending=False)
    # df_sorted.set_index("Month Number", inplace=True)

    # st.title("Expense Breakdown By Months")

    # st.bar_chart(data=df_sorted.set_index("Month Name")['Total'], width=0, height=0, use_container_width=True)

    # df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)

    # st.table(df_sorted.sort_index())