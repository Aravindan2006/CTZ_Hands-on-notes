"""
Hands-On 6 : Task 1 (Steps 75, 77, 78)
SQLAlchemy ORM models mirroring the college_db relational schema.
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Numeric,
    ForeignKey,
    Boolean,
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True, autoincrement=True)
    dept_name = Column(String(100), nullable=False)
    head_of_dept = Column(String(100))
    budget = Column(Numeric(12, 2))

    students = relationship("Student", back_populates="department")
    courses = relationship("Course", back_populates="department")
    professors = relationship("Professor", back_populates="department")

    def __repr__(self):
        return f"<Department id={self.department_id} name={self.dept_name!r}>"


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    date_of_birth = Column(Date)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    enrollment_year = Column(Integer)
    is_active = Column(Boolean, default=True)  # added in Hands-On 7, Task 2

    department = relationship("Department", back_populates="students")
    enrollments = relationship(
        "Enrollment", back_populates="student", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Student id={self.student_id} name={self.first_name} {self.last_name}>"


class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(150), nullable=False)
    course_code = Column(String(20), unique=True)
    credits = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    max_seats = Column(Integer, default=60)

    department = relationship("Department", back_populates="courses")
    enrollments = relationship(
        "Enrollment", back_populates="course", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Course id={self.course_id} code={self.course_code!r}>"


class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.student_id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.course_id"), nullable=False)
    enrollment_date = Column(Date)
    grade = Column(String(2))

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    def __repr__(self):
        return f"<Enrollment id={self.enrollment_id} student={self.student_id} course={self.course_id}>"


class Professor(Base):
    __tablename__ = "professors"

    professor_id = Column(Integer, primary_key=True, autoincrement=True)
    prof_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    salary = Column(Numeric(10, 2))

    department = relationship("Department", back_populates="professors")

    def __repr__(self):
        return f"<Professor id={self.professor_id} name={self.prof_name!r}>"


# ---------------------------------------------------------------------
# Hands-On 7, Task 2 (Step 102): new table added via a later migration
# ---------------------------------------------------------------------
class CourseSchedule(Base):
    __tablename__ = "course_schedules"

    schedule_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("courses.course_id"), nullable=False)
    day_of_week = Column(String(10), nullable=False)  # e.g. 'Monday'
    start_time = Column(String(5), nullable=False)    # 'HH:MM'
    end_time = Column(String(5), nullable=False)       # 'HH:MM'

    course = relationship("Course")

    def __repr__(self):
        return f"<CourseSchedule id={self.schedule_id} course={self.course_id} day={self.day_of_week}>"
