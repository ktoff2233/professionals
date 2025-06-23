import sys,os
from fastapi import FastAPI, HTTPException, Depends,Query
from fastapi.middleware.cors import CORSMiddleware
from database.db import *
from sqlalchemy.exc import SQLAlchemyError
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

@app.post("/login")
async def login(id: str = Query(...), password: str = Query(...)):
    # Add your authentication logic here
    return {"message": "Login successful"}

@app.get("/traders/{trader_id}")
async def get_trader(trader_id: int):
    try:
        with get_db_context() as db:
            traders = db.query(Trader).filter_by(id=trader_id).all()
            return [{"id": trader.id, "fname": trader.fname, "lname": trader.lname, "score": trader.score, "manager_id": trader.manager_id} for trader in traders]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

