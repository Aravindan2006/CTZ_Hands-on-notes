"""
courses/models.py — Hands-On 5, Task 1
SQLAlchemy models mirroring the Django schema from Hands-On 2.
"""
from datetime import date
from extensions import db


class Department(db.Model):
    __tablename__ = "departments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    head_of_dept = db.Column(db.String(100))
    budget = db.Column(db.Numeric(12, 2), default=0)

    courses = db.relationship("Course", back_populates="department", cascade="all, delete-orphan")
    students = db.relationship("Student", back_populates="department")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "head_of_dept": self.head_of_dept,
            "budget": float(self.budget) if self.budget is not None else None,
        }


class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    credits = db.Column(db.SmallInteger, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"), nullable=False)

    department = db.relationship("Department", back_populates="courses")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "credits": self.credits,
            "department_id": self.department_id,
        }


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"))
    enrollment_year = db.Column(db.Integer)

    department = db.relationship("Department", back_populates="students")

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "department_id": self.department_id,
            "enrollment_year": self.enrollment_year,
        }


class Enrollment(db.Model):
    __tablename__ = "enrollments"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    enrollment_date = db.Column(db.Date, default=date.today)
    grade = db.Column(db.String(2), nullable=True)

    student = db.relationship("Student")
    course = db.relationship("Course")

    __table_args__ = (db.UniqueConstraint("student_id", "course_id", name="uq_student_course"),)

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "course_id": self.course_id,
            "enrollment_date": self.enrollment_date.isoformat() if self.enrollment_date else None,
            "grade": self.grade,
        }
