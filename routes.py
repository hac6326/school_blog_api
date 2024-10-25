# app/routes.py

from fastapi import APIRouter, HTTPException, status
from .schemas import BlogPostCreate, BlogPost
from .models import blog_posts_collection
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=BlogPost)
async def create_blog_post(post: BlogPostCreate):
    post_dict = post.dict()
    result = await blog_posts_collection.insert_one(post_dict)
    post_dict["_id"] = str(result.inserted_id)
    return post_dict

@router.get("/{id}", response_model=BlogPost)
async def get_blog_post(id: str):
    post = await blog_posts_collection.find_one({"_id": ObjectId(id)})
    if post:
        post["_id"] = str(post["_id"])
        return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@router.get("/", response_model=list[BlogPost])
async def get_all_blog_posts():
    posts = []
    async for post in blog_posts_collection.find():
        post["_id"] = str(post["_id"])
        posts.append(post)
    return posts

@router.put("/{id}", response_model=BlogPost)
async def update_blog_post(id: str, post: BlogPostCreate):
    update_result = await blog_posts_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": post.dict()}
    )
    if update_result.modified_count == 1:
        updated_post = await blog_posts_collection.find_one({"_id": ObjectId(id)})
        updated_post["_id"] = str(updated_post["_id"])
        return updated_post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog_post(id: str):
    delete_result = await blog_posts_collection.delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
