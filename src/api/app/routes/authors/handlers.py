from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.config import get_session
from app.db.models import Author
from app.components.authorization import authorize

from . import schemas


router = APIRouter(
    prefix="/authors",
    tags=["authors"],
    dependencies=[Depends(authorize)],
)


@router.post("/", response_model=schemas.AuthorSchema)
async def create_author(
    author: schemas.AuthorCreateSchema,
    db: AsyncSession = Depends(get_session)
):
    new_author = Author(name=author.name)
    await new_author.save(db)
    return new_author


@router.get("/", response_model=schemas.AuthorsResponseSchema)
async def get_all_authors(db: AsyncSession = Depends(get_session)):
    authors = await Author.get_all(db)
    return {"authors": authors}


@router.get("/{author_id}", response_model=schemas.AuthorSchema)
async def get_author(
    author_id: int,
    db: AsyncSession = Depends(get_session)
):
    if author := await Author.get(db, author_id):
        return author
    raise HTTPException(status_code=404, detail="Author not found.")


@router.put("/{author_id}", response_model=schemas.AuthorSchema)
async def edit_author(
    author_id: int,
    author: schemas.AuthorCreateSchema,
    db: AsyncSession = Depends(get_session)
):
    author_db = await Author.get(db, author_id)
    if not author_db:
        raise HTTPException(status_code=404, detail="Author not found.")
    author_db.name = author.name
    await author_db.save(db)
    return author_db


@router.delete("/{author_id}")
async def delete_author(
    author_id: int,
    db: AsyncSession = Depends(get_session)
):
    if author_db := await Author.get(db, author_id):
        await author_db.delete(db)
        return {"author_id": author_id}
    raise HTTPException(status_code=404, detail="Author not found.")
