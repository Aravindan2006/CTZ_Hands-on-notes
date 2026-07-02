# Normalisation Analysis -- college_db

This mirrors and expands the inline comments in
`Hand_on-1/task2.sql`.

## 1NF -- Atomic Values
Every column across all five tables holds a single atomic value.
No column stores a comma-separated list, a repeating group, or a
nested structure. A hypothetical violation (storing multiple phone
numbers in one `phone_numbers` field) is avoided by design; if
multi-valued attributes were needed, they belong in a separate
child table.

## 2NF -- Full Functional Dependency on the Whole Key
2NF is only a concern for tables with a composite key. `enrollments`
has a natural composite candidate key of `(student_id, course_id)`.
Both non-key columns -- `enrollment_date` and `grade` -- depend on the
full pair, not on `student_id` or `course_id` alone, so the table
satisfies 2NF. Using a surrogate `enrollment_id` primary key does not
change this analysis; the composite uniqueness is still enforced
separately via a UNIQUE index.

## 3NF -- No Transitive Dependencies
No table stores a column that depends on another non-key column
rather than directly on the primary key. Specifically:
- `students.department_id` is a foreign key; `dept_name` is **not**
  duplicated into `students` (avoiding `student_id -> department_id
  -> dept_name`).
- The same reasoning applies to `courses` and `professors`.

## Why this matters
Normalising through 3NF eliminates update, insert, and delete
anomalies: renaming a department requires exactly one `UPDATE`
statement (on `departments`), not a bulk update across every table
that might have cached the name.

## Trade-off note
Fully normalised schemas trade write-simplicity for read-complexity --
most queries need JOINs to reassemble a "flat" view (see the views
created in Hands-On 3, e.g. `vw_student_enrollment_summary`). This is
an accepted, standard trade-off for an OLTP system like a student
registration platform, where data integrity matters more than raw
read throughput.
