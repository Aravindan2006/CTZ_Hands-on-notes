-- =====================================================================
-- Hands-On 1 : Task 1
-- Create the Database and Tables
-- Student Course Registration System - college_db
-- Works on PostgreSQL and MySQL 8.x (notes given where syntax differs)
-- =====================================================================

-- ---------------------------------------------------------------------
-- 1. Create the database
-- ---------------------------------------------------------------------
-- PostgreSQL: run this from psql / a superuser connection, then \c college_db
CREATE DATABASE college_db;

-- MySQL equivalent (uncomment if running on MySQL):
-- CREATE DATABASE IF NOT EXISTS college_db;
-- USE college_db;

-- ---------------------------------------------------------------------
-- 2. departments (created first -- everything else references it)
-- ---------------------------------------------------------------------
CREATE TABLE departments (
    department_id   SERIAL PRIMARY KEY,          -- MySQL: INT AUTO_INCREMENT PRIMARY KEY
    dept_name        VARCHAR(100) NOT NULL,
    hod_name         VARCHAR(100),
    budget           DECIMAL(12,2)
);

-- ---------------------------------------------------------------------
-- 3. students
-- ---------------------------------------------------------------------
CREATE TABLE students (
    student_id       SERIAL PRIMARY KEY,          -- MySQL: INT AUTO_INCREMENT PRIMARY KEY
    first_name       VARCHAR(50)  NOT NULL,
    last_name        VARCHAR(50)  NOT NULL,
    email            VARCHAR(100) NOT NULL UNIQUE,
    date_of_birth    DATE,
    department_id    INT,
    enrollment_year  INT,
    CONSTRAINT fk_students_department
        FOREIGN KEY (department_id) REFERENCES departments (department_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- ---------------------------------------------------------------------
-- 4. courses
-- ---------------------------------------------------------------------
CREATE TABLE courses (
    course_id        SERIAL PRIMARY KEY,          -- MySQL: INT AUTO_INCREMENT PRIMARY KEY
    course_name      VARCHAR(150) NOT NULL,
    course_code      VARCHAR(20)  UNIQUE,
    credits          INT,
    department_id    INT,
    CONSTRAINT fk_courses_department
        FOREIGN KEY (department_id) REFERENCES departments (department_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- ---------------------------------------------------------------------
-- 5. enrollments (the "junction" table between students and courses)
-- ---------------------------------------------------------------------
CREATE TABLE enrollments (
    enrollment_id    SERIAL PRIMARY KEY,          -- MySQL: INT AUTO_INCREMENT PRIMARY KEY
    student_id       INT NOT NULL,
    course_id        INT NOT NULL,
    enrollment_date  DATE,
    grade            CHAR(2),                     -- nullable: A, B, C, D, F
    CONSTRAINT fk_enrollments_student
        FOREIGN KEY (student_id) REFERENCES students (student_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_enrollments_course
        FOREIGN KEY (course_id) REFERENCES courses (course_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- ---------------------------------------------------------------------
-- 6. professors
-- ---------------------------------------------------------------------
CREATE TABLE professors (
    professor_id     SERIAL PRIMARY KEY,          -- MySQL: INT AUTO_INCREMENT PRIMARY KEY
    prof_name        VARCHAR(100) NOT NULL,
    email            VARCHAR(100) UNIQUE,
    department_id    INT,
    salary           DECIMAL(10,2),
    CONSTRAINT fk_professors_department
        FOREIGN KEY (department_id) REFERENCES departments (department_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- ---------------------------------------------------------------------
-- 7. Verification
-- ---------------------------------------------------------------------
-- PostgreSQL:
--   \d departments
--   \d students
--   \d courses
--   \d enrollments
--   \d professors
--
-- MySQL:
--   DESCRIBE departments;
--   DESCRIBE students;
--   DESCRIBE courses;
--   DESCRIBE enrollments;
--   DESCRIBE professors;
