from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class CategoryScheme(BaseModel):
    title: str


class PostScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    description: str
    image: Optional[str] = Field(None)
    publish: bool


class ReadPost(PostScheme):
    id: str


class CreateUpdatePost(PostScheme):
    pass
