-- =====================================================================
-- Hands-On 1 : Task 3
-- Alter and Extend the Schema
-- =====================================================================

-- ---------------------------------------------------------------------
-- 10. Add phone_number to students
-- ---------------------------------------------------------------------
ALTER TABLE students
    ADD COLUMN phone_number VARCHAR(15);

-- ---------------------------------------------------------------------
-- 11. Add max_seats to courses, default 60
-- ---------------------------------------------------------------------
ALTER TABLE courses
    ADD COLUMN max_seats INT DEFAULT 60;

-- ---------------------------------------------------------------------
-- 12. CHECK constraint on enrollments.grade
-- ---------------------------------------------------------------------
-- PostgreSQL / MySQL 8+:
ALTER TABLE enrollments
    ADD CONSTRAINT chk_enrollments_grade
    CHECK (grade IN ('A', 'B', 'C', 'D', 'F') OR grade IS NULL);
-- NOTE: MySQL < 8.0.16 parses CHECK constraints but does not enforce
-- them. Always verify with an invalid INSERT after running this.

-- ---------------------------------------------------------------------
-- 13. Rename departments.hod_name -> head_of_dept
-- ---------------------------------------------------------------------
-- PostgreSQL:
ALTER TABLE departments
    RENAME COLUMN hod_name TO head_of_dept;

-- MySQL 8+ equivalent (uncomment if running on MySQL):
-- ALTER TABLE departments
--     CHANGE COLUMN hod_name head_of_dept VARCHAR(100);

-- ---------------------------------------------------------------------
-- 14. Drop phone_number (simulate a schema rollback)
-- ---------------------------------------------------------------------
ALTER TABLE students
    DROP COLUMN phone_number;

-- ---------------------------------------------------------------------
-- Verification
-- ---------------------------------------------------------------------
-- PostgreSQL:
--   SELECT column_name, data_type, column_default
--   FROM information_schema.columns
--   WHERE table_name = 'students';
--
-- MySQL:
--   SELECT COLUMN_NAME, DATA_TYPE, COLUMN_DEFAULT
--   FROM INFORMATION_SCHEMA.COLUMNS
--   WHERE TABLE_SCHEMA = 'college_db' AND TABLE_NAME = 'students';
--
-- Expected: phone_number is gone, courses.max_seats defaults to 60,
-- departments.head_of_dept replaces hod_name, and inserting a grade of
-- 'Z' into enrollments now raises a CHECK constraint violation.
