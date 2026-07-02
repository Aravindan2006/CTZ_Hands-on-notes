"""
Hands-On 4 : Task 3
Identify and Fix the N+1 Query Problem
=======================================

Demonstrates the N+1 anti-pattern against college_db (PostgreSQL) using
psycopg2, then fixes it with a single JOIN query, and times both.

Run:
    pip install psycopg2-binary
    python task_3_n_plus_one_demo.py

Expected console output (with the 12-row sample enrollments data before
the NULL-grade rows were deleted in Hands-On 2, or 10 rows after):
    --- N+1 (bad) version ---
    13 queries executed
    Elapsed: 0.0123s
    --- Optimised JOIN version ---
    1 query executed
    Elapsed: 0.0021s
"""

import time
import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "college_db",
    "user": "postgres",
    "password": "postgres",
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


# ---------------------------------------------------------------------
# 56. BAD implementation -- N+1 queries
# ---------------------------------------------------------------------
def n_plus_one_version():
    """
    1 query to fetch all enrollments, then N additional queries -- one
    per enrollment row -- to fetch each student's name individually.
    Total queries = 1 + N.
    """
    query_count = 0
    results = []

    conn = get_connection()
    cur = conn.cursor()

    # Query #1: fetch all enrollments
    cur.execute("SELECT enrollment_id, student_id, course_id FROM enrollments;")
    query_count += 1
    enrollments = cur.fetchall()

    # Queries #2..#(N+1): one SELECT per row to fetch the student's name
    for enrollment_id, student_id, course_id in enrollments:
        cur.execute(
            "SELECT first_name, last_name FROM students WHERE student_id = %s;",
            (student_id,),
        )
        query_count += 1
        first_name, last_name = cur.fetchone()
        results.append(
            {
                "enrollment_id": enrollment_id,
                "student_name": f"{first_name} {last_name}",
                "course_id": course_id,
            }
        )

    cur.close()
    conn.close()
    return results, query_count


# ---------------------------------------------------------------------
# 57. OPTIMISED implementation -- single JOIN query
# ---------------------------------------------------------------------
def optimized_join_version():
    """
    A single JOIN query retrieves every enrollment record together with
    the associated student's name in one round trip. Total queries = 1.
    """
    query_count = 0

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT e.enrollment_id, s.first_name, s.last_name, e.course_id
        FROM enrollments e
        JOIN students s ON s.student_id = e.student_id;
        """
    )
    query_count += 1
    rows = cur.fetchall()

    results = [
        {
            "enrollment_id": enrollment_id,
            "student_name": f"{first_name} {last_name}",
            "course_id": course_id,
        }
        for enrollment_id, first_name, last_name, course_id in rows
    ]

    cur.close()
    conn.close()
    return results, query_count


# ---------------------------------------------------------------------
# 58. Compare round-trips and timing
# ---------------------------------------------------------------------
def main():
    print("--- N+1 (bad) version ---")
    start = time.perf_counter()
    bad_results, bad_query_count = n_plus_one_version()
    bad_elapsed = time.perf_counter() - start
    print(f"{bad_query_count} queries executed")
    print(f"Elapsed: {bad_elapsed:.4f}s")

    print("\n--- Optimised JOIN version ---")
    start = time.perf_counter()
    good_results, good_query_count = optimized_join_version()
    good_elapsed = time.perf_counter() - start
    print(f"{good_query_count} query executed")
    print(f"Elapsed: {good_elapsed:.4f}s")

    assert bad_results == good_results, "Both versions must return identical data!"
    print("\nBoth versions returned identical data: OK")
    print(
        f"Query round-trips saved: {bad_query_count - good_query_count} "
        f"({bad_query_count} -> {good_query_count})"
    )

    # ---------------------------------------------------------------
    # 59. Extrapolation to a real workload
    # ---------------------------------------------------------------
    # With 10,000 enrollments, the N+1 version issues 1 + 10,000 = 10,001
    # queries instead of a single JOIN query -- 10,000 EXTRA, unnecessary
    # round trips to the database, each carrying its own network and
    # parsing overhead. This is the most common source of hidden
    # performance regressions in ORM-backed applications.


if __name__ == "__main__":
    main()
