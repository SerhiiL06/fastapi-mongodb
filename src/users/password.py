from typing import Any, Dict, Optional

from fastapi import status
from fastapi.exceptions import HTTPException
from passlib.context import CryptContext
from typing_extensions import Annotated, Doc

bcrypt = CryptContext(schemes=["bcrypt"])


class HashedPassword:
    def create_hash_password(self, password):
        psswd = bcrypt.hash(password)
        return psswd

    def verify_password(self, simple_password, hash_password):
        result = bcrypt.verify(simple_password, hash_password)
        return result


class PasswordIncorrect(HTTPException):
    def __init__(self, status_code: int, detail: Any = None) -> None:
        super().__init__(status_code, detail)
