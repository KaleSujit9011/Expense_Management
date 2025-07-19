
from backend import db_helper

def test_fetch_expenses_for_date():
    expenses = db_helper.fetch_expenses_for_date("2024-08-15")
    assert len(expenses) == 1
    assert expenses[0]["category"] == "Shopping"
    assert expenses[0]["amount"] == 10.0

def test_fetch_expenses_for_date_invalid_date():
    expenses = db_helper.fetch_expenses_for_date("9999-08-15")
    assert len(expenses) == 0

def test_delete_expenses_for_date():
    result = db_helper.delete_expenses_for_date("2024-08-15")
    assert result is None  # Assuming successful execution

def test_delete_expenses_for_date_invalid_date():
    result = db_helper.delete_expenses_for_date("9999-08-15")
    assert result is None  # Should not raise an error

def test_insert_expense():
    result = db_helper.insert_expense("2024-08-15", 50.0, "Groceries", "Bought vegetables")
    assert result is None  # Assuming no return value

def test_fetch_expense_summary():
    summary = db_helper.fetch_expense_summary("2024-08-01", "2024-08-15")
    assert len(summary) == 1
    assert summary[0]["category"] == "Groceries"
    assert summary[0]["total"] == 150.0
