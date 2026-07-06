# Hands-On 5 — Flask with SQLAlchemy ORM & Database Integration

## Project Description
Connects the Flask API from Hands-On 4 to a real SQLite database using
Flask-SQLAlchemy and Flask-Migrate. Defines the same Department/Course/
Student/Enrollment schema as the Django hands-ons, with relationships, a
`to_dict()` serialization pattern, and a JOIN-based endpoint.

## Technologies
- Python 3.10+, Flask 3.0, Flask-SQLAlchemy, Flask-Migrate, SQLite

## Installation
```bash
cd Handson_05_Flask_SQLAlchemy
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Run Instructions
```bash
python seed.py          # creates tables + sample data
python app.py
```
API base: `http://127.0.0.1:5000/api/courses/`

To use real migrations instead of `db.create_all()`:
```bash
flask db init
flask db migrate -m "initial schema"
flask db upgrade
```

## Folder Structure
```
Handson_05_Flask_SQLAlchemy/
├── app.py                 # App factory, db.init_app(), Migrate(app, db)
├── config.py
├── extensions.py           # shared `db = SQLAlchemy()` instance
├── seed.py                 # creates tables + sample data
├── courses/
│   ├── models.py            # Department, Course, Student, Enrollment (SQLAlchemy)
│   └── routes.py            # DB-backed CRUD + /students/ JOIN endpoint
├── postman/
├── screenshots/
├── requirements.txt
└── .gitignore
```

## Features
- Real relational models with `db.relationship` and FK constraints
- `to_dict()` serialization (Flask's equivalent of DRF serializers)
- `db.get_or_404()` for automatic 404 responses
- JOIN query for `/api/courses/{id}/students/`
- `unique_together`-style constraint via `UniqueConstraint` on Enrollment

## API Endpoints
| Method | Endpoint                          | Description                     |
|--------|-------------------------------------|-----------------------------------|
| GET    | `/api/courses/`                     | List all courses (from DB)        |
| POST   | `/api/courses/`                      | Create a course                    |
| GET    | `/api/courses/{id}/`                | Get a course                       |
| PUT    | `/api/courses/{id}/`                | Update a course                    |
| DELETE | `/api/courses/{id}/`                | Delete a course                    |
| GET    | `/api/courses/{id}/students/`       | Enrolled students (JOIN query)     |

## Screenshots
See `screenshots/` folder.

## Learning Outcomes
- Integrated Flask-SQLAlchemy with the application factory pattern
- Defined ORM relationships and ran migrations with Flask-Migrate
- Replaced in-memory data with real, persisted database queries
- Wrote a JOIN query for a related-resource endpoint
