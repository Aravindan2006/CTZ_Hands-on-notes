-- =====================================================================
-- Hands-On 2 : Task 2
-- Single-Table Queries and Filtering
-- =====================================================================

-- ---------------------------------------------------------------------
-- 20. Students enrolled in 2022, ordered by last_name
-- ---------------------------------------------------------------------
SELECT student_id, first_name, last_name, enrollment_year
FROM students
WHERE enrollment_year = 2022
ORDER BY last_name ASC;

-- ---------------------------------------------------------------------
-- 21. Courses with more than 3 credits, sorted by credits descending
-- ---------------------------------------------------------------------
SELECT course_id, course_name, course_code, credits
FROM courses
WHERE credits > 3
ORDER BY credits DESC;

-- ---------------------------------------------------------------------
-- 22. Professors with salary between 80,000 and 95,000 (inclusive)
-- ---------------------------------------------------------------------
SELECT professor_id, prof_name, salary
FROM professors
WHERE salary BETWEEN 80000 AND 95000
ORDER BY salary DESC;

-- ---------------------------------------------------------------------
-- 23. Students whose email ends with '@college.edu'
-- ---------------------------------------------------------------------
SELECT student_id, first_name, last_name, email
FROM students
WHERE email LIKE '%@college.edu';

-- ---------------------------------------------------------------------
-- 24. Count of students per enrollment_year
-- ---------------------------------------------------------------------
SELECT enrollment_year, COUNT(*) AS student_count
FROM students
GROUP BY enrollment_year
ORDER BY enrollment_year;
-- Expected: 3 rows -- one per distinct enrollment_year (2021, 2022, 2023)
