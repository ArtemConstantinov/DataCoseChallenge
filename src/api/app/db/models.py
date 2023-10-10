from __future__ import annotations
from datetime import (
    datetime,
    timedelta,
)
from typing import List, Type
from typing_extensions import Self
from sqlalchemy import (
    ForeignKey,
    select,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
    DeclarativeBase,
)

from .models_mixins import ActionsMixin


class Base(AsyncAttrs, DeclarativeBase):
    """Base models class"""
    pass


class Book(Base, ActionsMixin):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(index=True)
    pages: Mapped[int] = mapped_column(index=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(back_populates="books", lazy="selectin")


class Author(Base, ActionsMixin):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(index=True)
    books: Mapped[List["Book"]] = relationship(back_populates="author", lazy="selectin", cascade="all, delete-orphan")

    @property
    def num_books(self) -> int:
        return len(self.books)


class User(Base, ActionsMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, index=True)
    password_hash: Mapped[str]
    created: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)
    tokens: Mapped[List["Token"]] = relationship(back_populates="user", lazy="selectin", cascade="all, delete-orphan")

    @classmethod
    async def get_by_username(cls: Type[Self], session: AsyncSession, username: str) -> User | None:
        statment = select(cls).where(cls.username == username)
        result = await session.execute(statment)
        return result.scalars().first()


class Token(Base, ActionsMixin):
    __tablename__ = "tokens"

    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str] = mapped_column(unique=True, index=True)
    created: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    expire: Mapped[datetime] = mapped_column(default=lambda: datetime.utcnow() + timedelta(days=7))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="tokens", lazy="selectin")

    @property
    def is_expired(self) -> bool:
        return self.expire < datetime.now()

    @classmethod
    async def get_by_token(cls: Type[Self], session: AsyncSession, token: str) -> Self | None:
        statment = select(cls).where(cls.token == token)
        result = await session.execute(statment)
        token_obj = result.scalars().first()
        if not token_obj or token_obj.is_expired:
            return None
        return token_obj

    @classmethod
    async def get_user(cls: Type[Self], session: AsyncSession, token: str) -> User | None:
        if token_obj := await cls.get_by_token(session, token):
            return token_obj.user
        return None
