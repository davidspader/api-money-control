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
