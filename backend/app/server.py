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

@app.get("/get_traders")
def get_traders(db: Session = Depends(get_db)):
    try:
        traders = db.query(Trader).all()
        return traders
    except Exception as e:
        print(f"Error fetching traders: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")