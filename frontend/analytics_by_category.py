import streamlit as st
import requests
import pandas as pd
from matplotlib import pyplot as plt

API_URL = "http://localhost:8000"

def analytics_category_tab():
    col1,col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Enter start date")
    with col2:
        end_date = st.date_input("Enter end date")

    if start_date > end_date:
        st.error("Start date must be earlier than or equal to end date.")
        return
    req_body = {
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date":end_date.strftime("%Y-%m-%d")
               }
    if st.button("Submit"):
        response = requests.post(f"{API_URL}/category_summary/",json=req_body)
        if response.status_code == 200:
          data_dict = response.json()
          
          
          if data_dict == None or data_dict == {}:
            st.info("No expenses for the selected dates")
            return
          
          data_list = [{"Category": key,"Total":value['total'] ,"Percentage":value['percentage']} for key,value in data_dict.items()]

          df = pd.DataFrame(data_list)
          df_sorted = df.sort_values(by="Percentage",ascending=False)

          st.subheader("Expense breakdown by category")

        #   st.bar_chart(data=df_sorted.set_index("Category")['Total'],width=0,height=0, use_container_width = True)
          
          df_sorted['Total'] = df_sorted["Total"].map("{:.2f}".format)
          df_sorted['Percentage'] = df_sorted["Percentage"].map("{:.2f}".format)
          st.table(df_sorted.reset_index(drop=True))

          _,col2,_ = st.columns([0.2,0.6, 0.2])
          with col2:
            # plt.figure(figsize=(5,7))
            plt.pie(data = df_sorted, x="Percentage",labels=df_sorted["Category"],autopct="%1.2f")
            st.pyplot(plt)
          

 




