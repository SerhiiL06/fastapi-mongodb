from enum import Enum, auto
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr


class Roles(Enum):
    DEFAULT = auto()
    ADMIN = auto()


class BaseUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    email: EmailStr


class RegisterUser(BaseUser):
    password1: str
    password2: str


class LoginUser(BaseUser):
    password: str


class ChangePasswordScheme(BaseModel):
    old_password: str
    new_password1: str
    new_password2: str


class Token(BaseModel):
    access_token: str
    token_type: str
