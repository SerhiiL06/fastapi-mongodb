from database.connection import user
from database.logic import retrieve_user_serial, list_of_user_serial
from .schemes import RegisterUser, LoginUser, BaseModel
from .logic import UserManager
from .authentication import UserAuth
from fastapi import APIRouter, HTTPException, Response
from fastapi import status, Depends
from typing import Annotated, List


users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.post("/register")
async def create_user(data: RegisterUser):
    user_check = UserManager()

    user_check.create_user(data)

    return Response(content="success", status_code=status.HTTP_201_CREATED)


@users_router.post("/login")
async def login(data: LoginUser):
    auth_proccess = UserAuth()

    auth_proccess.login_user(data)

    return Response(status_code=status.HTTP_200_OK, content="success")


@users_router.get("/user-list")
async def users_all():
    object_list = list_of_user_serial(user.find())
    return object_list
