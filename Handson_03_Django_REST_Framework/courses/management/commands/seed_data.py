"""
courses/management/commands/seed_data.py — Hands-On 2, Task 2
Custom management command to seed sample Departments, Courses, and Students.
Run with: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from django.db.models import Count, F
from courses.models import Department, Course, Student, Enrollment


class Command(BaseCommand):
    help = "Seeds sample data and demonstrates ORM queries (Hands-On 2, Task 2)"

    def handle(self, *args, **options):
        # --- Step 16: create sample objects ---
        cs, _ = Department.objects.get_or_create(
            name="Computer Science", head_of_dept="Dr. Rao", budget=500000
        )
        ee, _ = Department.objects.get_or_create(
            name="Electrical Engineering", head_of_dept="Dr. Iyer", budget=400000
        )

        c1, _ = Course.objects.get_or_create(
            name="Data Structures", code="CS101", credits=4, department=cs
        )
        c2, _ = Course.objects.get_or_create(
            name="Operating Systems", code="CS201", credits=4, department=cs
        )
        c3, _ = Course.objects.get_or_create(
            name="Web Development", code="CS301", credits=3, department=cs
        )
        c4, _ = Course.objects.get_or_create(
            name="Circuit Theory", code="EE101", credits=4, department=ee
        )

        students_data = [
            ("Asha", "Menon", "asha@college.edu", cs, 2023),
            ("Ravi", "Kumar", "ravi@college.edu", cs, 2023),
            ("Divya", "Nair", "divya@college.edu", cs, 2022),
            ("Karan", "Shah", "karan@college.edu", ee, 2024),
            ("Meera", "Pillai", "meera@college.edu", ee, 2024),
        ]
        students = []
        for fn, ln, email, dept, year in students_data:
            s, _ = Student.objects.get_or_create(
                email=email,
                defaults=dict(first_name=fn, last_name=ln, department=dept, enrollment_year=year),
            )
            students.append(s)

        Enrollment.objects.get_or_create(student=students[0], course=c1)
        Enrollment.objects.get_or_create(student=students[1], course=c1)
        Enrollment.objects.get_or_create(student=students[2], course=c2)
        Enrollment.objects.get_or_create(student=students[3], course=c4)

        # --- Step 17: filter courses in a department (uses __ lookup / JOIN) ---
        cs_courses = Course.objects.filter(department__name="Computer Science")
        self.stdout.write(f"CS courses: {[c.name for c in cs_courses]}")

        # --- Step 18: annotate course count per department ---
        counts = Department.objects.annotate(course_count=Count("courses"))
        for d in counts:
            self.stdout.write(f"{d.name}: {d.course_count} courses")

        # --- Step 19: select_related to avoid N+1 queries ---
        students_with_dept = Student.objects.select_related("department").all()
        for s in students_with_dept:
            self.stdout.write(f"{s} -> {s.department}")

        # --- Step 20: bulk update using F() expressions (no Python-side fetch) ---
        Department.objects.update(budget=F("budget") * 1.1)

        self.stdout.write(self.style.SUCCESS("Seed data created and ORM queries demonstrated."))
