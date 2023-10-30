import pytest
from fastapi.exceptions import HTTPException
from app.use_cases.category import CategoryUseCases
from app.db.models import Category as CategoryModel
from app.schemas.category import Category

def test_add_category_use_case(db_session, user_on_db):
    uc = CategoryUseCases(db_session)

    category = Category(
        name='category name',
        user_id=user_on_db.id
    )

    uc.add_category(category=category)
    categories = db_session.query(CategoryModel).all()

    assert len(categories) == 1
    assert categories[0].name == 'category name'
    assert categories[0].user_id == user_on_db.id

    db_session.delete(categories[0])
    db_session.commit()

def test_list_categories(db_session, categories_on_db):
    user_id = categories_on_db[1].id
    categories_on_db = categories_on_db[2]

    uc = CategoryUseCases(db_session=db_session)
    categories = uc.list_categories(user_id=user_id)

    assert len(categories) == 4
    assert categories[0].name == 'category 1'
    assert categories[0].user_id == user_id
    assert categories[1].name == 'category 2'
    assert categories[1].user_id == user_id
    assert categories[2].name == 'category 3'
    assert categories[2].user_id == user_id
    assert categories[3].name == 'category 4'
    assert categories[3].user_id == user_id

def test_delete_category(db_session,categories_on_db):
    user = categories_on_db[1]
    categories_on_db = categories_on_db[2]

    assert len(categories_on_db) == 4

    uc = CategoryUseCases(db_session=db_session)
    uc.delete_category(category_id=categories_on_db[0].id, user_id=user.id)

    categories_on_db = uc.list_categories(user_id=user.id)

    assert len(categories_on_db) == 3