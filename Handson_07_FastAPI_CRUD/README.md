# Hands-On 7 — FastAPI Dependency Injection, CRUD & OpenAPI Documentation

## Project Description
Completes full CRUD for Courses, Students, and Enrollments with correct
REST status codes (`201`, `204`, `404`), `response_model` filtering,
`HTTPException` error handling, a `BackgroundTasks`-powered enrollment
confirmation "email", and a customised, tag-grouped OpenAPI/Swagger UI.

## Technologies
- Python 3.10+, FastAPI, Uvicorn, SQLAlchemy 2.0 (async), aiosqlite, Pydantic v2

## Installation
```bash
cd Handson_07_FastAPI_CRUD
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Run Instructions
```bash
uvicorn main:app --reload
```
Swagger UI (grouped by tags: Courses / Students / Enrollments):
`http://127.0.0.1:8000/docs`

## Folder Structure
```
Handson_07_FastAPI_CRUD/
├── main.py           # Full CRUD, background tasks, OpenAPI customisation
├── database.py
├── models.py           # Department, Course, Student, Enrollment
├── schemas.py           # Pydantic schemas for all 3 resources
├── postman/
├── screenshots/
├── requirements.txt
└── .gitignore
```

## Features
- Full CRUD for Courses / Students / Enrollments
- `response_model` filters ORM output to the documented schema shape
- `HTTPException(404, ...)` -> automatic JSON error response
- `BackgroundTasks` — enrollment returns `201` immediately; a confirmation
  "email" is printed to the server console *after* the response is sent
- OpenAPI metadata (title, description, version, contact) + tag grouping

## API Endpoints
| Method | Endpoint                          | Description                              |
|--------|-------------------------------------|--------------------------------------------|
| GET    | `/api/courses/`                    | List courses                                |
| POST   | `/api/courses/`                     | Create course (201)                          |
| GET    | `/api/courses/{id}`                | Get course (404 if missing)                  |
| PUT    | `/api/courses/{id}`                | Update course                                |
| DELETE | `/api/courses/{id}`                | Delete course (204 No Content)               |
| GET    | `/api/courses/{id}/students/`      | Students enrolled in a course (JOIN)         |
| GET/POST | `/api/students/`                 | List / create students                       |
| GET    | `/api/students/{id}`               | Get / delete a student                        |
| POST   | `/api/enrollments/`                 | Create enrollment + background email task     |
| GET    | `/api/enrollments/`                | List enrollments                             |

## Screenshots
See `screenshots/` folder.

## Learning Outcomes
- Implemented complete, REST-correct CRUD with proper status codes
- Used `response_model` to control API output shape
- Handled errors consistently with `HTTPException`
- Used `BackgroundTasks` for non-blocking post-response work
- Customised OpenAPI docs with tags, summaries, and metadata
