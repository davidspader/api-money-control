import pytest
from app.schemas.expense import Expense, ExpenseInput


def test_expense_schema():
    expense = Expense(
        description="Expense description",
        value=99.99,
    )

    assert expense.dict() == {
        "description": "Expense description",
        "value": 99.99,
    }


def test_expense_schema_invalid_value():
    with pytest.raises(ValueError):
        Expense(
            description="Expense description",
            value="invalid",
        )

    with pytest.raises(ValueError):
        Expense(
            description="Expense description",
            value=0,
        )

def test_expense_schema_invalid_description():
    with pytest.raises(ValueError):
        Expense(
            description="",
            value=99.99,
        )


def test_expense_input_schema():
    expense = Expense(
        description="Expense description",
        value=99.99,
    )

    expense_input = ExpenseInput(category_id=1, expense=expense)

    assert expense_input.dict() == {
        "category_id": 1,
        "expense": {
            "description": "Expense description",
            "value": 99.99,
        },
    }
