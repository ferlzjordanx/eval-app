from datetime import timedelta

from src.services.auth_service import AuthService


def test_access_token_round_trip():
    token = AuthService.create_access_token(
        {"sub": "42", "email": "learner@example.com", "role": "PARTICIPANT"},
        expires_delta=timedelta(minutes=5),
    )

    payload = AuthService.decode_access_token(token)

    assert payload["sub"] == "42"
    assert payload["email"] == "learner@example.com"
    assert payload["role"] == "PARTICIPANT"
    assert "exp" in payload


def test_password_hash_verification():
    hashed = AuthService.hash_password("password123")

    assert hashed != "password123"
    assert AuthService.verify_password("password123", hashed)
    assert not AuthService.verify_password("wrong-password", hashed)
