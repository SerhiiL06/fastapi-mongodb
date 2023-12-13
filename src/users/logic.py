from datetime import datetime

from fastapi import HTTPException, status

from database.connection import user

from .exceptions import NotAdmin, UserAbsent
from .password import HashedPassword, PasswordIncorrect


class UserManager:
    __password_operations = HashedPassword()

    def create_user(self, user_data, superuser=False):
        self.check_exists_user(user_data.email)
        correct_password = self.comparison_password(
            user_data.password1, user_data.password2
        )

        hash_password = self.__password_operations.create_hash_password(
            correct_password
        )

        if superuser:
            role = "admin"

        else:
            role = "default"

        user.insert_one(
            {
                "email": user_data.email,
                "password": hash_password,
                "role": role,
                "created": datetime.utcnow(),
            }
        )

        return True

    @classmethod
    def check_exists_user(cls, email):
        user_exists = user.find_one({"email": email})

        if user_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="user with this email already exists",
            )

    @classmethod
    def comparison_password(cls, password1, password2):
        if password1 != password2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="password must be same"
            )

        return password1


def check_admin_role(data: dict):
    if data.get("role") != "admin":
        raise NotAdmin(detail="you don't have permissions for this action")
