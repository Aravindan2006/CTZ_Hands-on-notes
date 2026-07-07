# Hands-On 2 — Django Models, ORM & Admin Interface

## Project Description
Builds on Hands-On 1 by defining the Course Management data model
(Department, Course, Student, Enrollment), running migrations, seeding
sample data, demonstrating Django ORM query patterns (`filter`, `annotate`,
`select_related`, `F()` expressions), and registering all models in a
customised Django admin interface.

## Technologies
- Python 3.10+, Django 5.0, SQLite

## Installation
```bash
cd Handson_02_Django_Models_ORM_Admin
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Run Instructions
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py seed_data          # creates sample departments/courses/students + runs ORM demo queries
python manage.py createsuperuser    # e.g. admin / admin@college.edu / Admin@123
python manage.py runserver
```
Visit `http://127.0.0.1:8000/admin/` and log in.

## Folder Structure
```
Handson_02_Django_Models_ORM_Admin/
├── manage.py
├── notes.py
├── coursemanager/
├── courses/
│   ├── models.py                    # Department, Course, Student, Enrollment
│   ├── admin.py                     # Admin registration + CourseAdmin customisation
│   ├── migrations/
│   └── management/commands/seed_data.py
├── postman/
├── screenshots/
├── requirements.txt
└── .gitignore
```

## Features
- 4 related models with proper ForeignKeys and a `unique_together` constraint
- Custom management command seeding realistic sample data
- ORM query demonstrations: `filter(department__name=...)`, `annotate(Count(...))`,
  `select_related`, bulk `update(... F(...))`
- Admin customisation: `list_display`, `search_fields`, `list_filter`

## API Endpoints
Same as Hands-On 1 (`/api/hello/`); the primary interface for this hands-on
is the Django admin at `/admin/`.

## Screenshots
See `screenshots/` folder.

## Learning Outcomes
- Modeled a relational domain with Django ORM and ForeignKeys
- Ran and inspected migrations
- Used advanced ORM features: annotations, joins via `select_related`, and
  database-side updates with `F()`
- Customised the Django admin for a better data-management UX
- Enforced data integrity with `unique_together`
