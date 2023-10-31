import pytest
from app.schemas.expense import Expense, ExpenseInput, ExpenseOutput
from app.schemas.category import CategoryOutput


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


def test_expense_output_schema():
    categoryOutput = CategoryOutput(id=1, name="Category name", user_id=1)

    expense_output = ExpenseOutput(
        description="Expense description", value=99.99, id=1, category=categoryOutput
    )

    assert expense_output.dict() == {
        "id": 1,
        "description": "Expense description",
        "value": 99.99,
        "category": {"id": 1, "name": "Category name", "user_id": 1},
    }
