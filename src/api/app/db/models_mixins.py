from typing import (
    Iterable,
    Type,
)
from typing_extensions import Self
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class ActionsMixin:
    """Mixin of common queries"""
    id: int | None

    async def save(self, session: AsyncSession) -> None:
        """Add or Update object"""
        if not self.id:
            session.add(self)
        await session.commit()
        await session.refresh(self)

    async def delete(self, session: AsyncSession) -> None:
        """Commit object deletion"""
        await session.delete(self)
        await session.refresh(self)
        await session.commit()

    @classmethod
    async def get(cls: Type[Self], session: AsyncSession, obj_id: int) -> Self | None:
        """Query object by it's ID"""
        statement = select(cls).where(cls.id == obj_id)
        result = await session.execute(statement)
        return result.scalars().first()

    @classmethod
    async def get_all(cls: Type[Self], session: AsyncSession) -> Iterable[Self]:
        """Query all objects"""
        result = await session.execute(select(cls))
        return result.scalars().all()
