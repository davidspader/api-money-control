import pytest
from fastapi.exceptions import HTTPException
from app.db.models import Expense as ExpenseModel
from app.schemas.expense import Expense
from app.use_cases.expense import ExpenseUseCases

def test_add_expense_uc(db_session, category_on_db):
    user = category_on_db[1]
    category = category_on_db[2]

    uc = ExpenseUseCases(db_session=db_session)

    expense = Expense(
        description='Expense description',
        value=99.99
    )

    uc.add_expense(expense=expense, category_id=category.id, user_id=user.id)

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
        uc.add_expense(expense=expense, category_id=1, user_id=1)

def test_update_expense(db_session, expense_on_db):
    user = expense_on_db[1]
    expense = expense_on_db[2]

    expense_to_update = Expense(
        description='updated description',
        value=20.00
    )

    uc = ExpenseUseCases(db_session=db_session)
    uc.update_expense(id=expense.id, expense=expense_to_update, user_id=user.id)

    expense_updated_on_db = db_session.query(ExpenseModel).filter_by(id=expense.id).first()

    assert expense_updated_on_db is not None
    assert expense_updated_on_db.description == expense.description
    assert expense_updated_on_db.value == expense.value

def test_update_expense_with_invalid_id(db_session, expense_on_db):
    user = expense_on_db[1]

    expense_to_update = Expense(
        description='updated description',
        value=20.00
    )

    uc = ExpenseUseCases(db_session=db_session)

    with pytest.raises(HTTPException):
        uc.update_expense(id=1, expense=expense_to_update, user_id=user.id)