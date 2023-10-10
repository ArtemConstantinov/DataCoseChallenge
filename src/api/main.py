from __future__ import annotations
import os
import fastapi
import uvicorn
from app import app_config


# region Prams
DB_LINK: str = os.environ["DB_LINK"]
LISTNING_PORT: int = 8000
ORIGINS: tuple[str] = (
    "http://localhost:3000",
)
SECRET: str = "2fffmojn2v4fm@_mkm"
# endregion


def start_app() -> fastapi.FastAPI:
    """Entry point of starting app."""
    app = fastapi.FastAPI()
    app_config.configure(
        app=app,
        db_url=DB_LINK,
        secret_key=SECRET,
        origins=ORIGINS
    )
    return app


def restore_db() -> None:
    """Entry point of restoring data from seed file to DB."""
    from app.db.populate import restore_seed_data
    restore_seed_data(DB_LINK)
    print("Data is restored. ")


if __name__ == "__main__":
    uvicorn.run(start_app(), host="0.0.0.0", port=LISTNING_PORT)
