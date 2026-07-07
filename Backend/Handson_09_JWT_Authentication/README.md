# Hands-On 9 — Authentication & Security: JWT, OAuth2 & OWASP

## Project Description
Adds JWT-based authentication to the Course Management API: bcrypt password
hashing, registration, login (issuing a 30-minute JWT), a `get_current_user`
dependency that protects `POST`/`DELETE /api/v1/courses/`, and CORS
configuration for a local frontend.

## Technologies
- Python 3.10+, FastAPI, python-jose, passlib[bcrypt], SQLAlchemy 2.0 (async)

## Installation
```bash
cd Handson_09_JWT_Authentication
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```
> Note: `bcrypt` is pinned to `4.0.1` for compatibility with `passlib`'s bcrypt backend.

## Run Instructions
```bash
uvicorn main:app --reload
```
API base: `http://127.0.0.1:8000/api/v1/`

## Folder Structure
```
Handson_09_JWT_Authentication/
├── main.py           # CORS, auth router included, protected course routes
├── auth.py             # register / login / get_current_user
├── security.py          # bcrypt hashing + JWT create/decode
├── database.py, models.py (+ User model), schemas.py (+ auth schemas)
├── postman/
├── screenshots/
├── requirements.txt
└── .gitignore
```

## Features
- Passwords hashed with bcrypt (never stored/logged in plain text)
- `POST /api/v1/auth/register/` — 409 on duplicate email
- `POST /api/v1/auth/login/` — returns a 30-minute JWT access token
- `get_current_user` dependency — 401 on missing/invalid/expired token
- `POST`/`DELETE /api/v1/courses/` require a valid Bearer token; `GET` is public
- CORS enabled for `http://localhost:3000`

## API Endpoints
| Method | Endpoint                        | Auth required | Description                    |
|--------|-------------------------------------|:---:|-----------------------------------|
| POST   | `/api/v1/auth/register/`            | No  | Create a user (bcrypt-hashed password) |
| POST   | `/api/v1/auth/login/`               | No  | Returns `{access_token, token_type}` |
| GET    | `/api/v1/courses/`                  | No  | List courses                         |
| POST   | `/api/v1/courses/`                  | **Yes** | Create a course                  |
| DELETE | `/api/v1/courses/{id}/`             | **Yes** | Delete a course                  |

## Screenshots
See `screenshots/` folder.

## Learning Outcomes
- Hashed passwords securely with bcrypt and explained why over MD5/SHA-256
- Implemented JWT issuance and validation with `python-jose`
- Protected specific routes using FastAPI dependency injection
- Configured CORS for a browser-based frontend
- Understood how the OAuth2 Authorization Code flow differs from a simple
  first-party JWT login
