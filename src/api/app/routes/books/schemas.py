from pydantic import BaseModel
from typing import List
import datetime


# Book schema

class BookBaseSchema(BaseModel):
    title: str
    pages: int


class BookCreateSchema(BookBaseSchema):
    author_id: int


class BookEditSchema(BookBaseSchema):
    pass


class BookSchema(BookBaseSchema):
    id: int

    class Config:
        from_attributes = True


class BookResponseSchema(BookBaseSchema):
    id: int
    author_id: int

    class Config:
        from_attributes = True


class BooksSchema(BaseModel):
    books: List[BookResponseSchema]
