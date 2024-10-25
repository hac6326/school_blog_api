# app/schemas.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BlogPostBase(BaseModel):
    title: str
    content: str
    author: str
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

class BlogPostCreate(BlogPostBase):
    pass

class BlogPost(BlogPostBase):
    id: str
