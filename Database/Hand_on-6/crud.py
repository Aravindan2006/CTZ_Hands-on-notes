"""
Hands-On 6 : Task 2 & Task 3
CRUD via SQLAlchemy's Session API, then eliminating N+1 with joinedload.

--------------------------------------------------------------------
N+1 COMPARISON (Step 90) -- with engine echo=True enabled:

  Task 2, Step 84 (lazy loading, naive loop over e.student / e.course):
      1 query to fetch all Enrollment rows
    + 1 query per row to lazily load enrollment.student
    + 1 query per row to lazily load enrollment.course
    -----------------------------------------------------------------
      For 4 sample enrollments -> 1 + 4 + 4 = 9 queries executed
      (in the PDF's fuller sample data with 12 enrollments, this is the
       classic "13 queries executed" scenario: 1 + 12).

  Task 3, Step 88-89 (joinedload eager loading):
      session.query(Enrollment)
             .options(joinedload(Enrollment.student), joinedload(Enrollment.course))
             .all()
      -----------------------------------------------------------------
      -> 1 single SQL statement with LEFT OUTER JOINs to students and
         courses. Query count drops from N+1 (9, or 13 on the full
         dataset) down to exactly 1.
--------------------------------------------------------------------
"""

from sqlalchemy.orm import joinedload

from database import get_session, engine
from models import Department, Student, Course, Enrollment


# =======================================================================
# Task 2 : CRUD Operations via ORM
# =======================================================================

# ---------------------------------------------------------------------
# 81. INSERT: 3 Departments + 5 Students
# ---------------------------------------------------------------------
def seed_departments_and_students():
    with get_session() as session:
        departments = [
            Department(dept_name="Computer Science", head_of_dept="Dr. Ramesh Kumar", budget=850000.00),
            Department(dept_name="Electronics", head_of_dept="Dr. Priya Nair", budget=620000.00),
            Department(dept_name="Mechanical", head_of_dept="Dr. Suresh Iyer", budget=540000.00),
        ]
        session.add_all(departments)
        session.flush()  # populate department_id values before use below

        students = [
            Student(first_name="Arjun", last_name="Mehta", email="arjun.mehta@college.edu",
                    department_id=departments[0].department_id, enrollment_year=2022),
            Student(first_name="Priya", last_name="Suresh", email="priya.suresh@college.edu",
                    department_id=departments[0].department_id, enrollment_year=2022),
            Student(first_name="Rohan", last_name="Verma", email="rohan.verma@college.edu",
                    department_id=departments[1].department_id, enrollment_year=2021),
            Student(first_name="Sneha", last_name="Patel", email="sneha.patel@college.edu",
                    department_id=departments[2].department_id, enrollment_year=2023),
            Student(first_name="Vikram", last_name="Das", email="vikram.das@college.edu",
                    department_id=departments[0].department_id, enrollment_year=2022),
        ]
        session.add_all(students)
        print(f"Inserted {len(departments)} departments and {len(students)} students.")


# ---------------------------------------------------------------------
# 82. INSERT: 3 Courses + 4 Enrollments
# ---------------------------------------------------------------------
def seed_courses_and_enrollments():
    with get_session() as session:
        cs_dept = session.query(Department).filter_by(dept_name="Computer Science").first()

        courses = [
            Course(course_name="Data Structures & Algorithms", course_code="CS101",
                   credits=4, department_id=cs_dept.department_id),
            Course(course_name="Database Management Systems", course_code="CS102",
                   credits=3, department_id=cs_dept.department_id),
            Course(course_name="Object Oriented Programming", course_code="CS103",
                   credits=4, department_id=cs_dept.department_id),
        ]
        session.add_all(courses)
        session.flush()

        students = session.query(Student).filter_by(department_id=cs_dept.department_id).all()

        enrollments = [
            Enrollment(student_id=students[0].student_id, course_id=courses[0].course_id,
                       enrollment_date="2022-07-01", grade="A"),
            Enrollment(student_id=students[0].student_id, course_id=courses[1].course_id,
                       enrollment_date="2022-07-01", grade="B"),
            Enrollment(student_id=students[1].student_id, course_id=courses[0].course_id,
                       enrollment_date="2022-07-01", grade="B"),
            Enrollment(student_id=students[1].student_id, course_id=courses[2].course_id,
                       enrollment_date="2022-07-01", grade="A"),
        ]
        session.add_all(enrollments)
        print(f"Inserted {len(courses)} courses and {len(enrollments)} enrollments.")


# ---------------------------------------------------------------------
# 83. READ: all students in department 'Computer Science'
# ---------------------------------------------------------------------
def get_students_in_department(dept_name: str):
    with get_session() as session:
        students = (
            session.query(Student)
            .join(Department)
            .filter(Department.dept_name == dept_name)
            .all()
        )
        for s in students:
            print(f"{s.first_name} {s.last_name} -- {dept_name}")
        return students


# ---------------------------------------------------------------------
# 84. READ (naive / lazy -- will show N+1 with echo=True): every
#     enrollment's student name and course name
# ---------------------------------------------------------------------
def list_enrollments_naive():
    with get_session() as session:
        enrollments = session.query(Enrollment).all()
        for e in enrollments:
            # Each of these two lines triggers a LAZY LOAD -- i.e. a
            # separate SELECT -- the first time .student / .course is
            # accessed on a given row. With echo=True this is where the
            # N+1 query explosion becomes visible in the SQL log.
            print(f"{e.student.first_name} {e.student.last_name} -> {e.course.course_name}")


# ---------------------------------------------------------------------
# 85. UPDATE: find student by email, update enrollment_year
# ---------------------------------------------------------------------
def update_student_enrollment_year(email: str, new_year: int):
    with get_session() as session:
        student = session.query(Student).filter_by(email=email).first()
        if student is None:
            print(f"No student found with email {email}")
            return
        student.enrollment_year = new_year
        print(f"Updated {student.first_name} {student.last_name} -> enrollment_year={new_year}")


# ---------------------------------------------------------------------
# 86. DELETE: remove an enrollment record
# ---------------------------------------------------------------------
def delete_enrollment(enrollment_id: int):
    with get_session() as session:
        enrollment = session.get(Enrollment, enrollment_id)
        if enrollment is None:
            print(f"No enrollment found with id {enrollment_id}")
            return
        session.delete(enrollment)
        print(f"Deleted enrollment {enrollment_id}")


# =======================================================================
# Task 3 : Eager Loading to Fix N+1
# =======================================================================

# ---------------------------------------------------------------------
# 88-89. joinedload version -- 1 query instead of N+1
# ---------------------------------------------------------------------
def list_enrollments_optimized():
    with get_session() as session:
        enrollments = (
            session.query(Enrollment)
            .options(
                joinedload(Enrollment.student),
                joinedload(Enrollment.course),
            )
            .all()
        )
        for e in enrollments:
            # student/course are already loaded in the same JOIN query --
            # no additional SELECTs are issued here.
            print(f"{e.student.first_name} {e.student.last_name} -> {e.course.course_name}")


if __name__ == "__main__":
    seed_departments_and_students()
    seed_courses_and_enrollments()

    print("\n--- CS students ---")
    get_students_in_department("Computer Science")

    print("\n--- Naive (N+1) enrollment listing ---")
    print(f"(engine.echo = {engine.echo} -- enable True to see the raw SQL log)")
    list_enrollments_naive()

    print("\n--- Optimised (joinedload) enrollment listing ---")
    list_enrollments_optimized()

    print("\n--- Update + delete demo ---")
    update_student_enrollment_year("arjun.mehta@college.edu", 2023)
