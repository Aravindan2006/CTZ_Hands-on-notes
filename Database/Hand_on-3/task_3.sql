-- =====================================================================
-- Hands-On 3 : Task 3
-- Stored Procedures / Functions and Transactions
-- =====================================================================

-- =====================================================================
-- ===========================  MySQL VERSION  =========================
-- =====================================================================

-- ---------------------------------------------------------------------
-- 44. sp_enroll_student -- checks for duplicate enrollment, then inserts
-- ---------------------------------------------------------------------
DELIMITER $$

CREATE PROCEDURE sp_enroll_student (
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)
BEGIN
    DECLARE v_existing INT DEFAULT 0;

    SELECT COUNT(*) INTO v_existing
    FROM enrollments
    WHERE student_id = p_student_id
      AND course_id  = p_course_id;

    IF v_existing > 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Duplicate enrollment: student is already enrolled in this course.';
    ELSE
        INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
        VALUES (p_student_id, p_course_id, p_enrollment_date, NULL);
    END IF;
END$$

DELIMITER ;

-- ---------------------------------------------------------------------
-- 45. sp_transfer_student -- moves a student's department inside a
--     transaction, logs the move, rolls back on any failure
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS department_transfer_log (
    log_id            INT AUTO_INCREMENT PRIMARY KEY,
    student_id        INT NOT NULL,
    old_department_id INT,
    new_department_id INT,
    transferred_at    DATETIME DEFAULT CURRENT_TIMESTAMP
);

DELIMITER $$

CREATE PROCEDURE sp_transfer_student (
    IN p_student_id INT,
    IN p_new_department_id INT
)
BEGIN
    DECLARE v_old_department_id INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    START TRANSACTION;

    SELECT department_id INTO v_old_department_id
    FROM students
    WHERE student_id = p_student_id
    FOR UPDATE;

    UPDATE students
    SET department_id = p_new_department_id
    WHERE student_id = p_student_id;

    INSERT INTO department_transfer_log (student_id, old_department_id, new_department_id)
    VALUES (p_student_id, v_old_department_id, p_new_department_id);

    COMMIT;
END$$

DELIMITER ;

-- ---------------------------------------------------------------------
-- 46. Test the transaction with a deliberate failure
--     (invalid FK -> both statements are rolled back automatically by
--      the EXIT HANDLER above)
-- ---------------------------------------------------------------------
-- CALL sp_transfer_student(1, 9999);  -- 9999 does not exist in departments
-- Expected: statement fails on the FK constraint, ROLLBACK fires, and
-- students.department_id for student_id = 1 remains unchanged.

-- ---------------------------------------------------------------------
-- 47. SAVEPOINT demo -- two inserts, savepoint after the first, the
--     second deliberately fails, ROLLBACK TO SAVEPOINT keeps only the
--     first insert
-- ---------------------------------------------------------------------
START TRANSACTION;

INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
VALUES (2, 4, '2024-01-10', NULL);

SAVEPOINT after_first_insert;

-- Deliberate failure: course_id 9999 does not exist -> FK violation
INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
VALUES (2, 9999, '2024-01-10', NULL);

-- Because the second insert fails, roll back only to the savepoint,
-- keeping the first insert intact:
ROLLBACK TO SAVEPOINT after_first_insert;

COMMIT;
-- Expected: enrollment (student_id=2, course_id=4) is persisted;
-- the invalid (student_id=2, course_id=9999) row never exists.

-- =====================================================================
-- =========================  PostgreSQL VERSION  ======================
-- =====================================================================

-- ---------------------------------------------------------------------
-- 44. fn_enroll_student
-- ---------------------------------------------------------------------
-- CREATE OR REPLACE FUNCTION fn_enroll_student(
--     p_student_id INT,
--     p_course_id INT,
--     p_enrollment_date DATE
-- ) RETURNS VOID AS $$
-- DECLARE
--     v_existing INT;
-- BEGIN
--     SELECT COUNT(*) INTO v_existing
--     FROM enrollments
--     WHERE student_id = p_student_id AND course_id = p_course_id;
--
--     IF v_existing > 0 THEN
--         RAISE EXCEPTION 'Duplicate enrollment: student % already enrolled in course %',
--             p_student_id, p_course_id;
--     ELSE
--         INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
--         VALUES (p_student_id, p_course_id, p_enrollment_date, NULL);
--     END IF;
-- END;
-- $$ LANGUAGE plpgsql;

-- ---------------------------------------------------------------------
-- 45. fn_transfer_student
-- ---------------------------------------------------------------------
-- CREATE TABLE IF NOT EXISTS department_transfer_log (
--     log_id            SERIAL PRIMARY KEY,
--     student_id        INT NOT NULL,
--     old_department_id INT,
--     new_department_id INT,
--     transferred_at    TIMESTAMP DEFAULT NOW()
-- );
--
-- CREATE OR REPLACE FUNCTION fn_transfer_student(
--     p_student_id INT,
--     p_new_department_id INT
-- ) RETURNS VOID AS $$
-- DECLARE
--     v_old_department_id INT;
-- BEGIN
--     SELECT department_id INTO v_old_department_id
--     FROM students WHERE student_id = p_student_id;
--
--     UPDATE students SET department_id = p_new_department_id
--     WHERE student_id = p_student_id;
--
--     INSERT INTO department_transfer_log (student_id, old_department_id, new_department_id)
--     VALUES (p_student_id, v_old_department_id, p_new_department_id);
-- EXCEPTION
--     WHEN OTHERS THEN
--         RAISE;  -- re-raise; caller's transaction rolls back automatically
-- END;
-- $$ LANGUAGE plpgsql;

-- ---------------------------------------------------------------------
-- 47. SAVEPOINT demo (PostgreSQL syntax is identical to standard SQL)
-- ---------------------------------------------------------------------
-- BEGIN;
-- INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
-- VALUES (2, 4, '2024-01-10', NULL);
-- SAVEPOINT after_first_insert;
-- INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
-- VALUES (2, 9999, '2024-01-10', NULL);  -- fails: FK violation
-- ROLLBACK TO SAVEPOINT after_first_insert;
-- COMMIT;
