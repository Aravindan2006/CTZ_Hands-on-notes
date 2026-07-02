"""initial schema

Hands-On 7 : Task 1 (Step 95-97)
Generated via: alembic revision --autogenerate -m "initial schema"

Revision ID: 0001
Revises:
Create Date: 2024-01-01 09:00:00
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "0001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "departments",
        sa.Column("department_id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("dept_name", sa.String(length=100), nullable=False),
        sa.Column("head_of_dept", sa.String(length=100), nullable=True),
        sa.Column("budget", sa.Numeric(12, 2), nullable=True),
    )

    op.create_table(
        "students",
        sa.Column("student_id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("first_name", sa.String(length=50), nullable=False),
        sa.Column("last_name", sa.String(length=50), nullable=False),
        sa.Column("email", sa.String(length=100), nullable=False, unique=True),
        sa.Column("date_of_birth", sa.Date(), nullable=True),
        sa.Column("department_id", sa.Integer(), sa.ForeignKey("departments.department_id"), nullable=True),
        sa.Column("enrollment_year", sa.Integer(), nullable=True),
    )

    op.create_table(
        "courses",
        sa.Column("course_id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("course_name", sa.String(length=150), nullable=False),
        sa.Column("course_code", sa.String(length=20), nullable=True, unique=True),
        sa.Column("credits", sa.Integer(), nullable=True),
        sa.Column("department_id", sa.Integer(), sa.ForeignKey("departments.department_id"), nullable=True),
        sa.Column("max_seats", sa.Integer(), server_default="60"),
    )

    op.create_table(
        "enrollments",
        sa.Column("enrollment_id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("student_id", sa.Integer(), sa.ForeignKey("students.student_id"), nullable=False),
        sa.Column("course_id", sa.Integer(), sa.ForeignKey("courses.course_id"), nullable=False),
        sa.Column("enrollment_date", sa.Date(), nullable=True),
        sa.Column("grade", sa.String(length=2), nullable=True),
    )

    op.create_table(
        "professors",
        sa.Column("professor_id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("prof_name", sa.String(length=100), nullable=False),
        sa.Column("email", sa.String(length=100), nullable=True, unique=True),
        sa.Column("department_id", sa.Integer(), sa.ForeignKey("departments.department_id"), nullable=True),
        sa.Column("salary", sa.Numeric(10, 2), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("professors")
    op.drop_table("enrollments")
    op.drop_table("courses")
    op.drop_table("students")
    op.drop_table("departments")
