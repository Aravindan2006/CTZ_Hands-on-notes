-- =====================================================================
-- Hands-On 3 : Task 2
-- Creating and Using Views
-- =====================================================================

-- ---------------------------------------------------------------------
-- 39. vw_student_enrollment_summary
--     full name, department, courses enrolled, GPA (A=4, B=3, C=2, D=1, F=0)
-- ---------------------------------------------------------------------
CREATE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    s.first_name || ' ' || s.last_name AS full_name,   -- MySQL: CONCAT(...)
    d.dept_name,
    COUNT(e.enrollment_id) AS courses_enrolled,
    ROUND(AVG(
        CASE e.grade
            WHEN 'A' THEN 4
            WHEN 'B' THEN 3
            WHEN 'C' THEN 2
            WHEN 'D' THEN 1
            WHEN 'F' THEN 0
        END
    ), 2) AS gpa
FROM students s
JOIN departments d ON s.department_id = d.department_id
LEFT JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name, d.dept_name;

-- ---------------------------------------------------------------------
-- 40. vw_course_stats
--     course_name, course_code, total_enrollments, avg_gpa
-- ---------------------------------------------------------------------
CREATE VIEW vw_course_stats AS
SELECT
    c.course_name,
    c.course_code,
    COUNT(e.enrollment_id) AS total_enrollments,
    ROUND(AVG(
        CASE e.grade
            WHEN 'A' THEN 4
            WHEN 'B' THEN 3
            WHEN 'C' THEN 2
            WHEN 'D' THEN 1
            WHEN 'F' THEN 0
        END
    ), 2) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name, c.course_code;
-- Expected: SELECT * FROM vw_course_stats returns 5 rows (one per course).

-- ---------------------------------------------------------------------
-- 41. Students with GPA above 3.0
-- ---------------------------------------------------------------------
SELECT full_name, dept_name, gpa
FROM vw_student_enrollment_summary
WHERE gpa > 3.0
ORDER BY gpa DESC;

-- ---------------------------------------------------------------------
-- 42. Attempt to UPDATE through vw_student_enrollment_summary
-- ---------------------------------------------------------------------
-- UPDATE vw_student_enrollment_summary SET gpa = 4.0 WHERE student_id = 1;
--
-- This FAILS (PostgreSQL: "cannot update view ... view is not
-- automatically updatable" / MySQL: "is not updatable"). Multi-table
-- views built from a JOIN plus GROUP BY / aggregate functions are not
-- updatable because the database engine cannot unambiguously map a
-- change in the view's derived, aggregated output (gpa, courses_enrolled)
-- back to a single row in a single base table -- an aggregate value like
-- AVG(grade) doesn't correspond to any one physical column that could be
-- written to.

-- ---------------------------------------------------------------------
-- 43. Drop both views, recreate a single-table, updatable view
--     WITH CHECK OPTION
-- ---------------------------------------------------------------------
DROP VIEW IF EXISTS vw_student_enrollment_summary;
DROP VIEW IF EXISTS vw_course_stats;

-- Single-table subset view: only students who enrolled from 2022 onward
CREATE VIEW vw_student_enrollment_summary AS
SELECT
    student_id,
    first_name,
    last_name,
    email,
    department_id,
    enrollment_year
FROM students
WHERE enrollment_year >= 2022
WITH CHECK OPTION;
-- WITH CHECK OPTION guarantees any INSERT/UPDATE performed through this
-- view must still satisfy enrollment_year >= 2022, otherwise it is
-- rejected -- e.g. trying to UPDATE a row's enrollment_year to 2020
-- through this view would be blocked.
