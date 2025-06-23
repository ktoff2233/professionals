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

