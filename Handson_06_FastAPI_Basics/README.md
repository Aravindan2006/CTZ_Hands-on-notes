# Hands-On 6 — FastAPI: Path Parameters, Pydantic & Async Endpoints

## Project Description
Rebuilds the Course Management API in FastAPI, using Pydantic schemas for
request/response validation, path & query parameters (with pagination and
filtering), and an async SQLAlchemy engine wired in via FastAPI's
dependency injection (`Depends(get_db)`).

## Technologies
- Python 3.10+, FastAPI, Uvicorn, SQLAlchemy 2.0 (async), aiosqlite, Pydantic v2

## Installation
```bash
cd Handson_06_FastAPI_Basics
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Run Instructions
```bash
uvicorn main:app --reload
```
Swagger UI: `http://127.0.0.1:8000/docs`
API base: `http://127.0.0.1:8000/api/courses/`

Sample departments/courses are auto-seeded on startup if the DB is empty.

## Folder Structure
```
Handson_06_FastAPI_Basics/
├── main.py           # FastAPI app, routes, startup seeding
├── database.py         # async engine, session, get_db() dependency
├── models.py            # SQLAlchemy ORM models
├── schemas.py            # Pydantic CourseCreate/CourseUpdate/CourseResponse/DepartmentResponse
├── postman/
├── screenshots/
├── requirements.txt
└── .gitignore
```

## Features
- Automatic request validation via Pydantic (`422` on bad input)
- Auto-generated OpenAPI / Swagger docs at `/docs`
- Async endpoints (`async def`) with async SQLAlchemy
- Dependency-injected DB sessions (`Depends(get_db)`)
- Pagination (`skip`, `limit`) and filtering (`department_id`) query params
- Nested Pydantic models (`DepartmentResponse` containing `CourseResponse` list)

## API Endpoints
| Method | Endpoint                                  | Description                        |
|--------|---------------------------------------------|--------------------------------------|
| GET    | `/`                                          | Health check                         |
| GET    | `/api/courses/?skip=&limit=&department_id=` | Paginated, filterable course list    |
| GET    | `/api/courses/{course_id}`                  | Get a course by ID                    |
| POST   | `/api/courses/`                              | Create a course (validated by Pydantic)|

## Screenshots
See `screenshots/` folder (Swagger UI screenshot recommended).

## Learning Outcomes
- Built request/response validation with Pydantic
- Used FastAPI's automatic OpenAPI documentation
- Implemented async endpoints backed by an async SQLAlchemy engine
- Applied FastAPI's dependency injection system for DB sessions
- Implemented pagination and filtering via query parameters
