# ER Diagram -- college_db

```
 departments (1) ----< (M) students
 departments (1) ----< (M) courses
 departments (1) ----< (M) professors
 students    (1) ----< (M) enrollments
 courses     (1) ----< (M) enrollments
 courses     (1) ----< (M) course_schedules      (added in Hands-On 7)
```

## Entities

**departments**
`department_id (PK)`, `dept_name`, `head_of_dept`, `budget`

**students**
`student_id (PK)`, `first_name`, `last_name`, `email (UNIQUE)`,
`date_of_birth`, `department_id (FK -> departments)`, `enrollment_year`,
`is_active` (added in Hands-On 7)

**courses**
`course_id (PK)`, `course_name`, `course_code (UNIQUE)`, `credits`,
`department_id (FK -> departments)`, `max_seats`

**enrollments**
`enrollment_id (PK)`, `student_id (FK -> students)`,
`course_id (FK -> courses)`, `enrollment_date`, `grade`
Composite candidate key: `(student_id, course_id)` -- enforced via a
UNIQUE index in Hands-On 4.

**professors**
`professor_id (PK)`, `prof_name`, `email (UNIQUE)`,
`department_id (FK -> departments)`, `salary`

**course_schedules** (added in Hands-On 7)
`schedule_id (PK)`, `course_id (FK -> courses)`, `day_of_week`,
`start_time`, `end_time`

## Relationship summary

- One department has many students, many courses, and many professors.
- A student can enroll in many courses, and a course can have many
  students -- this many-to-many relationship is resolved through the
  `enrollments` junction table.
- A course can have many scheduled class sessions (`course_schedules`).

## Text-based diagram

```
        +----------------+
        |  departments   |
        +----------------+
         | 1        | 1        | 1
         | *         | *        | *
+----------------+ +----------------+ +----------------+
|    students    | |    courses     | |   professors   |
+----------------+ +----------------+ +----------------+
     | 1                | 1
     | *                | *
     +------------------+
              |
     +----------------+
     |  enrollments   |
     +----------------+

              +----------------+
courses  1 -- * course_schedules
              +----------------+
```
