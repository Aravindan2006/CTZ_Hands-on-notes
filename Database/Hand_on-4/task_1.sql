-- =====================================================================
-- Hands-On 4 : Task 1
-- Baseline Performance -- No Indexes
-- =====================================================================

-- ---------------------------------------------------------------------
-- 48. EXPLAIN on the target query
-- ---------------------------------------------------------------------
-- PostgreSQL:
EXPLAIN ANALYZE
SELECT s.first_name, s.last_name, c.course_name
FROM enrollments e
JOIN students s ON s.student_id = e.student_id
JOIN courses  c ON c.course_id  = e.course_id
WHERE s.enrollment_year = 2022;

-- MySQL:
-- EXPLAIN FORMAT=JSON
-- SELECT s.first_name, s.last_name, c.course_name
-- FROM enrollments e
-- JOIN students s ON s.student_id = e.student_id
-- JOIN courses  c ON c.course_id  = e.course_id
-- WHERE s.enrollment_year = 2022;

-- ---------------------------------------------------------------------
-- 49-50. Sample baseline EXPLAIN output (small sample dataset -- record
--         your own actual output here; this is representative)
-- ---------------------------------------------------------------------
-- PostgreSQL sample output (before indexing):
--
-- Hash Join  (cost=1.20..2.35 rows=4 width=68) (actual time=0.045..0.061 rows=6 loops=1)
--   Hash Cond: (e.course_id = c.course_id)
--   ->  Hash Join  (cost=1.09..2.20 rows=4 width=42) (actual time=0.030..0.041 rows=6 loops=1)
--         Hash Cond: (e.student_id = s.student_id)
--         ->  Seq Scan on enrollments e  (cost=0.00..1.10 rows=10 width=8)
--         ->  Hash  (cost=1.06..1.06 rows=6 width=38)
--               ->  Seq Scan on students s  (cost=0.00..1.06 rows=6 width=38)
--                     Filter: (enrollment_year = 2022)
--   ->  Hash  (cost=1.05..1.05 rows=5 width=34)
--         ->  Seq Scan on courses c  (cost=0.00..1.05 rows=5 width=34)
--
-- Observation: at this row count, PostgreSQL's planner chooses Seq Scan
-- on all three tables (students, enrollments, courses) -- no indexes are
-- being used to filter enrollment_year = 2022. Estimated cost for the
-- students filter step is cost=0.00..1.06. On a tiny table this Seq Scan
-- is actually cheap and reasonable, but the SAME plan on a students
-- table with 500,000 rows would mean scanning every single row just to
-- find the ~2022 subset -- that's where an index becomes essential
-- (see Task 2).
