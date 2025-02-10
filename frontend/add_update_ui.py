import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"
def add_update_tab():
  selected_date = st.date_input("Enter your expense date",label_visibility="collapsed")

  response = requests.get(f"{API_URL}/expenses/{selected_date}")
  print(response)
  if response.status_code == 200:
    existing_expenses = response.json()
    categories = ['Rent','Entertainment','Shopping','Food','Other']
    expenses=[]
    with st.form(key="expense_form"):
        col1,col2,col3 = st.columns(3)
        with col1:
           st.text("Amount")
        with col2:
           st.text("Category")
        with col3:
           st.text("Notes")
        for i in range(5):
            if i < len(existing_expenses):
               amount = existing_expenses[i]["amount"]
               category = existing_expenses[i]["category"]
               notes = existing_expenses[i]["notes"]
            else:
               amount = 0.0
               category = "Other"  
               notes =  ""
            with col1:
              amount_input=st.number_input(label="Amount",min_value=0.0,step=1.0,value=amount,key=f"amount_{i}",label_visibility="collapsed")
            with col2:
              category_input=st.selectbox(label="Category",options=categories,index = categories.index(category),key=f"category_{i}",label_visibility="collapsed")
            with col3:
              notes_input=st.text_input(label="Notes",key=f"notes_{i}",label_visibility="collapsed",value=notes)

            expenses.append({
                "category": category_input,
                "notes": notes_input,
                "amount": amount_input
            })

        submit_button = st.form_submit_button()
        if submit_button:
           
           filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]
           response = requests.post(f"{API_URL}/expenses/{selected_date}",json=filtered_expenses)
           if response.status_code == 200:
              st.write(f"DB updated successful")
           else:
              st.write(f"db update failed")
    
                  
   
  else:
    st.write("failed to retrieve expense")  
    existing_expenses = []
