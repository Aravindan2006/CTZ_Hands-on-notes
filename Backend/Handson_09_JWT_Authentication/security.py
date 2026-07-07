"""
security.py — Hands-On 9, Task 1 & 2
Password hashing (bcrypt via passlib) and JWT creation/validation (python-jose).

Why bcrypt over MD5/SHA-256 for passwords:
MD5 and SHA-256 are designed to be FAST — great for checksums, terrible for
passwords, because that speed lets an attacker try billions of guesses per
second on a leaked hash. bcrypt has a tunable "work factor" that
deliberately slows down hashing, making brute-force and rainbow-table
attacks computationally expensive, and it automatically salts each hash.
"""
from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import jwt, JWTError
from passlib.context import CryptContext

SECRET_KEY = "dev-secret-key-change-in-production-09"  # move to env var in real deployments
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """Hash a plain-text password using bcrypt. Never store the plain text."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> dict:
    """Raises JWTError if the token is invalid or expired."""
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
