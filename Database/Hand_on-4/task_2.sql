-- =====================================================================
-- Hands-On 4 : Task 2
-- Add Indexes and Compare Plans
-- =====================================================================

-- ---------------------------------------------------------------------
-- 51. B-Tree index on students.enrollment_year
-- ---------------------------------------------------------------------
CREATE INDEX idx_students_enrollment_year
    ON students (enrollment_year);

-- ---------------------------------------------------------------------
-- 52. Composite UNIQUE index -- also prevents duplicate enrollments
-- ---------------------------------------------------------------------
CREATE UNIQUE INDEX ux_enrollments_student_course
    ON enrollments (student_id, course_id);
-- Column order: student_id first, course_id second, since most lookups
-- filter "all courses for a given student" (equality on student_id)
-- before narrowing to a specific course.

-- ---------------------------------------------------------------------
-- 53. Index on courses.course_code
-- ---------------------------------------------------------------------
CREATE INDEX idx_courses_course_code
    ON courses (course_code);

-- ---------------------------------------------------------------------
-- 54. Re-run EXPLAIN from Task 1 and compare
-- ---------------------------------------------------------------------
EXPLAIN ANALYZE
SELECT s.first_name, s.last_name, c.course_name
FROM enrollments e
JOIN students s ON s.student_id = e.student_id
JOIN courses  c ON c.course_id  = e.course_id
WHERE s.enrollment_year = 2022;

-- Observation (documented change):
-- After creating idx_students_enrollment_year, the planner's scan on
-- students switches from "Seq Scan on students ... Filter:
-- (enrollment_year = 2022)" to "Index Scan using
-- idx_students_enrollment_year on students ... Index Cond:
-- (enrollment_year = 2022)". On this small sample table the planner may
-- still pick Seq Scan (it estimates that's cheaper when almost every row
-- qualifies), but as row counts grow the optimizer switches to the
-- Index Scan automatically -- this is the expected/documented behaviour
-- to note in your own run against a larger dataset.

-- ---------------------------------------------------------------------
-- 55. Partial index -- optimise lookups for un-evaluated enrollments
-- ---------------------------------------------------------------------
CREATE INDEX idx_enrollments_no_grade
    ON enrollments (student_id)
    WHERE grade IS NULL;
-- NOTE: partial indexes are a PostgreSQL feature. MySQL 8.x has no
-- direct equivalent; the closest approximation is a regular composite
-- index on (grade, student_id), since MySQL cannot filter the index
-- itself by a WHERE predicate at creation time:
--   CREATE INDEX idx_enrollments_grade_student ON enrollments (grade, student_id);

-- Verify the composite UNIQUE index blocks duplicate enrollment inserts:
-- INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
-- VALUES (1, 1, '2024-01-01', NULL);
-- Expected: ERROR - duplicate key value violates unique constraint
-- "ux_enrollments_student_course" (student 1 is already enrolled in
-- course 1 from the sample data).
