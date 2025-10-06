from backend import db_helper

def test_fetch_expenses_for_valid_date_():
    expenses = db_helper.fetch_expenses_for_date('2025-05-22')

    assert len(expenses) == 1
    assert expenses[0]['amount'] == 720
    assert expenses[0]['category'] == 'food'
    assert expenses[0]['notes'] == 'vegetable'

def test_fetch_expenses_for_valid_date_multiple_data():
    expenses = db_helper.fetch_expenses_for_date('2024-08-02')

    assert len(expenses) == 6
    assert expenses[1]['amount'] == 150
    assert expenses[3]['category'] == 'Entertainment'
    assert expenses[4]['notes'] == 'Clothes'

def test_fetch_expenses_for_invalid_date():
    expenses = db_helper.fetch_expenses_for_date('2099-03-18')

    assert len(expenses) == 0

def test_fetch_expenses_for_valid_date_():
    expenses = db_helper.fetch_expenses_for_date('2025-05-22')

    assert len(expenses) == 1
    assert expenses[0]['amount'] == 720
    assert expenses[0]['category'] == 'food'
    assert expenses[0]['notes'] == 'vegetable'

def test_fetch_expenses_dates_summary():
    summary  = db_helper.fetch_expenses_dates_summary('2024-09-05','2024-09-30' )
    summary_dict = {row['category']: row['total'] for row in summary}

    assert summary_dict['Food'] == 290
    assert summary_dict['Entertainment'] == 115
