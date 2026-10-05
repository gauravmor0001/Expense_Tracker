from fastapi import FastAPI
from app.database import engine, Base
from app import models 
from app.routers.auth import router as auth_router
# Automatically generates tables in Neon based on your models.py
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker")

@app.get("/")
def root():
    return {"status": "FastAPI successfully connected to Neon Postgres"}

app.include_router(auth_router)