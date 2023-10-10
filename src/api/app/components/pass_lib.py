from __future__ import annotations

"""Password related helper functions."""
import asyncio
import random
import string

from concurrent.futures import ProcessPoolExecutor
import passlib.hash as pass_hash
from typing import Awaitable


def validate_pwd(pwd: str | bytes, pwd_hash: str | bytes) -> Awaitable[bool]:
    """ Run password validation in to the executor """
    with ProcessPoolExecutor(1) as worker:
        r = worker.submit(pass_hash.pbkdf2_sha256.verify, pwd, pwd_hash)
        return asyncio.wrap_future(r)


def generate_pwd(length: int) -> str:
    """ Generate password with specified length. """
    gen_list = random.choices(
        f"{string.digits}{string.ascii_letters}",
        k=length
    )
    return "".join(gen_list)


def hash_pwd(pwd: str) -> Awaitable[str]:
    """ Helping tool for hashing passwords """
    with ProcessPoolExecutor(1) as worker:
        r = worker.submit(pass_hash.pbkdf2_sha256.using(rounds=100_000).hash, pwd)
        return asyncio.wrap_future(r)
