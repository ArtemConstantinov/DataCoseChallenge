from fastapi import (
    Depends,
    Header,
    HTTPException,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession
# from starlette.requests import Request

from typing import Annotated
from app.db.config import get_session
from app.db.models import (
    Token, 
    User,
)


async def authorize(
    authorization: Annotated[str, Header(alias="Authorization")], 
    db: AsyncSession = Depends(get_session)
) -> User | None:

    keyword = "Bearer "
    err = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if not authorization.startswith(keyword):
        raise err
    token = authorization[len(keyword):]

    # validate if tocken is signed by our app
    user = await Token.get_user(session=db, token=token)
    if not user:
        raise err
    return user

