from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    Generator,
)
from .db.config import init as init_db
from .routes import (
    auth,
    authors,
    books,
)
from .components.tokenizer import init_serializer
from fastapi.middleware import cors
if TYPE_CHECKING:
    from fastapi import (
        FastAPI,
        APIRouter,
    )

__all__ = (
    "configure",
)


def routes_registry() -> Generator[APIRouter, None, None]:
    yield auth.router
    yield authors.router
    yield books.router


def configure(app: FastAPI, db_url: str, secret_key: str, origins: tuple[str]) -> None:
    """ Configuring Application. """

    # Initialize database connection
    init_db(db_url)

    # Initialize tokens serializer
    init_serializer(secret_key)

    # Add middlewares
    app.add_middleware(
        cors.CORSMiddleware,
        allow_origins=list(origins),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register routers
    for route in routes_registry():
        app.include_router(route)
