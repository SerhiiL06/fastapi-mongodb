from typing import Any, Dict, Optional
from typing_extensions import Annotated, Doc
from fastapi import status
from fastapi.exceptions import HTTPException


class UserAbsent(HTTPException):
    DEFAULT_ERROR = status.HTTP_400_BAD_REQUEST

    def __init__(self, status_code: int = DEFAULT_ERROR, detail: Any = None) -> None:
        super().__init__(status_code, detail)
