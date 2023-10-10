from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.components.authorization import authorize
from app.db.config import get_session
from app.db.models import (
    Author,
    Book,
)
from . import schemas

router = APIRouter(
    prefix="/books",
    tags=["books"],
    dependencies=[Depends(authorize)],
)


@router.post("/", response_model=schemas.BookResponseSchema)
async def create_book(
    book: schemas.BookCreateSchema,
    db: AsyncSession = Depends(get_session)
):
    author = await Author.get(db, book.author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found.")
    new_book = Book(
        title=book.title,
        pages=book.pages,
        author_id=book.author_id
    )
    await new_book.save(db)
    return new_book


@router.get("/", response_model=schemas.BooksSchema)
async def get_all_books(db: AsyncSession = Depends(get_session)):
    books = await Book.get_all(db)
    return {"books": books}


@router.get("/{book_id}", response_model=schemas.BooksSchema)
async def get_book(
    book_id: int,
    db: AsyncSession = Depends(get_session)
):
    if book := await Book.get(db, book_id):
        return book
    raise HTTPException(status_code=404, detail="Book not found.")


@router.put("/{book_id}", response_model=schemas.BookResponseSchema)
async def edit_book(
    book_id: int,
    book: schemas.BookEditSchema,
    db: AsyncSession = Depends(get_session)
):
    db_book = await Book.get(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found.")
    db_book.title = book.title
    db_book.pages = book.pages
    await db_book.save(db)
    return db_book


@router.delete("/{book_id}")
async def delete_book(
    book_id: int,
    db: AsyncSession = Depends(get_session)
):
    if db_book := await Book.get(db, book_id):
        await db_book.delete(db)
        return {"book_id": book_id}
    raise HTTPException(status_code=404, detail="Book not found.")
