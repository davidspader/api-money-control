import pytest
from app.schemas.category import Category, CategoryOutput

def test_category_schema():
    category=Category(
        name='category name',
    )

    assert category.dict() == {
        'name': 'category name',
    }

def test_category_schema_invalid_name(user_on_db):
    with pytest.raises(ValueError):
        Category(
            name='',
        )

def test_category_schema_output(user_on_db):
    categoryOutput = CategoryOutput(
        name='category name',
        user_id=user_on_db.id,
        id=1
    )

    assert categoryOutput.dict() == {
        'name': 'category name',
        'user_id': user_on_db.id,
        'id': 1
    }

def test_category_schema__output_invalid_user_id():
    with pytest.raises(ValueError):
        CategoryOutput(
            name='category name',
            user_id='invalid',
            id=1
        )

def test_category_schema_output_invalid_id(user_on_db):
    with pytest.raises(ValueError):
        CategoryOutput(
            name='category name',
            user_id=user_on_db.id,
            id='invalid'
        )