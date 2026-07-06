# Hands-On 1 — Web Framework Foundations & Django Project Setup

## Project Description
Introduces core web framework concepts (request-response cycle, MVC/MVT,
WSGI vs ASGI, middleware) and scaffolds the base Django project
(`coursemanager`) with a `courses` app, used as the foundation for
Hands-On 2 and 3. Implements a minimal `/api/hello/` endpoint to prove the
project runs end-to-end.

## Technologies
- Python 3.10+
- Django 5.0

## Installation
```bash
cd Handson_01_Django_Project_Setup
python -m venv venv
source venv/bin/activate      # venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Run Instructions
```bash
python manage.py migrate
python manage.py runserver
```
Visit: http://127.0.0.1:8000/api/hello/

## Folder Structure
```
Handson_01_Django_Project_Setup/
├── manage.py
├── notes.py                  # Task 1 write-up (request cycle, middleware, WSGI/ASGI, MVT)
├── coursemanager/             # Django project (settings, urls, wsgi, asgi)
├── courses/                   # Django app (views, urls)
├── postman/                   # Postman collection
├── screenshots/
├── requirements.txt
└── .gitignore
```

## Features
- Django project + app scaffolding
- Function-based view returning a plain-text response
- Modular URL routing via `include()`
- Fully annotated `notes.py` covering framework fundamentals

## API Endpoints
| Method | Endpoint       | Description                          |
|--------|----------------|---------------------------------------|
| GET    | `/api/hello/`  | Returns "Course Management API is running" |
| GET    | `/admin/`      | Django admin login                    |

## Screenshots
See `screenshots/` folder.

## Learning Outcomes
- Understood the full Django request-response lifecycle
- Learned the difference between a Django project and a Django app
- Learned WSGI vs ASGI and when to use each
- Mapped MVC concepts onto Django's MVT pattern
- Built and ran a working Django server with a custom endpoint
