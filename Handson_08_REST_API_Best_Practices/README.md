# Hands-On 8 — RESTful API Design Best Practices

## Project Description
Refactors the FastAPI Course Management API (built in Hands-On 6/7) to
follow REST best practices: URL versioning, plural noun resource naming,
PATCH for partial updates alongside PUT for full replacement, correct
status codes, a `Location` header on creation, DRF-style offset pagination,
search filtering, and a standardised error response envelope.

## Technologies
- Python 3.10+, FastAPI, Uvicorn, SQLAlchemy 2.0 (async), aiosqlite

## Installation
```bash
cd Handson_08_REST_API_Best_Practices
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Run Instructions
```bash
uvicorn main:app --reload
```
API base: `http://127.0.0.1:8000/api/v1/courses/`

## Folder Structure
```
Handson_08_REST_API_Best_Practices/
├── main.py         # versioned, paginated, filtered, PATCH-enabled endpoints
├── database.py
├── models.py
├── schemas.py
├── errors.py         # standardised {"error": {...}} response format
├── postman/
├── screenshots/
├── requirements.txt
└── .gitignore
```

## Features
- **Versioning**: all endpoints under `/api/v1/`
- **PATCH vs PUT**: PATCH updates only supplied fields; PUT replaces the whole resource
- **Location header**: `POST /api/v1/courses/` returns `Location: /api/v1/courses/{id}/`
- **Pagination envelope**: `{"count", "next", "previous", "results"}` (DRF-style)
- **Search filtering**: `?search=` matches course name/code (case-insensitive)
- **Standardised errors**: `{"error": {"code", "message", "field"}}` for all 4xx/422 responses

## API Endpoints
| Method | Endpoint                                        | Description                         |
|--------|----------------------------------------------------|----------------------------------------|
| GET    | `/api/v1/courses/?page=&page_size=&search=`        | Paginated, filterable list             |
| POST   | `/api/v1/courses/`                                  | Create (201 + `Location` header)        |
| GET    | `/api/v1/courses/{id}/`                            | Retrieve (standardised 404 on miss)     |
| PUT    | `/api/v1/courses/{id}/`                            | Full replace                            |
| PATCH  | `/api/v1/courses/{id}/`                            | Partial update                          |
| DELETE | `/api/v1/courses/{id}/`                            | Delete (204 No Content)                 |

## Screenshots
See `screenshots/` folder.

## Learning Outcomes
- Audited and corrected REST resource naming and HTTP method semantics
- Implemented URL-based API versioning and discussed the header-based alternative
- Built offset pagination with a standard response envelope
- Added case-insensitive search filtering
- Standardised error responses across the whole API
