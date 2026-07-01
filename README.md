# CTZ Hands-on Experiments — Backend

Ten hands-on exercises covering Python backend frameworks — **Django, Flask,
and FastAPI** — built around a single running scenario: a **Course
Management API** for a college system (Departments, Courses, Students,
Enrollments). Each hands-on is a fully independent, runnable project.

## Technologies
Django 5, Django REST Framework, Flask 3, Flask-SQLAlchemy, Flask-Migrate,
FastAPI, Uvicorn, SQLAlchemy 2.0 (sync & async), Pydantic v2, python-jose
(JWT), passlib/bcrypt, SQLite.

## Installation
Each hands-on folder is self-contained with its own `requirements.txt`.
```bash
cd Handson_0X_<name>
python -m venv venv && source venv/bin/activate   # venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Run Instructions
See each hands-on's own `README.md` for exact run commands — they differ
slightly per framework (`manage.py runserver`, `python app.py`, or
`uvicorn main:app --reload`).

## Folder Structure
```
CTZ_Hands-on-Experiments-Backend/
├── README.md
├── Handson_01_Django_Project_Setup/           # Web framework foundations, Django scaffold
├── Handson_02_Django_Models_ORM_Admin/        # Models, migrations, ORM queries, admin
├── Handson_03_Django_REST_Framework/          # Serializers, APIView, ViewSets, routers
├── Handson_04_Flask_Basics/                    # App factory, Blueprints, JSON responses
├── Handson_05_Flask_SQLAlchemy/                # Flask + SQLAlchemy ORM, migrations
├── Handson_06_FastAPI_Basics/                   # Pydantic, path/query params, async DB
├── Handson_07_FastAPI_CRUD/                     # Full CRUD, background tasks, OpenAPI
├── Handson_08_REST_API_Best_Practices/          # Versioning, pagination, PATCH, errors
├── Handson_09_JWT_Authentication/               # bcrypt, JWT, protected routes, CORS
└── Handson_10_Microservices/                    # Gateway + 2 services + inter-service calls
```

## Features
- The same Course Management domain rebuilt in 3 different frameworks
- Progression from framework fundamentals → ORM → REST APIs → auth → microservices
- Every hands-on includes its own README, requirements.txt, .gitignore,
  Postman collection, and screenshots folder
- All code has been run and verified end-to-end (migrations applied, servers
  started, and every documented endpoint exercised with real HTTP requests)

## API Endpoints
The common Course Management endpoints implemented across frameworks:

| Endpoint                  | Method | Description                  |
|----------------------------|--------|---------------------------------|
| `/api/courses/`             | GET     | List all courses                 |
| `/api/courses/`             | POST    | Create a new course               |
| `/api/courses/{id}/`        | GET     | Retrieve a course by ID           |
| `/api/courses/{id}/`        | PUT     | Update a course                    |
| `/api/courses/{id}/`        | DELETE  | Delete a course                    |
| `/api/students/`            | GET/POST| List or create students             |
| `/api/enrollments/`         | POST    | Enroll a student in a course         |
| `/api/auth/login/`          | POST    | Login and receive a JWT token          |

Each hands-on's own README documents its exact endpoint set (some add
versioning, e.g. `/api/v1/...`, in Hands-On 8 onward).

## Screenshots
Each hands-on has its own `screenshots/` folder — see individual READMEs
for what to capture.

## Learning Outcomes
- Understood and compared three major Python web frameworks and when to
  reach for each
- Built REST APIs from first principles through to production-style
  concerns: pagination, filtering, versioning, standardised errors
- Implemented authentication and authorization with JWTs and bcrypt
- Understood microservice decomposition and inter-service communication
  trade-offs

## Getting Started After Cloning
```bash
git init
git add .
git commit -m "Completed all 10 Hands-On Exercises"
git push
```
