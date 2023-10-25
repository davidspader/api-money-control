from sqlalchemy.orm import Session
from app.db.models import Category as CategoryModel
from app.schemas.category import Category

class CategoryUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_category(self, category: Category):
        category = CategoryModel(**category.dict())
        self.db_session.add(category)
        self.db_session.commit()

    def list_categories(self, user_id: int):
        categories = self.db_session.query(CategoryModel).where(CategoryModel.user_id == user_id).all()
        return categories