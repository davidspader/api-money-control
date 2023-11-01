import pytest
from fastapi.exceptions import HTTPException
from app.db.models import Expense as ExpenseModel
from app.schemas.expense import Expense
from app.use_cases.expense import ExpenseUseCases

def test_add_expense_uc(db_session, category_on_db):
    category = category_on_db[2]

    uc = ExpenseUseCases(db_session=db_session)

    expense = Expense(
        description='Expense description',
        value=99.99
    )

    uc.add_expense(expense=expense, category_id=category.id)

    expense_on_db = db_session.query(ExpenseModel).first()

    assert expense_on_db is not None
    assert expense_on_db.description == expense.description
    assert expense_on_db.value == expense.value
    assert expense_on_db.category.name == category.name

    db_session.delete(expense_on_db)
    db_session.commit()

def test_add_expense_uc_invalid_category_id(db_session):
    uc = ExpenseUseCases(db_session=db_session)

    expense = Expense(
        description='Expense description',
        value=99.99
    )

    with pytest.raises(HTTPException):
        uc.add_expense(expense=expense, category_id=1)
