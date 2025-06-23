from sqlalchemy import create_engine, Column, Integer, String
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
import os
from contextlib import contextmanager
from requests import Session
from database_table_models import Base, Trader, Manager, Transaction, PositionEnum, Login
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timedelta
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


def get_transaction_sell_prices_by_trader(db: Session, trader_id):
    """
    Fetch a list of transaction sell prices for a specific trader, arranged by sell date.
    :param db: Database session
    :param trader_id: ID of the trader
    :return: List of sell prices arranged by sell date
    """
    try:
        transactions = (
            db.query(Transaction.sell_price)
            .filter(Transaction.trader_id == trader_id, Transaction.sell_price.isnot(None))
            .order_by(Transaction.sell_date.asc())
            .all()
        )
        db.commit()
        return [transaction.sell_price for transaction in transactions]
    except SQLAlchemyError as e:
        db.rollback()
        print(f"SQLAlchemyError occurred: {str(e)}")
    except Exception as e:
        db.rollback()
        print(f"An unexpected error occurred: {str(e)}")
        
def get_transaction_purchase_prices_by_trader(db: Session, trader_id):
    """
    Fetch a list of transaction purchase prices for a specific trader, arranged by purchase date in ascending order.
    :param db: Database session
    :param trader_id: ID of the trader
    :return: List of purchase prices arranged by purchase date in ascending order
    """
    try:
        transactions = (
            db.query(Transaction.purchase_price)
            .filter(Transaction.trader_id == trader_id, Transaction.purchase_price.isnot(None))
            .order_by(Transaction.purchase_date.asc())  # Explicitly set ascending order
            .all()
        )
        db.commit()
        return [transaction.purchase_price for transaction in transactions]
    except SQLAlchemyError as e:
        db.rollback()
        print(f"SQLAlchemyError occurred: {str(e)}")
    except Exception as e:
        db.rollback()
        print(f"An unexpected error occurred: {str(e)}")

def get_transaction_profits_by_trader(db: Session, trader_id):
    """
    Fetch a list of profits (sell price - purchase price) for a specific trader's transactions,
    arranged by sell date in ascending order. Transactions with NULL sell_date or sell_price are excluded.
    :param db: Database session
    :param trader_id: ID of the trader
    :return: List of profits arranged by sell date in ascending order
    """
    try:
        transactions = (
            db.query(Transaction.sell_price, Transaction.purchase_price)
            .filter(
                Transaction.trader_id == trader_id,
                Transaction.sell_price.isnot(None),
                Transaction.purchase_price.isnot(None),
                Transaction.sell_date.isnot(None)  # Exclude transactions with NULL sell_date
            )
            .order_by(Transaction.sell_date.asc())  # Explicitly set ascending order
            .all()
        )
        db.commit()
        return [transaction.sell_price - transaction.purchase_price for transaction in transactions]
    except SQLAlchemyError as e:
        db.rollback()
        print(f"SQLAlchemyError occurred: {str(e)}")
    except Exception as e:
        db.rollback()
        print(f"An unexpected error occurred: {str(e)}")
        
def get_transaction_types_by_date(db: Session, trader_id):
    """
    Fetch a list of transaction types (position) for a specific trader, arranged by purchase date in ascending order.
    :param db: Database session
    :param trader_id: ID of the trader
    :return: List of transaction types (actual values) arranged by purchase date in ascending order
    """
    try:
        transactions = (
            db.query(Transaction.position)
            .filter(Transaction.trader_id == trader_id)
            .order_by(Transaction.purchase_date.asc())  # Explicitly set ascending order
            .all()
        )
        db.commit()
        return [transaction.position.value for transaction in transactions]  # Extract actual values from PositionEnum
    except SQLAlchemyError as e:
        db.rollback()
        print(f"SQLAlchemyError occurred: {str(e)}")
    except Exception as e:
        db.rollback()
        print(f"An unexpected error occurred: {str(e)}")
def get_transaction_sell_dates_by_trader(db: Session, trader_id):
    """
    Fetch a list of sell dates for a specific trader's transactions, arranged by sell date in ascending order.
    Transactions with NULL sell_date are excluded. Dates are formatted as day-month-year.
    :param db: Database session
    :param trader_id: ID of the trader
    :return: List of sell dates formatted as day-month-year, arranged by sell date in ascending order
    """
    try:
        transactions = (
            db.query(Transaction.sell_date)
            .filter(Transaction.trader_id == trader_id, Transaction.sell_date.isnot(None))  # Exclude NULL sell_date
            .order_by(Transaction.sell_date.asc())  # Explicitly set ascending order
            .all()
        )
        db.commit()
        return [transaction.sell_date.strftime("%d-%m-%Y") for transaction in transactions]  # Format dates
    except SQLAlchemyError as e:
        db.rollback()
        print(f"SQLAlchemyError occurred: {str(e)}")
    except Exception as e:
        db.rollback()
        print(f"An unexpected error occurred: {str(e)}")
        
with get_db_context() as db:
    trader_id = 1  # Replace with the desired trader ID
    sell_dates = get_transaction_sell_dates_by_trader(db, trader_id)
    print(sell_dates)