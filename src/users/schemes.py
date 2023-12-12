from pydantic import BaseModel, EmailStr, ConfigDict


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
