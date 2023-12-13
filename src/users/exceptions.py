from typing import Any, Dict, Optional

from fastapi import status
from fastapi.exceptions import HTTPException
from typing_extensions import Annotated, Doc


class UserAbsent(HTTPException):
    DEFAULT_ERROR = status.HTTP_400_BAD_REQUEST

    def __init__(self, status_code: int = DEFAULT_ERROR, detail: Any = None) -> None:
        super().__init__(status_code, detail)


class NotAdmin(HTTPException):
    DEFAULT_ERROR = status.HTTP_403_FORBIDDEN

    def __init__(self, status_code: int = DEFAULT_ERROR, detail: Any = None) -> None:
        super().__init__(status_code, detail)
