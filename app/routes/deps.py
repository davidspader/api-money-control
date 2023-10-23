from fastapi import Depends
from sqlalchemy.orm import Session as SessionSqlAlchemy
from fastapi.security import OAuth2PasswordBearer
from app.db.connection import Session
from app.use_cases.user import UserUseCases

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')

def get_db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()

def auth(
    db_session: SessionSqlAlchemy = Depends(get_db_session),
    token = Depends(oauth_scheme)
):
    uc = UserUseCases(db_session=db_session)
    uc.verify_token(token=token)