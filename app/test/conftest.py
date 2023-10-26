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
def authenticated_user(db_session):
    user = UserModel(
        username='authenticated_user',
        password=cryptContext.hash('pass#')
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    user_login = User(
        username=user.username,
        password='pass#'
    ) 

    uc = UserUseCases(db_session=db_session)
    token_data = uc.user_login(user=user_login, expires_in=1)

    headers = {"Authorization": f"Bearer {token_data.access_token}"}

    data = [headers, user]

    yield data

    db_session.delete(user)
    db_session.commit()

@pytest.fixture()
def categories_on_db(db_session, authenticated_user):
    data = [authenticated_user[0]]
    # user = authenticated_user[1]
    
    categories = [
        CategoryModel(name='category 1', user_id=1),
        CategoryModel(name='category 2', user_id=1),
        CategoryModel(name='category 3', user_id=1),
        CategoryModel(name='category 4', user_id=1)
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