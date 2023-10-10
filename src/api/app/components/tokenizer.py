from __future__ import annotations
from typing import Any
from itsdangerous import URLSafeTimedSerializer
from itsdangerous.exc import (BadSignature, SignatureExpired)


_serializer: URLSafeTimedSerializer | None = None


def init_serializer(secret_key: str) -> None:
    global _serializer
    _serializer = URLSafeTimedSerializer(secret_key)


def generate_signed_token(data: dict[str, Any], salt: str) -> str:
    global _serializer
    if not _serializer:
        raise RuntimeError("Serializer is not set")
    token = _serializer.dumps(data, salt)
    if isinstance(token, bytes):
        return token.decode()
    return token


def verify_signed_token(token) -> dict[str, Any] | None:
    global _serializer
    if not _serializer:
        raise RuntimeError("Serializer is not set")
    try:
        data = _serializer.loads(token)
    except (BadSignature, SignatureExpired) as e:
        return None
    else:
        return data


# # Example usage
# data_to_encode = {'user_id': 123, 'role': 'admin'}

# # Generate a signed token
# signed_token = generate_signed_token(data_to_encode)
# print(f"Generated Token: {signed_token}")

# # Verify the token
# verified_data = verify_signed_token(signed_token)
# if verified_data:
#     print(f"Verified Data: {verified_data}")
# else:
#     print("Token verification failed.")
