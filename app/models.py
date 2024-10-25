# app/models.py

from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings

client = AsyncIOMotorClient(settings.MONGO_URI)
database = client[settings.DATABASE_NAME]
blog_posts_collection = database["blog_posts"]
