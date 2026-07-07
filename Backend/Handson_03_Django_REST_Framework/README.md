# Hands-On 3 — Django REST Views, Serializers & ViewSets

## Project Description
Builds the actual REST API for the Course Management system using Django
REST Framework. Starts with `APIView`-based endpoints (Task 1), then
refactors to `ModelViewSet` + `DefaultRouter` (Task 2) for full CRUD on
Courses, Students, Enrollments, and Departments, including a custom
`/api/courses/{id}/students/` action.

## Technologies
- Python 3.10+, Django 5.0, Django REST Framework 3.15, SQLite

## Installation
```bash
cd Handson_03_Django_REST_Framework
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Run Instructions
```bash
python manage.py migrate
python manage.py seed_data
python manage.py runserver
```
API base: `http://127.0.0.1:8000/api/`

## Folder Structure
```
Handson_03_Django_REST_Framework/
├── manage.py
├── coursemanager/
├── courses/
│   ├── models.py
│   ├── serializers.py     # DepartmentSerializer, CourseSerializer, StudentSerializer, EnrollmentSerializer
│   ├── views.py            # APIView versions (Task 1) + ViewSets (Task 2, wired up)
│   ├── urls.py              # DefaultRouter registration
│   └── management/commands/seed_data.py
├── postman/
├── screenshots/
├── requirements.txt
└── .gitignore
```

## Features
- Full CRUD via `ModelViewSet` for 4 resources
- Auto-generated URL routing via `DefaultRouter`
- Custom `@action` endpoint: list students enrolled in a course
- Proper HTTP status codes (200, 201, 204, 400, 404)

## API Endpoints
| Method | Endpoint                          | Description                     |
|--------|------------------------------------|----------------------------------|
| GET    | `/api/courses/`                    | List all courses                 |
| POST   | `/api/courses/`                    | Create a course                  |
| GET    | `/api/courses/{id}/`               | Retrieve a course                |
| PUT    | `/api/courses/{id}/`               | Update a course                  |
| DELETE | `/api/courses/{id}/`               | Delete a course                  |
| GET    | `/api/courses/{id}/students/`      | Custom action — enrolled students|
| GET/POST | `/api/students/`                 | List / create students           |
| GET/POST | `/api/enrollments/`              | List / create enrollments        |
| GET/POST | `/api/departments/`              | List / create departments        |

## Screenshots
See `screenshots/` folder.

## Learning Outcomes
- Built REST endpoints two ways: `APIView` and `ModelViewSet`
- Understood how `DefaultRouter` auto-generates URL patterns
- Implemented and tested a custom ViewSet `@action`
- Verified all CRUD operations and status codes with live HTTP requests
