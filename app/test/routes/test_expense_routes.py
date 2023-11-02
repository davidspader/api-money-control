from fastapi.testclient import TestClient
from fastapi import status
from app.db.models import Expense as ExpenseModel
from app.main import app

client = TestClient(app)


def test_add_expense_route(db_session, category_on_db):
    token = category_on_db[0]
    user = category_on_db[1]
    category = category_on_db[2]

    client.headers = token

    body = {
        "user_id": user.id,
        "category_id": category.id,
        "expense": {
            "description": "Expense description", 
            "value": 99.99
        },
    }

    response = client.post("/expense/add", json=body)

    assert response.status_code == status.HTTP_201_CREATED

    expenses_on_db = db_session.query(ExpenseModel).all()

    assert len(expenses_on_db) == 1

    db_session.delete(expenses_on_db[0])
    db_session.commit()

def test_update_expense_route(db_session, expense_on_db):
    token = expense_on_db[0]
    user = expense_on_db[1]
    expense_on_db = expense_on_db[2]

    client.headers = token

    body = {
        'description': 'updated expense description',
        'value': 10.10
    }

    response = client.put(f'/expense/update/{user.id}/{expense_on_db.id}', json=body)

    assert response.status_code == status.HTTP_200_OK

    db_session.refresh(expense_on_db)

    expense_on_db.description == 'updated expense description'
    expense_on_db.value == 10.10

def test_update_expense_route_invalid_id(expense_on_db):
    token = expense_on_db[0]
    user = expense_on_db[1]

    client.headers = token

    body = {
        'description': 'updated expense description',
        'value': 10.10
    }

    response = client.put(f'/expense/update/{user.id}/1', json=body)

    assert response.status_code == status.HTTP_404_NOT_FOUND