-- =====================================================================
-- Hands-On 2 : Task 4
-- Aggregations and Grouping
-- =====================================================================

-- ---------------------------------------------------------------------
-- 30. Total enrollments per course
-- ---------------------------------------------------------------------
SELECT
    c.course_name,
    COUNT(e.enrollment_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name
ORDER BY enrollment_count DESC;

-- ---------------------------------------------------------------------
-- 31. Average professor salary per department, rounded to 2 decimals
-- ---------------------------------------------------------------------
SELECT
    d.dept_name,
    ROUND(AVG(p.salary), 2) AS avg_salary
FROM departments d
JOIN professors p ON d.department_id = p.department_id
GROUP BY d.dept_name
ORDER BY avg_salary DESC;
-- Expected: 4 rows -- one per department.

-- ---------------------------------------------------------------------
-- 32. Departments where total budget exceeds 600,000
-- ---------------------------------------------------------------------
SELECT dept_name, budget
FROM departments
WHERE budget > 600000
ORDER BY budget DESC;

-- ---------------------------------------------------------------------
-- 33. Grade distribution for course CS101
-- ---------------------------------------------------------------------
SELECT
    e.grade,
    COUNT(*) AS grade_count
FROM enrollments e
JOIN courses c ON e.course_id = c.course_id
WHERE c.course_code = 'CS101'
GROUP BY e.grade
ORDER BY e.grade;

-- ---------------------------------------------------------------------
-- 34. Departments with more than 2 students enrolled (across all courses)
-- ---------------------------------------------------------------------
SELECT
    d.dept_name,
    COUNT(DISTINCT e.student_id) AS enrolled_students
FROM departments d
JOIN courses c ON c.department_id = d.department_id
JOIN enrollments e ON e.course_id = c.course_id
GROUP BY d.dept_name
HAVING COUNT(DISTINCT e.student_id) > 2
ORDER BY enrolled_students DESC;
