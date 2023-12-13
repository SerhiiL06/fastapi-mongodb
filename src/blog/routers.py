from bson import ObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, HTTPException, Query, Response, status

from database.connection import category, post
from database.serializers import list_serial, retrieve_post_serial
from src.users.authentication import current_user

from .schemes import CategoryScheme, CreateUpdatePost, ReadPost

blog_router = APIRouter()


@blog_router.get("/")
async def get_post_list(user: current_user, is_pub: bool = Query(None)):
    if user.get("role") != "admin":
        raise HTTPException(
            status_code=403, detail="you don't have permissions for this"
        )
    result = list_serial(post.find())

    if bool is not None:
        result = list_serial(post.find({"publish": is_pub}))

    return result


@blog_router.get("/{id}", response_model=ReadPost)
async def get_retrieve_post(id: str):
    try:
        result = retrieve_post_serial(category.find_one({"_id": ObjectId(id)}))

    except InvalidId:
        raise HTTPException(status_code=404, detail="not found")

    return Response(status_code=status.HTTP_200_OK, content={"post_list": result})


@blog_router.post("/")
async def create_post(data: CreateUpdatePost, user: current_user):
    if not data.image:
        del data.image

    data.author = user.get("email")

    post.insert_one(data.model_dump())

    return Response(content="create", status_code=status.HTTP_201_CREATED)


@blog_router.delete("/{id}")
async def delete_post(id: str):
    post.find_one_and_delete({"_id": id})

    return Response(
        content={"message": "delete success"}, status_code=status.HTTP_204_NO_CONTENT
    )
