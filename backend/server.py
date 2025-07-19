from http.client import HTTPException

from fastapi import FastAPI
from datetime import date

from fastapi.openapi.utils import status_code_ranges

import db_helper
from typing import List
from pydantic import BaseModel

app = FastAPI()

class  Expense(BaseModel):
    amount:float
    category:str
    notes:str

class  DateRange(BaseModel):
    start_date:date
    end_date:date

@app.get("/expenses/{expense_date}",response_model=List[Expense])

async def get_expenses(expense_date: str):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update(expense_date: date ,expenses: List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date,expense.amount,expense.category,expense.notes)

    return  {"message": "Expense updated successfully"}

@app.post("/analytic/category/")
def get_analytics_category(date_range:DateRange):
    data = db_helper.fetch_expense_summary_categories(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500 , detail="Failed to retrieve expense summary from the database")

    total = sum([row['total'] for row in data])
    breakdown = {}
    for row in data:
        percentage = (row['total']*100/total) if total != 0 else 0
        breakdown[row['category']] = {
            'total':row['total'],
            "percentage":percentage
        }
    return breakdown

@app.post("/analytic/month/")
def get_analytics_month(date_range: DateRange):
    data = db_helper.fetch_expense_summary_months(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database")

    results = []
    for row in data:
        results.append({
            "month": row["month"],
            "total": row["total"]
        })

    return results

