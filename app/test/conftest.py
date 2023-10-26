import pytest
from decouple import config
from app.db.connection import Session
from passlib.context import CryptContext
from app.db.models import User as UserModel
from app.db.models import Category as CategoryModel
from app.use_cases.user import UserUseCases
from app.schemas.user import User

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
cryptContext = CryptContext(schemes=['sha256_crypt'])

@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()

@pytest.fixture()
def user_on_db(db_session):
    user = UserModel(
        username='username',
        password=cryptContext.hash('pass#')
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    yield user

    db_session.delete(user)
    db_session.commit()

@pytest.fixture()
def another_user_on_db(db_session):
    user = UserModel(
        username='username2',
        password=cryptContext.hash('pass#')
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    yield user

    db_session.delete(user)
    db_session.commit()

@pytest.fixture()
def authentication_token(db_session, user_on_db):
    user = User(
        username=user_on_db.username,
        password='pass#'
    )

    uc = UserUseCases(db_session=db_session)
    token_data = uc.user_login(user=user, expires_in=1)

    headers = {"Authorization": f"Bearer {token_data.access_token}"}

    yield headers

@pytest.fixture()
def categories_on_db(db_session, user_on_db):
    data = [user_on_db.id]
    
    categories = [
        CategoryModel(name='category 1', user_id=user_on_db.id),
        CategoryModel(name='category 2', user_id=user_on_db.id),
        CategoryModel(name='category 3', user_id=user_on_db.id),
        CategoryModel(name='category 4', user_id=user_on_db.id)
    ]

    for category in categories:
        db_session.add(category)
    db_session.commit()

    for category in categories:
        db_session.refresh(category)
    
    data.append(categories)
    
    yield data

    for category in categories:
        db_session.delete(category)
    db_session.commit()