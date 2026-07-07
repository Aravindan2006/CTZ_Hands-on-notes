# Hands-On 4 — Flask App Structure, Routing & Blueprints

## Project Description
Rebuilds the Course Management API in Flask, using the application factory
pattern, a modular Blueprint for course routes, request validation, a
consistent JSON response envelope, and JSON-based error handlers (instead
of Flask's default HTML error pages).

## Technologies
- Python 3.10+, Flask 3.0

## Installation
```bash
cd Handson_04_Flask_Basics
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Run Instructions
```bash
python app.py
```
API base: `http://127.0.0.1:5000/api/courses/`

## Folder Structure
```
Handson_04_Flask_Basics/
├── app.py                # Application factory (create_app) + error handlers
├── config.py              # Config class
├── courses/
│   ├── __init__.py
│   └── routes.py          # Blueprint: courses_bp with full CRUD
├── postman/
├── screenshots/
├── requirements.txt
└── .gitignore
```

## Features
- Application factory pattern (`create_app()`)
- Blueprint-based modular routing (`courses_bp`, prefix `/api/courses`)
- Request body validation with 400 responses for missing fields
- Consistent JSON envelope: `{"status": "success", "data": ...}`
- JSON 404 / 500 error handlers (no HTML error pages)

## API Endpoints
| Method | Endpoint                    | Description          |
|--------|-------------------------------|------------------------|
| GET    | `/api/courses/`               | List all courses       |
| POST   | `/api/courses/`                | Create a course         |
| GET    | `/api/courses/{id}/`          | Get a course by ID     |
| PUT    | `/api/courses/{id}/`          | Update a course        |
| DELETE | `/api/courses/{id}/`          | Delete a course        |

## Screenshots
See `screenshots/` folder.

## Learning Outcomes
- Understood Flask's minimal, unopinionated approach vs Django
- Applied the application factory pattern to avoid circular imports
- Organised routes using Blueprints
- Built consistent, all-JSON API responses including error handling
