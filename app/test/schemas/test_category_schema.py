import pytest
from app.schemas.category import Category, CategoryOutput, CategoryInput

def test_category_schema():
    category=Category(
        name='category name',
        user_id=1
    )

    assert category.dict() == {
        'name': 'category name',
        'user_id': 1
    }

def test_category_schema_invalid_name():
    with pytest.raises(ValueError):
        Category(
            name='',
            user_id=1
        )

def test_category_schema_invalid_user_id():
    with pytest.raises(ValueError):
        Category(
            name='category name',
            user_id='invalid'
        )

def test_category_schema_output():
    categoryOutput = CategoryOutput(
        name='category name',
        user_id=1,
        id=1
    )

    assert categoryOutput.dict() == {
        'name': 'category name',
        'user_id': 1,
        'id': 1
    }

def test_category_schema_output_invalid_id():
    with pytest.raises(ValueError):
        CategoryOutput(
            name='category name',
            user_id=1,
            id='invalid'
        )

def test_category_schema_input():
    category=CategoryInput(
        name='category name',
    )

    assert category.dict() == {
        'name': 'category name',
    }

def test_category_schema_input_invalid():
    with pytest.raises(ValueError):
        CategoryInput(
            name='',
        )