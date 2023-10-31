from  pydantic import field_validator
from app.schemas.base import CustomBaseModel

class Expense(CustomBaseModel):
    description: str
    value: float

class ExpenseInput(CustomBaseModel):
    category_id: int
    expense: Expense