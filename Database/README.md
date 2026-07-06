# Database Integration -- Student Course Registration System
Digital Nurture 5.0 | Module 3 | PostgreSQL, MySQL & MongoDB

## Project Overview
This repository implements all 7 Hands-On exercises from the Module 3
Database Integration exercise book, built around a single scenario: a
college's Student Course Registration System. It progresses from raw
DDL/DML through advanced SQL, query optimisation, MongoDB document
modelling, a SQLAlchemy ORM layer, and finally Alembic migrations.

## Folder Structure
```
Database/
  Hand_on-1/                  DDL, constraints, normalisation (1NF-3NF)
    task1.sql
    task2.sql
    task3.sql
  Hand_on-2/                  DML, SELECT, JOINs, aggregation
    task1.sql
    task2.sql
    task3.sql
    task4.sql
  Hand_on-3/                  Subqueries, views, procedures/functions, transactions
    task_1.sql
    task_2.sql
    task_3.sql
  Hand_on-4/                  Indexes, EXPLAIN, N+1 problem
    task_1.sql
    task_2.sql
    task_3_n_plus_one_demo.py
  Hand_on-5/                  MongoDB document modelling
    feedback_data.js
    crud_queries.js
    aggregation_queries.js
    indexes.js
  Hand_on-6/                  SQLAlchemy ORM
    models.py
    database.py
    config.py
    crud.py
    requirements.txt
    README.md
  Hand_on-7/                  Alembic migrations
    alembic.ini
    env.py
    script.py.mako
    versions/
    README.md
  docs/
    ER_Diagram.md
    Normalization.md
    Optimization_Report.md
    MongoDB_Design.md
    ORM_Explanation.md
    Migration_Guide.md
  screenshots/
  requirements.txt
  .gitignore
  .env.example
  LICENSE
  README.md                   (this file)
```

## Requirements
- PostgreSQL (latest) or MySQL Community Server 8.x
- MongoDB Community Server + MongoDB Compass (or `mongosh`)
- Python 3.10+
- Python packages (see `requirements.txt`):
  `sqlalchemy`, `psycopg2-binary`, `mysql-connector-python`, `pymongo`,
  `alembic`, `flask-sqlalchemy`, `python-dotenv`

## Installation
```bash
git clone <your-repo-url>
cd Database
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # then edit .env with your credentials
```

## Database Setup

### PostgreSQL
```bash
createdb college_db
psql -d college_db -f Hand_on-1/task1.sql
psql -d college_db -f Hand_on-1/task3.sql
psql -d college_db -f Hand_on-2/task1.sql
```

### MySQL
```bash
mysql -u root -p -e "CREATE DATABASE college_db;"
mysql -u root -p college_db < Hand_on-1/task1.sql
mysql -u root -p college_db < Hand_on-1/task3.sql
mysql -u root -p college_db < Hand_on-2/task1.sql
```
(Un-comment the MySQL-specific lines noted inline in each `.sql` file
where PostgreSQL and MySQL syntax diverge, e.g. `AUTO_INCREMENT` vs
`SERIAL`, `CHANGE COLUMN` vs `RENAME COLUMN`.)

### MongoDB
```bash
mongosh
> load('Hand_on-5/feedback_data.js')
> load('Hand_on-5/crud_queries.js')
> load('Hand_on-5/aggregation_queries.js')
> load('Hand_on-5/indexes.js')
```
Or open each `.js` file's contents in MongoDB Compass's embedded shell.

## Running the SQL Scripts
Run each `Hand_on-N` folder's files in numeric order -- e.g. for
Hands-On 3: `task_1.sql` -> `task_2.sql` -> `task_3.sql`. Hands-On 1
and 2 must be completed before 3 and 4; all of 1-4 must be completed
before attempting 5, 6, and 7 (per the exercise book's stated
sequence).

## Running the Python / ORM Scripts
```bash
cd Hand_on-4
python task_3_n_plus_one_demo.py

cd ../Hand_on-6
python database.py    # creates tables in college_db_orm
python crud.py         # seeds data, runs CRUD + N+1 + joinedload demo
```

## Running Alembic
```bash
cd Hand_on-7
alembic upgrade head              # apply all 3 migrations
alembic current                    # confirm head revision
alembic history --verbose          # view the full chain
alembic downgrade -1               # step back one revision
alembic downgrade base             # revert everything
alembic upgrade head               # re-apply everything
```
See `Hand_on-7/README.md` for the full command reference.

## Screenshots
Placeholders and suggested filenames are listed in `screenshots/README.md`.
Add your own screenshots there as you run each exercise.

## Expected Outputs (high level)
- **Hands-On 1**: 5 tables created with no errors; ALTERs apply cleanly.
- **Hands-On 2**: `students` has 10 rows; `enrollments` has only
  non-NULL-grade rows after the DELETE.
- **Hands-On 3**: `vw_course_stats` returns 5 rows; SAVEPOINT test
  keeps the first insert after a partial rollback.
- **Hands-On 4**: EXPLAIN shows Index Scan after indexing;
  `task_3_n_plus_one_demo.py` prints "13 queries executed" (naive) vs
  "1 query executed" (optimised).
- **Hands-On 5**: `db.feedback.countDocuments()` returns 11; aggregation
  pipelines return per-course averages and a tag leaderboard.
- **Hands-On 6**: `echo=True` SQL log shows the query count drop from
  N+1 down to 1 after switching to `joinedload`.
- **Hands-On 7**: `alembic history` shows 3 revisions;
  `is_active` and `course_schedules` appear/disappear correctly across
  upgrade/downgrade cycles.

## Troubleshooting
| Issue | Likely Cause | Fix |
|---|---|---|
| `psycopg2.OperationalError: could not connect` | PostgreSQL not running, or wrong host/port in `.env` | Confirm `pg_isready`, check `.env` |
| `ERROR 1045 (28000): Access denied` (MySQL) | Wrong credentials | Check `DB_USER`/`DB_PASSWORD` |
| `ModuleNotFoundError` for any package | Virtualenv not activated / deps not installed | `pip install -r requirements.txt` |
| Alembic `Target database is not up to date` | Migrations applied out of order | Run `alembic current`, then `alembic upgrade head` |
| MongoDB `IXSCAN` not shown in `explain()` | Index not created yet | Run `Hand_on-5/indexes.js` first |
| `CHECK` constraint silently ignored (MySQL) | MySQL version < 8.0.16 | Upgrade MySQL, or enforce the rule in application code as a fallback |

## License
MIT -- see `LICENSE`.
