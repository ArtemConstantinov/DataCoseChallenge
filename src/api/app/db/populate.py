import asyncio
import json
from typing import (
    Any,
    TypeVar,
    Generator,
)
from pathlib import Path
from sqlalchemy.ext.asyncio import AsyncSession
from . import (
    models,
    config,
)

# For speed up, the seed path is hardcoded, in normal case I will move it outside,
# also MODEL_REGISTRY can be populated with decorator patern instead of hardcoding


__all__ = (
    "populate",
    "restore_seed_data",
)

MODEL_REGISTRY = {
    "users": models.User,
    "authors": models.Author,
    "books": models.Book,
}

T = TypeVar("T", bound=models.Base)
DataType = dict[str, list[dict[str, Any]]]


def read_seed(path: Path = Path(__file__).parent / "seed.json") -> DataType:
    """Read JSON from seed file and convert it to the dict"""
    if not path.is_file():
        raise RuntimeError("Provided Wrong Seed file path")
    with path.open("r") as file:
        return json.loads(file.read())


def parse_data(data: DataType) -> Generator[T, None, None]:
    """Parse dict values and yield  created model object"""
    for model, rows in data.items():
        model_cls = MODEL_REGISTRY.get(model, None)
        if not model_cls:
            continue
        for row in rows:
            if "books" in row:
                books_data = row.pop("books")
                books = list(parse_data({"books": books_data}))
                yield model_cls(books=books, **row)
            else:
                yield model_cls(**row)


async def populate(session: AsyncSession) -> None:
    data = read_seed()
    # We need sequencial execution so no asyncio.gather here
    for model_obj in parse_data(data):
        session.add(model_obj)
    await session.commit()


def restore_seed_data(url: str) -> None:
    """Entry point for restore data."""
    config.init(url)

    async def closure() -> None:
        async for session in config.get_session():
            await populate(session)
    asyncio.run(closure())
