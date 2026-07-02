# Hands-On 7 -- Migrations & Versioning (Alembic)

## Setup
```bash
pip install alembic sqlalchemy psycopg2-binary
```

This folder already contains an initialised Alembic project
(`alembic.ini`, `env.py`, `script.py.mako`, `versions/`) equivalent to
what `alembic init migrations` scaffolds -- it has been pre-populated so
the full migration history is visible without running commands.

Update `sqlalchemy.url` in `alembic.ini` (or export `DB_*` env vars and
adapt `env.py`) to point at your `college_db_orm` database before
running any command below.

## Migration history in this project
| Revision | Description                    | Depends on |
|----------|--------------------------------|------------|
| `0001`   | initial schema (5 base tables) | -          |
| `0002`   | add `is_active` to `students`  | `0001`     |
| `0003`   | add `course_schedules` table   | `0002`     |

## Task 1 -- Baseline migration
```bash
alembic init migrations                       # (already done in this folder)
alembic revision --autogenerate -m "initial schema"
alembic upgrade head                           # applies 0001
alembic current                                # shows revision hash + alembic_version table
```

## Task 2 -- Incremental migrations
```bash
alembic revision --autogenerate -m "add is_active to students"
alembic upgrade head                           # applies 0002

alembic revision --autogenerate -m "add course_schedules table"
alembic upgrade head                           # applies 0003

alembic history --verbose                      # shows all 3 revisions in order
```

## Task 3 -- Rollback and recovery
```bash
alembic current                                # note the current head, e.g. 0003
alembic downgrade -1                           # step back one revision (0003 -> 0002); is_active stays, course_schedules drops... 
                                                # wait -- downgrade -1 from head 0003 drops course_schedules (0003's change)
alembic downgrade -1                           # (0002 -> 0001) drops is_active column
alembic downgrade base                         # undo everything, back to an empty schema
alembic upgrade head                           # re-apply all three, back to the latest state
alembic current                                # confirms it matches head (0003)
```

### Command reference
| Command                                    | Effect                                      |
|---------------------------------------------|----------------------------------------------|
| `alembic revision --autogenerate -m "msg"`   | Diff models vs DB, generate a new migration   |
| `alembic upgrade head`                       | Apply all migrations up to the latest         |
| `alembic upgrade +1`                         | Apply just the next migration                 |
| `alembic downgrade -1`                       | Revert the most recently applied migration    |
| `alembic downgrade base`                     | Revert all migrations (empty schema)          |
| `alembic current`                            | Show the currently applied revision           |
| `alembic history --verbose`                  | Show the full migration chain                 |

### Bonus -- Django migrations equivalent
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py migrate <app_name> <previous_migration_number>   # rollback
```

**Always back up production databases before running any `downgrade` command.**
