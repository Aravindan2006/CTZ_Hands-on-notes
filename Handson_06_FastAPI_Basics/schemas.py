"""
schemas.py — Hands-On 6, Task 1
Pydantic schemas for request validation and response serialization.
"""
from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None


class CourseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    code: str
    credits: int
    department_id: int


class DepartmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    head_of_dept: Optional[str] = None
    courses: List[CourseResponse] = []
