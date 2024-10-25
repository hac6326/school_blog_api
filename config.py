# app/config.py

from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "school_blog_db"

settings = Settings()
