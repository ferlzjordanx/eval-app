from datetime import datetime, timedelta, timezone
import asyncio

import jwt
from fastapi import HTTPException

from src.middleware.auth import add_user_context_headers, verify_jwt_token


JWT_SECRET = "test-secret-that-is-long-enough-for-hs256"


def test_verify_jwt_token_returns_user_context():
    token = jwt.encode(
        {
            "sub": "7",
            "email": "trainer@example.com",
            "role": "TRAINER",
            "exp": datetime.now(timezone.utc) + timedelta(minutes=5),
        },
        JWT_SECRET,
        algorithm="HS256",
    )

    user_context = asyncio.run(verify_jwt_token(f"Bearer {token}"))

    assert user_context == {
        "user_id": "7",
        "email": "trainer@example.com",
        "role": "TRAINER",
    }


def test_verify_jwt_token_rejects_missing_header():
    try:
        asyncio.run(verify_jwt_token(None))
    except HTTPException as exc:
        assert exc.status_code == 401
    else:
        raise AssertionError("Expected missing Authorization header to be rejected")



def test_add_user_context_headers_preserves_existing_headers():
    headers = add_user_context_headers(
        {"accept": "application/json"},
        {"user_id": "7", "email": "trainer@example.com", "role": "TRAINER"},
    )

    assert headers["accept"] == "application/json"
    assert headers["X-User-Id"] == "7"
    assert headers["X-User-Email"] == "trainer@example.com"
    assert headers["X-User-Role"] == "TRAINER"
