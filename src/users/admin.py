from bson import ObjectId
from fastapi import APIRouter

from database.connection import user as user_collections
from database.serializers import list_of_user_serial, retrieve_user_serial

from .authentication import current_user
from .exceptions import UserAbsent
from .logic import check_admin_role

admin_users = APIRouter(prefix="/users/admin", tags=["admin-users"])


@admin_users.get("/users-list")
async def user_list(user: current_user):
    check_admin_role(user)

    object_list = list_of_user_serial(user_collections.find())

    return object_list


@admin_users.get("/users-list/{id}")
async def retrieve_user(id: str, user: current_user):
    check_admin_role(user)

    retrieve_user = user_collections.find_one({"_id": ObjectId(id)})

    if not retrieve_user:
        raise UserAbsent(detail="User with this id doesn't exists")

    return retrieve_user_serial(retrieve_user)
