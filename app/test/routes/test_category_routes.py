from fastapi.testclient import TestClient
from fastapi import status
from app.db.models import Category as CategoryModel
from app.main import app

client = TestClient(app)

def test_add_category_route(db_session, user_on_db, authentication_token):
    client.headers = authentication_token
    
    body = {
        "name": 'category name',
        "user_id": user_on_db.id
    }

    response = client.post('/category/add', json=body)

    assert response.status_code == status.HTTP_201_CREATED

    categories = db_session.query(CategoryModel).all()

    assert len(categories) == 1
    db_session.delete(categories[0])
    db_session.commit()

def test_list_categories(categories_on_db, authentication_token):
    client.headers = authentication_token

    response = client.get('/category/list')

    assert response.status_code == status.HTTP_200_OK

    categories = response.json()

    assert len(categories) == 4
    assert categories[0] == {
        "name": categories_on_db[0].name,
        "user_id": categories_on_db[0].user_id,
        "id": categories_on_db[0].id
    }