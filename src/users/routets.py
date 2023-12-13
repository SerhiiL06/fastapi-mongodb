from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from database.connection import user
from database.serializers import list_of_user_serial, retrieve_user_serial

from .authentication import UserAuth, current_user
from .logic import UserManager
from .schemes import BaseModel, LoginUser, RegisterUser, Token

users_router = APIRouter(prefix="/users", tags=["users"])

get_current_user = UserAuth


@users_router.post("/register")
async def create_user(data: RegisterUser):
    user_check = UserManager()

    user_check.create_user(data)

    return Response(content="success", status_code=status.HTTP_201_CREATED)


@users_router.post("/login")
async def login(data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    auth_proccess = UserAuth()

    user_token = auth_proccess.login_user(data)

    return Response(status_code=status.HTTP_200_OK, content=user_token)


@users_router.get("/user-list")
async def users_all(u: current_user):
    object_list = list_of_user_serial(user.find())
    return object_list
