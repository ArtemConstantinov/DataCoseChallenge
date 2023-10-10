from pydantic import BaseModel
import datetime

# Authentication schemas

class LoginSchema(BaseModel):
    username: str
    password: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class TokenPayloadSchema(BaseModel):
    username: str


class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    created: datetime.datetime
    updated: datetime.datetime


class UserInDBSchema(UserSchema):
    password: str