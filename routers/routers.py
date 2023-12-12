from fastapi import APIRouter, HTTPException
from fastapi.exceptions import ValidationException
from database.connection import collection_name
from database.logic import list_serial
from schemes.schemes import Todo
from bson import ObjectId
from bson.errors import InvalidId

todo_router = APIRouter()


@todo_router.get("/")
async def list_of_todos():
    todo_list = list_serial(collection_name.find())
    return todo_list


@todo_router.post("/")
async def create_todo(data: Todo):
    collection_name.insert_one(data.model_dump())

    return {"success"}


@todo_router.put("/{id}")
async def update_todo(id: str, data: Todo):
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": data.model_dump()}
    )

    return {"success"}


@todo_router.delete("/{id}")
async def delete_todo(id: str):
    try:
        collection_name.find_one({"_id": ObjectId(id)})
    except InvalidId:
        return {"message": "not found"}
    collection_name.find_one_and_delete({"_id": ObjectId(id)})

    return {"message": "delete success"}
