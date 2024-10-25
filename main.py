# app/main.py

from fastapi import FastAPI
from .routes import router

app = FastAPI()

app.include_router(router, prefix="/posts", tags=["Blog Posts"])

@app.get("/")
def root():
    return {"message": "Welcome to the School Blog API"}
