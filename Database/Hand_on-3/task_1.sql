-- =====================================================================
-- Hands-On 3 : Task 1
-- Subqueries
-- =====================================================================

-- ---------------------------------------------------------------------
-- 35. Students enrolled in more courses than the average number of
--     enrollments per student (non-correlated subquery for the average)
-- ---------------------------------------------------------------------
SELECT
    s.student_id,
    s.first_name,
    s.last_name,
    COUNT(e.enrollment_id) AS course_count
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.enrollment_id) > (
    -- average enrollments per student, computed independently
    SELECT AVG(cnt) FROM (
        SELECT COUNT(*) AS cnt
        FROM enrollments
        GROUP BY student_id
    ) AS per_student_counts
)
ORDER BY course_count DESC;

-- ---------------------------------------------------------------------
-- 36. Courses where ALL enrolled students received a grade of 'A'
--     (NOT EXISTS pattern: no student in this course has a grade <> 'A')
-- ---------------------------------------------------------------------
SELECT c.course_id, c.course_name
FROM courses c
WHERE EXISTS (
        SELECT 1 FROM enrollments e WHERE e.course_id = c.course_id
      )
  AND NOT EXISTS (
        SELECT 1
        FROM enrollments e
        WHERE e.course_id = c.course_id
          AND (e.grade IS DISTINCT FROM 'A')   -- MySQL: e.grade <> 'A' OR e.grade IS NULL
      );

-- ---------------------------------------------------------------------
-- 37. Highest-paid professor in each department (correlated subquery)
-- ---------------------------------------------------------------------
SELECT p.professor_id, p.prof_name, p.department_id, p.salary
FROM professors p
WHERE p.salary = (
    SELECT MAX(p2.salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
);

-- ---------------------------------------------------------------------
-- 38. Derived table (subquery in FROM): per-department average salary,
--     filtered to departments where that average exceeds 85,000
-- ---------------------------------------------------------------------
SELECT dept_avg.department_id, dept_avg.avg_salary
FROM (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM professors
    GROUP BY department_id
) AS dept_avg
WHERE dept_avg.avg_salary > 85000;
