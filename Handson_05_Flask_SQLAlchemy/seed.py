"""
seed.py — Hands-On 5, Task 1, Step 51
Seeds sample departments and courses. Run with: python seed.py
"""
from app import create_app
from extensions import db
from courses.models import Department, Course, Student, Enrollment

app = create_app()

with app.app_context():
    db.create_all()

    if not Department.query.first():
        cs = Department(name="Computer Science", head_of_dept="Dr. Rao", budget=500000)
        ee = Department(name="Electrical Engineering", head_of_dept="Dr. Iyer", budget=400000)
        db.session.add_all([cs, ee])
        db.session.commit()

        c1 = Course(name="Data Structures", code="CS101", credits=4, department_id=cs.id)
        c2 = Course(name="Operating Systems", code="CS201", credits=4, department_id=cs.id)
        c3 = Course(name="Circuit Theory", code="EE101", credits=4, department_id=ee.id)
        db.session.add_all([c1, c2, c3])
        db.session.commit()

        s1 = Student(first_name="Asha", last_name="Menon", email="asha@college.edu", department_id=cs.id, enrollment_year=2023)
        s2 = Student(first_name="Ravi", last_name="Kumar", email="ravi@college.edu", department_id=cs.id, enrollment_year=2023)
        db.session.add_all([s1, s2])
        db.session.commit()

        db.session.add_all([
            Enrollment(student_id=s1.id, course_id=c1.id),
            Enrollment(student_id=s2.id, course_id=c1.id),
        ])
        db.session.commit()

        print("Seed data created.")
    else:
        print("Data already exists, skipping seed.")
