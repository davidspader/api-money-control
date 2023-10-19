from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from fastapi.exceptions import HTTPException
from fastapi import status
from app.schemas.user import User
from app.db.models import User as UserModel

cryptContext = CryptContext(schemes=['sha256_crypt'])

class UserUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def register_user(self, user: User):
        new_user = UserModel(
            username=user.username,
            password=cryptContext.hash(user.password)
        )

        self.db_session.add(new_user)

        try:
            self.db_session.commit()
        except IntegrityError:
            self.db_session.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Username already exists'
            )