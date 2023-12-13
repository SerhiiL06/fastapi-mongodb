import os
from datetime import datetime, timedelta
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import JWTError

from database.connection import user

from .exceptions import UserAbsent
from .password import HashedPassword, PasswordIncorrect
from .schemes import Token

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
bearer = OAuth2PasswordBearer(tokenUrl="/users/login")


class UserAuth:
    def login_user(self, user_data):
        current_user = self.check_exists_user(user_data.username)

        self.verify_password(user_data.password, current_user.get("password"))

        return self.create_access_token(
            email=current_user["email"], role=current_user["role"]
        )

    @staticmethod
    def authenticate(token: Annotated[str, bearer]):
        if not token:
            raise HTTPException(status_code=401, detail="Token not found")

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        except JWTError:
            raise HTTPException(status_code=401, detail="Token not valid")

        exp_value = data["exp"]
        exp_datetime = datetime.utcfromtimestamp(exp_value)

        if exp_datetime < datetime.utcnow():
            raise HTTPException(status_code=401, detail="Token not valid")

        return {"email": data["email"], "role": data["role"]}

    @classmethod
    def create_access_token(csl, email: str, role: str) -> dict:
        exp = datetime.utcnow() + timedelta(minutes=30)
        payload = {"email": email, "role": role, "exp": exp}

        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        return token

    @classmethod
    def check_exists_user(cls, email):
        user_exists = user.find_one({"email": email})

        if not user_exists:
            raise UserAbsent(detail="user with this email doesn't exists")
        return user_exists

    @classmethod
    def verify_password(cls, secret, hashed):
        bcrypt = HashedPassword()

        if not bcrypt.verify_password(secret, hashed):
            raise PasswordIncorrect(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong Password"
            )


current_user = Annotated[dict, Depends(UserAuth.authenticate)]
