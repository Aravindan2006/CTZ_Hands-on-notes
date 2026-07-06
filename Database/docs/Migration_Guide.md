# Migration Guide -- Alembic (Hands-On 7)

## What migrations solve
As `models.py` evolves (new columns, new tables), the live database
schema must evolve in lock-step, in a way that is: (1) version
controlled, (2) reproducible across every developer's machine and
every environment (dev/staging/prod), and (3) reversible. Alembic
provides exactly this for SQLAlchemy projects.

## Project layout
```
Hand_on-7/
  alembic.ini          -- points Alembic at the target DB + migration folder
  env.py                -- wires target_metadata to models.Base.metadata
  script.py.mako         -- template used to generate new revision files
  versions/
    20240101_0001_initial_schema.py
    20240115_0002_add_is_active_to_students.py
    20240201_0003_add_course_schedules.py
```

## Migration chain in this project
```
0001 (initial schema)
  |
0002 (add is_active to students)
  |
0003 (add course_schedules table)   <-- head
```

Each revision file has an `upgrade()` (apply this change) and a
`downgrade()` (undo this change) function, and references the revision
it builds on via `down_revision`. This linked-list structure is what
lets `alembic history` reconstruct the full chain and lets
`alembic downgrade`/`upgrade` walk it in either direction.

## Everyday commands
```bash
alembic revision --autogenerate -m "description"   # generate a new migration from model diffs
alembic upgrade head                                 # apply all pending migrations
alembic downgrade -1                                  # revert the most recent migration
alembic downgrade base                                # revert everything
alembic current                                       # show applied revision
alembic history --verbose                             # show the full chain
```

## Autogenerate caveats
`--autogenerate` compares `target_metadata` (from `models.py`) against
the live database and generates a best-effort diff. It reliably
detects new/dropped tables and new/dropped columns, but it can miss
column **renames** (seeing them as a drop + add instead) and does not
generate data-migration logic (e.g. backfilling a new NOT NULL column)
-- always read the generated file before applying it, and hand-edit
where necessary.

## Safety notes
- Always back up production databases before running `downgrade`.
- Test the full `upgrade head -> downgrade base -> upgrade head` cycle
  in a disposable environment before trusting it in production.
- Prefer additive changes (new nullable columns, new tables) where
  possible; they're safer to deploy and roll back than destructive
  ones (dropping/renaming columns in use by running application code).
