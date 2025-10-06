import pymysql
from pymysql.cursors import DictCursor
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager",
    )

    if connection.open:
        print("Connected to MySQL Server")
    else:
        print("Connection to MySQL server failed")

    cursor = connection.cursor(DictCursor)
    try:
        yield cursor  # give the cursor to the calling code
        if commit:    # ✅ run commit after work is done
            connection.commit()
    finally:
        cursor.close()
        connection.close()

def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expense = cursor.fetchall()
        return expense

def fetch_expenses_for_date(expense_date):
    logger.info(f"Fetch expenses for date: {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            "SELECT * FROM expenses WHERE DATE(expense_date) = %s",
            (expense_date,)
        )
        expense = cursor.fetchall() or []
    return expense

def delete_expenses_for_date(expense_date):
    logger.info(f"Fetch expenses for date: {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("Delete from expenses where expense_date = %s", (expense_date,))

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"Insert expenses for date: {expense_date} with amount: {amount}, category: {category} and notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )

def fetch_expenses_dates_summary(start_date, end_date):
    logger.info(f"Fetch expenses dates summary with start date: {start_date} end: {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            "SELECT category, SUM(amount) AS total "
            "FROM expenses "
            "WHERE expense_date BETWEEN %s AND %s "
            "GROUP BY category",
            (start_date, end_date)
        )
        summary = cursor.fetchall()
    return summary


if __name__ == "__main__":
    #expenses = fetch_all_records()
    #print(expenses)
    fetch_expenses_for_date("2024-08-03")
    #insert_expense("2025-05-22", 720, "food", "vegetable")
    #delete_expenses_for_date("2025-05-22")
    #category_summary = fetch_expenses_dates_summary("2024-09-05","2024-09-30")
    #for record in category_summary:
       # print(record)
    #monthly_summary = fetch_expenses_dates_month("2024-08-01", "2024-09-30")
    #for record in monthly_summary:
      #  print(record)
