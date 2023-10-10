from typing import (
    AsyncGenerator, 
    Callable,
)
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)

__all__ = (
    "init",
    "get_session"
)

SessionConstructor: Callable[[], AsyncSession] | None = None


def init(url: str) -> None:
    global SessionConstructor
    engine = create_async_engine(url)
    SessionConstructor = async_sessionmaker(engine, expire_on_commit=False, autoflush=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    if not SessionConstructor:
        raise RuntimeError("The session constructor is undefined")

    session = SessionConstructor()
    try:
        yield session
    finally:
        await session.close()
