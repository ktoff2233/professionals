from sqlalchemy import create_engine, Column, Integer, String
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
import os
from contextlib import contextmanager
from requests import Session
from database_table_models import Base, Trader, Manager, Transaction, PositionEnum, Login
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine=create_engine(DATABASE_URL, pool_size=20, max_overflow=20, pool_timeout=30, pool_recycle=1800)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)


def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@contextmanager
def get_db_context():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_db():
    Base.metadata.drop_all(bind=engine)
    init_db()
    print("Database created successfully.")
