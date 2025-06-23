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


## Defining functions:


def get_all_traders(db: Session):
    """Fetch all traders from the database."""
    try:
        traders = db.query(Trader).all()
        db.commit()
        return traders
    except SQLAlchemyError as e:
        db.rollback()
        print(f"SQLAlchemyError occurred: {str(e)}")
    except Exception as e:
        db.rollback()
        print(f"An unexpected error occurred: {str(e)}")

def get_trader_by_id(db: Session, trader_id):
    """Fetch a trader by their ID."""
    try:
        trader = db.query(Trader).get(trader_id)
        db.commit()
        return trader
    except SQLAlchemyError as e:
        db.rollback()
        print(f"SQLAlchemyError occurred: {str(e)}")
    except Exception as e:
        db.rollback()
        print(f"An unexpected error occurred: {str(e)}")

def get_all_managers(db: Session):
    """Fetch all managers from the database."""
    try:
        managers = db.query(Manager).all()
        db.commit()
        return managers
    except SQLAlchemyError as e:
        db.rollback()
        print(f"SQLAlchemyError occurred: {str(e)}")
    except Exception as e:
        db.rollback()
        print(f"An unexpected error occurred: {str(e)}")

def get_manager_by_id(db: Session, manager_id):
    """Fetch a manager by their ID."""
    try:
        manager = db.query(Manager).get(manager_id)
        db.commit()
        return manager
    except SQLAlchemyError as e:
        db.rollback()
        print(f"SQLAlchemyError occurred: {str(e)}")
    except Exception as e:
        db.rollback()
        print(f"An unexpected error occurred: {str(e)}")

def get_traders_by_manager(db: Session, manager_id):
    """Fetch all traders assigned to a specific manager."""
    try:
        traders = db.query(Trader).filter_by(manager_id=manager_id).all()
        db.commit()
        return traders
    except SQLAlchemyError as e:
        db.rollback()
        print(f"SQLAlchemyError occurred: {str(e)}")
    except Exception as e:
        db.rollback()
        print(f"An unexpected error occurred: {str(e)}")

def get_employee_count_by_manager(db: Session, manager_id):
    """Fetch the number of traders assigned to a specific manager."""
    try:
        count = db.query(Trader).filter_by(manager_id=manager_id).count()
        db.commit()
        return count
    except SQLAlchemyError as e:
        db.rollback()
        print(f"SQLAlchemyError occurred: {str(e)}")
    except Exception as e:
        db.rollback()
        print(f"An unexpected error occurred: {str(e)}")


