from app.schemas.base import CustomBaseModel

class Category(CustomBaseModel):
    name: str
    user_id: int

class CategoryOutput(Category):
    id: int

    class Config:
        orm_mode=True