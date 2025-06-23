import sys,os
from fastapi import FastAPI, HTTPException, Depends,Query
from fastapi.middleware.cors import CORSMiddleware
from database_table_models import *
from db import *  # Import database module
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text

app = FastAPI()
# CORS configuration
origins = [
    "http://localhost:3000",
"*"
] # IF GETTING AN ERROR REMOVE * IF STILL GETTING AN ERRROR RUN NPM INSTALL NPM RUN DEV AND CHECK WHAT THE LOCALHOST URL IS 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/database-status")
def check_database_status():
    try:
        print("Checking database status...")
        with get_db_context() as connection:
            result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table';")).fetchall()
            print(f"Tables in database: {result}")
            return {"tables": [row[0] for row in result]}  # Extract table names from the result
    except Exception as e:
        print(f"Error checking database status: {e}")
        raise HTTPException(status_code=500, detail="Database connection failed")

@app.get("/traders")
def fetch_all_traders():
    try:
        with get_db_context() as db:
            return get_all_traders(db)
    except Exception as e:
        print(f"Error fetching traders: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/traders/{trader_id}")
def fetch_trader_by_id(trader_id: int):
    try:
        with get_db_context() as db:
            return get_trader_by_id(db, trader_id)
    except Exception as e:
        print(f"Error fetching trader: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/managers")
def fetch_all_managers():
    try:
        with get_db_context() as db:
            return get_all_managers(db)
    except Exception as e:
        print(f"Error fetching managers: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/managers/{manager_id}")
def fetch_manager_by_id(manager_id: int):
    try:
        with get_db_context() as db:
            return get_manager_by_id(db, manager_id)
    except Exception as e:
        print(f"Error fetching manager: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/managers/{manager_id}/traders")
def fetch_traders_by_manager(manager_id: int):
    try:
        with get_db_context() as db:
            return get_traders_by_manager(db, manager_id)
    except Exception as e:
        print(f"Error fetching traders by manager: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/managers/{manager_id}/employee-count")
def fetch_employee_count_by_manager(manager_id: int):
    try:
        with get_db_context() as db:
            return get_employee_count_by_manager(db, manager_id)
    except Exception as e:
        print(f"Error fetching employee count: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/traders/{trader_id}/sell-prices")
def fetch_transaction_sell_prices(trader_id: int):
    try:
        with get_db_context() as db:
            return get_transaction_sell_prices_by_trader(db, trader_id)
    except Exception as e:
        print(f"Error fetching transaction sell prices: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/traders/{trader_id}/purchase-prices")
def fetch_transaction_purchase_prices(trader_id: int):
    try:
        with get_db_context() as db:
            return get_transaction_purchase_prices_by_trader(db, trader_id)
    except Exception as e:
        print(f"Error fetching transaction purchase prices: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/traders/{trader_id}/profits")
def fetch_transaction_profits(trader_id: int):
    try:
        with get_db_context() as db:
            return get_transaction_profits_by_trader(db, trader_id)
    except Exception as e:
        print(f"Error fetching transaction profits: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/traders/{trader_id}/types")
def fetch_transaction_types(trader_id: int):
    try:
        with get_db_context() as db:
            return get_transaction_types_by_date(db, trader_id)
    except Exception as e:
        print(f"Error fetching transaction types: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/traders/{trader_id}/sell-dates")
def fetch_transaction_sell_dates(trader_id: int):
    try:
        with get_db_context() as db:
            return get_transaction_sell_dates_by_trader(db, trader_id)
    except Exception as e:
        print(f"Error fetching transaction sell dates: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")