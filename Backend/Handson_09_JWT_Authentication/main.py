"""
main.py — Hands-On 8: REST API Best Practices
Implements: URL versioning (/api/v1/), plural noun resource naming,
PATCH for partial updates, Location header on POST, offset pagination
envelope, search filtering, and standardised error responses.

------------------------------------------------------------------------------
Task 2, Step 82 — Versioning strategies (comment discussion)
------------------------------------------------------------------------------
1. URL versioning (used here, e.g. /api/v1/courses/): simple, visible in the
   URL, easy to test directly in a browser or curl. Downside: URL changes
   between versions, which can break bookmarks/links.
2. Header-based versioning (e.g. Accept: application/vnd.api+json;version=1):
   keeps URLs clean and stable across versions. Downside: harder to test
   casually (can't just click a link), less discoverable.
------------------------------------------------------------------------------
Task 2, Step 104 style discussion also documented in Hands-On 10's README.
"""
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.responses import Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_, func

from fastapi.middleware.cors import CORSMiddleware
from database import get_db, init_db, AsyncSessionLocal
from auth import router as auth_router, get_current_user
from models import User
from models import Course, Department
from schemas import CourseCreate, CourseUpdate, CourseResponse
from errors import http_exception_handler, validation_exception_handler
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError

app = FastAPI(title="Course Management API", version="1.0.0")

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# Hands-On 9, Task 2, Step 94 — CORS configuration for a local frontend dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)


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
            db.add_all([
                Course(name="Data Structures", code="CS101", credits=4, department_id=cs.id),
                Course(name="Operating Systems", code="CS201", credits=4, department_id=cs.id),
                Course(name="Web Development", code="CS301", credits=3, department_id=cs.id),
            ])
            await db.commit()


V1 = "/api/v1"


# --------------------------------------------------------------------------
# GET /api/v1/courses/  — Task 2, Step 83/84: pagination + search filtering
# --------------------------------------------------------------------------
@app.get(f"{V1}/courses/", tags=["Courses"])
async def list_courses(
    request: Request,
    page: int = 1,
    page_size: int = 10,
    search: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
):
    stmt = select(Course)
    count_stmt = select(func.count()).select_from(Course)

    if search:
        like = f"%{search}%"
        condition = or_(Course.name.ilike(like), Course.code.ilike(like))
        stmt = stmt.where(condition)
        count_stmt = count_stmt.where(condition)

    total = (await db.execute(count_stmt)).scalar_one()

    offset = (page - 1) * page_size
    stmt = stmt.offset(offset).limit(page_size)
    result = await db.execute(stmt)
    courses = result.scalars().all()

    base_url = str(request.url).split("?")[0]
    has_next = offset + page_size < total
    has_prev = page > 1
    next_url = f"{base_url}?page={page + 1}&page_size={page_size}" if has_next else None
    prev_url = f"{base_url}?page={page - 1}&page_size={page_size}" if has_prev else None

    return {
        "count": total,
        "next": next_url,
        "previous": prev_url,
        "results": [CourseResponse.model_validate(c).model_dump() for c in courses],
    }


# --------------------------------------------------------------------------
# POST — Task 1, Step 80/81: 201 + Location header
# --------------------------------------------------------------------------
@app.post(f"{V1}/courses/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED, tags=["Courses"])
async def create_course(
    course: CourseCreate,
    response: Response,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_course = Course(**course.model_dump())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    response.headers["Location"] = f"{V1}/courses/{new_course.id}/"
    return new_course


@app.get(f"{V1}/courses/{{course_id}}/", response_model=CourseResponse, tags=["Courses"])
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    course = await db.get(Course, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail=f"Course with id {course_id} does not exist")
    return course


@app.put(f"{V1}/courses/{{course_id}}/", response_model=CourseResponse, tags=["Courses"])
async def replace_course(course_id: int, payload: CourseCreate, db: AsyncSession = Depends(get_db)):
    """PUT — full replace, all fields required (Task 1, Step 79)."""
    course = await db.get(Course, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail=f"Course with id {course_id} does not exist")
    for field, value in payload.model_dump().items():
        setattr(course, field, value)
    await db.commit()
    await db.refresh(course)
    return course


@app.patch(f"{V1}/courses/{{course_id}}/", response_model=CourseResponse, tags=["Courses"])
async def patch_course(course_id: int, payload: CourseUpdate, db: AsyncSession = Depends(get_db)):
    """PATCH — partial update, only supplied fields change (Task 1, Step 79)."""
    course = await db.get(Course, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail=f"Course with id {course_id} does not exist")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(course, field, value)
    await db.commit()
    await db.refresh(course)
    return course


@app.delete(f"{V1}/courses/{{course_id}}/", status_code=status.HTTP_204_NO_CONTENT, tags=["Courses"])
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    course = await db.get(Course, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail=f"Course with id {course_id} does not exist")
    await db.delete(course)
    await db.commit()
    return None
