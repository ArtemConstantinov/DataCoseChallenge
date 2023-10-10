from __future__ import annotations
from typing import Annotated
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Response,
    status,
    Header,
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.components import (
    pass_lib,
    tokenizer,
)
from app.db.config import get_session
from app.db.models import (
    User,
    Token,
)
from . import schemas
from loguru import logger

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/login", response_model=schemas.TokenSchema | None)
async def login(login_data: schemas.LoginSchema, db: AsyncSession = Depends(get_session)) -> schemas.TokenSchema | None:
    err = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="The provided username or password is incorrect.",
    )
    user = await User.get_by_username(db, login_data.username)
    if not user:
        raise err

    pwd_is_valid = await pass_lib.validate_pwd(
        pwd=login_data.password,
        pwd_hash=user.password_hash
    )
    if not pwd_is_valid:
        raise err
    token = tokenizer.generate_signed_token({"username": user.username}, "NoSalt")
    token_obj = Token(token=token, user_id=user.id)
    await token_obj.save(db)
    return schemas.TokenSchema(
        access_token=token,
        token_type="bearer"
    )


@router.delete("/logout")
async def logout(
    authorization: Annotated[str, Header(alias="Authorization")],
    db: AsyncSession = Depends(get_session)
) -> Response:
    token_obj = await Token.get_by_token(db, authorization[7:])
    if not token_obj:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is already logged out. Please log in to perform this action.",
        )
    await token_obj.delete(db)
    return Response()
