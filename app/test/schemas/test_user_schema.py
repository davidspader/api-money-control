import pytest
from app.schemas.user import User

def test_user_schema():
    user = User(username='username', password='pass#')
    assert user.dict() == {
        'username': 'username',
        'password': 'pass#'
    }

def test_user_schema_invalid_username():
    with pytest.raises(ValueError):
        User(username='username#', password='pass#')