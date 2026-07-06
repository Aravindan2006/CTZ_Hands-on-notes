-- =====================================================================
-- Hands-On 2 : Task 3
-- Multi-Table Joins
-- =====================================================================

-- ---------------------------------------------------------------------
-- 25. Student full name alongside department name
-- ---------------------------------------------------------------------
SELECT
    s.first_name || ' ' || s.last_name AS full_name,   -- MySQL: CONCAT(s.first_name, ' ', s.last_name)
    d.dept_name
FROM students s
JOIN departments d ON s.department_id = d.department_id
ORDER BY full_name;

-- ---------------------------------------------------------------------
-- 26. Each enrollment with student name and course name (3-table JOIN)
-- ---------------------------------------------------------------------
SELECT
    e.enrollment_id,
    s.first_name || ' ' || s.last_name AS student_name, -- MySQL: CONCAT(...)
    c.course_name,
    e.enrollment_date,
    e.grade
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses  c ON e.course_id  = c.course_id
ORDER BY e.enrollment_id;

-- ---------------------------------------------------------------------
-- 27. Students NOT enrolled in any course (LEFT JOIN + IS NULL pattern)
-- ---------------------------------------------------------------------
SELECT s.student_id, s.first_name, s.last_name
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
WHERE e.enrollment_id IS NULL;

-- ---------------------------------------------------------------------
-- 28. Every course with its enrollment count (0 for courses with none)
-- ---------------------------------------------------------------------
SELECT
    c.course_id,
    c.course_name,
    COUNT(e.enrollment_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name
ORDER BY c.course_id;
-- Expected: all 5 courses appear, including any with 0 students.

-- ---------------------------------------------------------------------
-- 29. Departments with their professors and salaries (incl. depts with none)
-- ---------------------------------------------------------------------
SELECT
    d.dept_name,
    p.prof_name,
    p.salary
FROM departments d
LEFT JOIN professors p ON d.department_id = p.department_id
ORDER BY d.dept_name, p.prof_name;
