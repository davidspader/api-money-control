from fastapi.testclient import TestClient
from fastapi import status
from app.db.models import Category as CategoryModel
from app.main import app

client = TestClient(app)

def test_add_category_route(db_session, authenticated_user):
    token = authenticated_user[0]
    user = authenticated_user[1]

    client.headers = token
    
    body = {
        "name": 'category name',
        "user_id": user.id
    }

    response = client.post('/category/add', json=body)

    assert response.status_code == status.HTTP_201_CREATED

    categories = db_session.query(CategoryModel).all()

    assert len(categories) == 1
    db_session.delete(categories[0])
    db_session.commit()

def test_list_categories(categories_on_db):
    token = categories_on_db[0]
    user = categories_on_db[1]
    categories_on_db = categories_on_db[2]

    client.headers = token

    response = client.get(f'/category/list/{user.id}')

    assert response.status_code == status.HTTP_200_OK

    categories = response.json()

    assert len(categories) == 4
    assert categories[0] == {
        "name": categories_on_db[0].name,
        "user_id": categories_on_db[0].user_id,
        "id": categories_on_db[0].id
    }

def test_list_categories_without_user_id(categories_on_db):
    token = categories_on_db[0]
    categories_on_db = categories_on_db[2]

    client.headers = token

    response = client.get(f'/category/list')

    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_delete_category_route(categories_on_db):
    token = categories_on_db[0]
    user = categories_on_db[1]
    categories_on_db = categories_on_db[2]

    client.headers = token

    response = client.delete(f'/category/delete/{user.id}/{categories_on_db[0].id}')

    assert response.status_code == status.HTTP_200_OK

def test_delete_category_route_without_ids(categories_on_db):
    token = categories_on_db[0]

    client.headers = token

    response = client.delete(f'/category/delete')

    assert response.status_code == status.HTTP_404_NOT_FOUND