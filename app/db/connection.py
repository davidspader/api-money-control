from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = config('DATABASE_URL')

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)