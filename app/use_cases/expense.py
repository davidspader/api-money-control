from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status
from app.db.models import Expense as ExpenseModel
from app.db.models import Category as CategoryModel
from app.schemas.expense import Expense

class ExpenseUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def add_expense(self, expense: Expense, category_id: int, user_id: int):
        category = self.db_session.query(CategoryModel).filter_by(id=category_id, user_id=user_id).first()
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Category not found'
            )
        
        expense_model = ExpenseModel(**expense.dict())
        expense_model.category_id = category_id

        self.db_session.add(expense_model)
        self.db_session.commit()