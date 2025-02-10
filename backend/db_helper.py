import mysql.connector
from contextlib import contextmanager
from logging_setup import set_up_logging

logger = set_up_logging("db_helper")

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="neethu@123",
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()


def fetch_expenses_for_date(expense_date):
    logger.info(f"Expenses fetched for date {expense_date} ")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses


def delete_expenses_for_date(expense_date):
    logger.info(f"Expenses deleted for date {expense_date} ")

    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


def insert_expense(expense_date, amount, category, notes):
    logger.info(f"Expenses inserted for date {expense_date} having amount={amount}, category={category}, notes={notes} ")

    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )


def fetch_expenses_between_dates(start,end):
    logger.info(f"Expenses fetched between dates {start}  and {end}")
    with get_db_cursor() as cursor:
        cursor.execute('''
                       SELECT category, SUM(amount) as total from expenses 
                       where expense_date between %s and %s
                       group by category''', (start,end)
                      )
        expenses = cursor.fetchall()
        return expenses


def fetch_expenses_by_month():
    logger.info(f"All expenses fetched grouped by month")
    with get_db_cursor() as cursor:
        cursor.execute('''
                        SELECT  MONTH(expense_date) as month_number,
                        MONTHNAME(expense_date) AS month_name,
                        SUM(amount) AS total
                        FROM expenses 
                        GROUP BY month_number,month_name ;
                       '''
                      )
        expenses = cursor.fetchall()
        logger.info(f"expense fetched is {expenses}")
        return expenses

if __name__ == "__main__":
    pass
    # expenses = fetch_expenses_for_date("2024-08-01")
    # insert_expense("2024-08-25","40","Food","herbal tea")
    # delete_expenses_for_date("2024-08-25")
    # summary  = fetch_expenses_between_dates("2024-08-01","2024-08-05")
    # for record in summary:
        # print(record['category'],record['total'])
