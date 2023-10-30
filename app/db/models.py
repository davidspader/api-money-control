from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)

class Category(Base):
    __tablename__ = 'categories'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    user_id = Column('user_id', ForeignKey('users.id'), nullable=False)
    expenses = relationship('Expense', back_populates='category')

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    description = Column('description', String, nullable=False)
    value = Column('value', Float)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, onupdate=func.now())
    category_id = Column('category_id', ForeignKey('categories.id'), nullable=False)
    category = relationship('Category', back_populates='expenses')
