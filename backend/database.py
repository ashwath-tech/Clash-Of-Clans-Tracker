from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from backend.config import settings
from sqlalchemy_utils import database_exists, create_database

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()