# ORM Layer Explanation -- SQLAlchemy (Hands-On 6)

## Architecture
```
Hand_on-6/
  config.py     -- reads .env, builds the SQLAlchemy connection URL
  database.py   -- engine (with pooling), session factory, init_db()
  models.py     -- ORM model classes + relationships
  crud.py       -- CRUD functions + N+1 demo + joinedload fix
```

This mirrors a typical Flask/FastAPI backend layering: configuration
is separated from connection management, which is separated from the
domain models, which is separated from the business-logic / data-access
functions that use them.

## Models and relationships
Five core models (`Department`, `Student`, `Course`, `Enrollment`,
`Professor`) map 1:1 onto the relational schema from Hands-On 1, plus
`CourseSchedule`, added later via the Hands-On 7 migration.
`relationship()` is declared bidirectionally with `back_populates` so
that, e.g., `department.students` and `student.department` both work
as native Python object navigation, without hand-written JOINs.

## Connection pooling
`database.py` configures SQLAlchemy's `QueuePool` explicitly:
`pool_size=5`, `max_overflow=10`, `pool_timeout=30`,
`pool_recycle=1800`, and `pool_pre_ping=True`. In a web application
serving concurrent requests, a shared, bounded pool of live database
connections avoids the overhead of opening a fresh TCP connection (and
re-authenticating) for every request, while `pool_pre_ping` guards
against stale connections that a firewall or DB restart may have
silently dropped.

## Session management
`get_session()` is a context manager: it commits on success, rolls
back on any exception, and always closes the session -- guaranteeing
connections are returned to the pool even when a request handler
raises.

## The N+1 problem and its fix
`list_enrollments_naive()` iterates over `Enrollment` rows and accesses
`.student` / `.course` on each -- with SQLAlchemy's default *lazy*
loading strategy, each access issues its own `SELECT`. With `echo=True`
on the engine, this is directly visible as a burst of individual
queries in the log.

`list_enrollments_optimized()` uses
`.options(joinedload(Enrollment.student), joinedload(Enrollment.course))`,
which tells SQLAlchemy to fetch the related `Student` and `Course` rows
via `LEFT OUTER JOIN` in the *same* query as the `Enrollment` rows --
collapsing what would be 1 + N queries into exactly 1.

An alternative eager-loading strategy, `subqueryload`, issues one
additional query per relationship using an `IN (...)` subquery instead
of a JOIN -- still O(1) relative to N, useful when the JOIN result set
would otherwise be very wide (many relationships loaded on the same
row).
