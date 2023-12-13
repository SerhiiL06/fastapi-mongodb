from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CategoryScheme(BaseModel):
    title: str


class PostScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    description: str
    image: Optional[str] = Field(None)
    publish: bool
    author: str = None


class ReadPost(PostScheme):
    id: str


class CreateUpdatePost(PostScheme):
    pass
