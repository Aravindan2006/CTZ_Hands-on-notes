"""
models.py — Hands-On 7
SQLAlchemy ORM models, extended with Student and Enrollment for full CRUD.
"""
from sqlalchemy import Column, Integer, String, ForeignKey, SmallInteger, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base


class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    head_of_dept = Column(String(100))

    courses = relationship("Course", back_populates="department")


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    code = Column(String(20), unique=True, nullable=False)
    credits = Column(SmallInteger, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="courses")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))


class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)


class User(Base):
    """Hands-On 9, Task 1, Step 86"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(150), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
