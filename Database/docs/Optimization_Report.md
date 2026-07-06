# Query Optimisation Report

Summarises the work done in `Hand_on-4/`.

## Baseline (no indexes)
The query joining `enrollments`, `students`, and `courses`, filtered on
`students.enrollment_year = 2022`, initially runs with a Sequential
Scan (PostgreSQL) / Full Table Scan (MySQL) on `students` to evaluate
the `enrollment_year` filter, since no index exists on that column.
On a small sample table this is cheap, but it does not scale: on a
table with hundreds of thousands of rows, a Seq Scan means reading
every single row just to find the matching subset.

## Indexes added
| Index | Table.Column(s) | Purpose |
|---|---|---|
| `idx_students_enrollment_year` | `students(enrollment_year)` | Speeds up filtering students by intake year |
| `ux_enrollments_student_course` | `enrollments(student_id, course_id)` | Composite UNIQUE index; speeds up per-student lookups AND enforces "no duplicate enrollment" |
| `idx_courses_course_code` | `courses(course_code)` | Speeds up course lookups by code (e.g. `CS101`) |
| `idx_enrollments_no_grade` | `enrollments(student_id) WHERE grade IS NULL` | Partial index -- optimises the specific "ungraded enrollments" lookup pattern without indexing graded rows |

## Result
After indexing, `EXPLAIN ANALYZE` on the baseline query shows the
planner switching the `students` scan from Seq Scan to Index Scan
using `idx_students_enrollment_year` as the qualifying row count drops
relative to the table size. The composite UNIQUE index additionally
guarantees data integrity by rejecting duplicate `(student_id,
course_id)` inserts at the database level, rather than relying on
application code to check first.

## Composite index column order
`ux_enrollments_student_course` is defined as `(student_id,
course_id)` rather than the reverse, because the dominant access
pattern is "look up all courses for a given student" (equality filter
on `student_id` first).

## N+1 problem (Task 3)
`n_plus_one_demo.py` measures the difference directly:
- **Naive loop**: 1 query to fetch enrollments + 1 query per row to
  fetch the student -- for 12 sample enrollments, 13 total queries.
- **Single JOIN**: exactly 1 query, identical result set.

Extrapolated to 10,000 enrollments, the naive approach issues 10,001
queries -- 10,000 avoidable round trips -- versus 1 for the JOIN
version. This exact pattern reappears at the ORM layer in Hands-On 6,
fixed there with `joinedload`.
