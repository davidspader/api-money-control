from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.schemas.category import Category
from app.routes.deps import get_db_session, auth
from app.use_cases.category import CategoryUseCases

router = APIRouter(prefix='/category', tags=['Category'], dependencies=[Depends(auth)])