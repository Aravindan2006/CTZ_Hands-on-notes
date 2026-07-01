"""
auth.py — Hands-On 9, Task 1 & 2
Registration, login, and the get_current_user dependency used to protect routes.

------------------------------------------------------------------------------
OAuth2 Authorization Code flow vs this simple JWT login (Task 2, Step 95)
------------------------------------------------------------------------------
The Authorization Code flow (full OAuth2) involves: the client redirecting
the user to an Authorization Server's login page, the user authenticating
there (never sharing credentials with the client app), the Auth Server
redirecting back with a short-lived "authorization code", and the client
exchanging that code (server-to-server, with a client secret) for an
access token — optionally also a refresh token.

Our implementation here is the simpler "Resource Owner Password" style flow:
the client sends the email/password DIRECTLY to our own API, which verifies
them and issues a JWT immediately. This is fine for a first-party API you
own, but should never be used for third-party "Login with X" integrations,
where the Authorization Code flow protects the user's credentials from ever
touching the client application.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from models import User
from schemas import UserRegister, UserResponse, UserLogin, Token
from security import get_password_hash, verify_password, create_access_token, decode_access_token

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login/")


@router.post("/register/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(payload: UserRegister, db: AsyncSession = Depends(get_db)):
    existing = await db.execute(select(User).where(User.email == payload.email))
    if existing.scalars().first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    user = User(email=payload.email, hashed_password=get_password_hash(payload.password))
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


@router.post("/login/", response_model=Token)
async def login(payload: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == payload.email))
    user = result.scalars().first()
    if user is None or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")

    token = create_access_token({"sub": user.email})
    return Token(access_token=token)


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_access_token(token)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    result = await db.execute(select(User).where(User.email == email))
    user = result.scalars().first()
    if user is None:
        raise credentials_exception
    return user
