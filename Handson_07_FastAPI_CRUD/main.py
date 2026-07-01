"""
main.py — Hands-On 7
Full CRUD for Courses/Students/Enrollments with proper HTTP status codes,
response_model filtering, HTTPException error handling, background tasks
for enrollment confirmation emails, and customised OpenAPI docs.
"""
from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db, init_db, AsyncSessionLocal
from models import Course, Department, Student, Enrollment
from schemas import (
    CourseCreate, CourseUpdate, CourseResponse,
    StudentCreate, StudentResponse,
    EnrollmentCreate, EnrollmentResponse,
)

app = FastAPI(
    title="Course Management API",
    description="Backend API for managing departments, courses, students and enrollments.",
    version="1.0.0",
    contact={"name": "Digital Nurture 5.0", "email": "poc@college.edu"},
)


@app.on_event("startup")
async def on_startup():
    await init_db()
    async with AsyncSessionLocal() as db:
        result = await db.execute(select(Department))
        if not result.scalars().first():
            cs = Department(name="Computer Science", head_of_dept="Dr. Rao")
            db.add(cs)
            await db.commit()
            await db.refresh(cs)
            db.add(Course(name="Data Structures", code="CS101", credits=4, department_id=cs.id))
            await db.commit()


def send_confirmation_email(student_email: str):
    """Task 2, Step 73 — simulated background task (runs AFTER the response is sent)."""
    print(f"Sending confirmation to {student_email}")


# ---------------------------- Courses ----------------------------
@app.get("/api/courses/", response_model=list[CourseResponse], tags=["Courses"])
async def list_courses(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course))
    return result.scalars().all()


@app.post(
    "/api/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create a new course",
    response_description="The created course",
)
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    new_course = Course(**course.model_dump())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return new_course


@app.get("/api/courses/{course_id}", response_model=CourseResponse, tags=["Courses"])
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    course = await db.get(Course, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@app.put("/api/courses/{course_id}", response_model=CourseResponse, tags=["Courses"])
async def update_course(course_id: int, payload: CourseUpdate, db: AsyncSession = Depends(get_db)):
    course = await db.get(Course, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(course, field, value)
    await db.commit()
    await db.refresh(course)
    return course


@app.delete("/api/courses/{course_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Courses"])
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    course = await db.get(Course, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    await db.delete(course)
    await db.commit()
    return None


@app.get("/api/courses/{course_id}/students/", response_model=list[StudentResponse], tags=["Courses"])
async def course_students(course_id: int, db: AsyncSession = Depends(get_db)):
    course = await db.get(Course, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    result = await db.execute(
        select(Student).join(Enrollment, Enrollment.student_id == Student.id)
        .where(Enrollment.course_id == course_id)
    )
    return result.scalars().all()


# ---------------------------- Students ----------------------------
@app.get("/api/students/", response_model=list[StudentResponse], tags=["Students"])
async def list_students(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student))
    return result.scalars().all()


@app.post("/api/students/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED, tags=["Students"])
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    new_student = Student(**student.model_dump())
    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    return new_student


@app.get("/api/students/{student_id}", response_model=StudentResponse, tags=["Students"])
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    student = await db.get(Student, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.delete("/api/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Students"])
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    student = await db.get(Student, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    await db.delete(student)
    await db.commit()
    return None


# ---------------------------- Enrollments ----------------------------
@app.post(
    "/api/enrollments/",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Enrollments"],
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    """Task 2, Step 73 — creates the enrollment, returns 201 immediately, and
    schedules a background task to 'send' a confirmation email afterwards."""
    student = await db.get(Student, enrollment.student_id)
    course = await db.get(Course, enrollment.course_id)
    if student is None or course is None:
        raise HTTPException(status_code=404, detail="Student or Course not found")

    new_enrollment = Enrollment(**enrollment.model_dump())
    db.add(new_enrollment)
    await db.commit()
    await db.refresh(new_enrollment)

    background_tasks.add_task(send_confirmation_email, student.email)
    return new_enrollment


@app.get("/api/enrollments/", response_model=list[EnrollmentResponse], tags=["Enrollments"])
async def list_enrollments(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Enrollment))
    return result.scalars().all()
