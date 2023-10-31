from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.schemas.expense import ExpenseInput
from app.routes.deps import get_db_session, auth
from app.use_cases.expense import ExpenseUseCases

router = APIRouter(prefix='/expense', tags=['Expenses'], dependencies=[Depends(auth)])

@router.post('/add', status_code=status.HTTP_201_CREATED, description='Add new expense')
def add_expenses(
    expense_input: ExpenseInput,
    db_session: Session = Depends(get_db_session)
):
    uc = ExpenseUseCases(db_session=db_session)
    uc.add_expense(
        expense=expense_input.expense,
        category_id=expense_input.category_id
    )

    return Response(status_code=status.HTTP_201_CREATED)