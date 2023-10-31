from  pydantic import field_validator
from app.schemas.base import CustomBaseModel

class Expense(CustomBaseModel):
    description: str
    value: float

    @field_validator('description')
    def validate_name(cls, value):
        if len(value) == 0:
            raise ValueError("empty description not allowed")
        return value
    
    @field_validator('value')
    def validate_value(cls, value):
        if value <= 0:
            raise ValueError("Invalid value")
        return value

class ExpenseInput(CustomBaseModel):
    category_id: int
    expense: Expense
    