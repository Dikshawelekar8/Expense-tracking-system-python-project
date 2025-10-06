from fastapi import FastAPI, HTTPException
from datetime import date
from typing import List, Optional
from pydantic import BaseModel
import db_helper

class Expense(BaseModel):
    expense_date: Optional[date] = None
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date

app = FastAPI()

@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expense(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: list[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(
            expense_date,
            expense.amount,
            expense.category,
            expense.notes
        )
    return {"message": f"Expense recorded for {expense_date}"}

@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_expenses_dates_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Internal Server Error")

    total = sum([row['total'] for row in data])

    new_data = {}
    for row in data:
        percentage = (row['total'] / total) * 100 if total != 0 else 0
        new_data[row['category']] = {
            "total": row["total"],
            "percentage": percentage
        }

    return new_data

