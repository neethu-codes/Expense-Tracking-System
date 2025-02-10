import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_category_tab():
    col1,col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Enter start date")
    with col2:
        end_date = st.date_input("Enter end date")
    req_body = {
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date":end_date.strftime("%Y-%m-%d")
               }
    if st.button("Submit"):
        response = requests.post(f"{API_URL}/analytics",json=req_body)
        if response.status_code == 200:
          data_dict = response.json()

          data_list = [{"Category": key,"Total":value['total'] ,"Percentage":value['percentage']} for key,value in data_dict.items()]

          df = pd.DataFrame(data_list)
          df_sorted = df.sort_values(by="Percentage",ascending=False)

          st.subheader("Expense breakdown by category")

          st.bar_chart(data=df_sorted.set_index("Category")['Total'],width=0,height=0, use_container_width = True)
          df_sorted['Total'] = df_sorted["Total"].map("{:.2f}".format)
          df_sorted['Percentage'] = df_sorted["Percentage"].map("{:.2f}".format)
          st.table(df_sorted)
          

 




