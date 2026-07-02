"""
main.py — Hands-On 6
FastAPI entry point: Pydantic validation, path/query params, async DB access
via dependency injection, pagination and filtering.
"""
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db, init_db, AsyncSessionLocal
from models import Course, Department
from schemas import CourseCreate, CourseResponse

app = FastAPI(title="Course Management API", version="1.0")


@app.on_event("startup")
async def on_startup():
    await init_db()
    # seed minimal data if empty
    async with AsyncSessionLocal() as db:
        result = await db.execute(select(Department))
        if not result.scalars().first():
            cs = Department(name="Computer Science", head_of_dept="Dr. Rao")
            ee = Department(name="Electrical Engineering", head_of_dept="Dr. Iyer")
            db.add_all([cs, ee])
            await db.commit()
            await db.refresh(cs)
            await db.refresh(ee)
            db.add_all([
                Course(name="Data Structures", code="CS101", credits=4, department_id=cs.id),
                Course(name="Operating Systems", code="CS201", credits=4, department_id=cs.id),
                Course(name="Web Development", code="CS301", credits=3, department_id=cs.id),
                Course(name="Circuit Theory", code="EE101", credits=4, department_id=ee.id),
            ])
            await db.commit()


@app.get("/")
async def root():
    return {"message": "API running"}


@app.post("/api/courses/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    """FastAPI validates `course` against CourseCreate automatically (422 on failure)."""
    new_course = Course(**course.model_dump())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return new_course


@app.get("/api/courses/{course_id}", response_model=CourseResponse)
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    course = await db.get(Course, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@app.get("/api/courses/", response_model=list[CourseResponse])
async def list_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db),
):
    """Task 2, Step 63/67 — pagination + filtering via query params."""
    stmt = select(Course)
    if department_id is not None:
        stmt = stmt.where(Course.department_id == department_id)
    stmt = stmt.offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()
