# Hands-On 6 -- ORM Integration (SQLAlchemy)

## Files
- `models.py` -- SQLAlchemy ORM model classes (Department, Student, Course, Enrollment, Professor, CourseSchedule)
- `database.py` -- engine, connection pool configuration, and session factory (`get_session()`)
- `config.py` -- environment-driven DB configuration (reads `.env`)
- `crud.py` -- CRUD operations, the N+1 demonstration, and its `joinedload` fix

## Setup
```bash
pip install -r requirements.txt
cp ../.env.example .env      # edit with your DB credentials
python database.py           # creates all tables in college_db_orm
python crud.py                # seeds sample data and runs the CRUD/N+1 demo
```

## Enabling SQL query logging
Set `DB_ECHO=True` in `.env` to print every SQL statement SQLAlchemy issues --
this is how the N+1 problem in `list_enrollments_naive()` is diagnosed,
and how you confirm `list_enrollments_optimized()` collapses it to a
single query.
