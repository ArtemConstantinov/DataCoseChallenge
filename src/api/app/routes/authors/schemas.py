from pydantic import BaseModel
from typing import List


# Author schema
class AuthorBaseSchema(BaseModel):
    name: str


class AuthorCreateSchema(AuthorBaseSchema):
    pass


class AuthorSchema(AuthorBaseSchema):
    id: int
    num_books: int
    # books: List[BookSchema]

    class Config:
        from_attributes = True


class AuthorsResponseSchema(BaseModel):
    authors: List[AuthorSchema]


class AuthorResponseSchema(AuthorBaseSchema):
    id: int
    num_books: int

    class Config:
        from_attributes = True
