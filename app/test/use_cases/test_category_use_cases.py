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
