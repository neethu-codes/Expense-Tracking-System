from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

class Expense(BaseModel):
    category: str
    amount: float
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date

app=FastAPI()

@app.get("/expenses/{date}",response_model = List[Expense])
def get_expenses_by_date(date:date):
    expense = db_helper.fetch_expenses_for_date(date)
    return expense

@app.post("/expenses/{expense_date}")
def insert_expenses_by_date(expense_date:date, expenses: List[Expense]):

    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
    
    return f"expenses inserted/updated"
    # return f"request received for {date}"

@app.post("/category_summary/")
def get_expenses_between_dates(date_range:DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500,detail = "fetch expense summary failed")
    

    summary = {}
    full_total = sum([row['total'] for row in data])
    for row in data:   
        percentage = (row['total']/full_total)*100  if full_total!=0 else 0  
        summary[row["category"]]= {
                                "total":row['total'],
                                "percentage":round((row['total']/full_total)*100,2)
                            }
                     
    return summary

@app.get("/monthly_summary/")
def get_all_expenses_by_month():
    data = db_helper.fetch_monthly_expense_summary()
    if data is None:
        raise HTTPException(status_code=500,detail = "fetch expense by month failed")
    return data


@app.post("/daily_summary/")
def get_analytics_by_day(date_range: DateRange):
    daily_summary = db_helper.fetch_daily_expense_summary(date_range.start_date, date_range.end_date)
    if daily_summary is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve daily expense summary from the database.")

    return daily_summary
