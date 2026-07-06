"""add course_schedules table

Hands-On 7 : Task 2 (Step 102)
Generated via: alembic revision --autogenerate -m "add course_schedules table"

Revision ID: 0003
Revises: 0002
Create Date: 2024-02-01 14:00:00
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "0003"
down_revision: Union[str, None] = "0002"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "course_schedules",
        sa.Column("schedule_id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("course_id", sa.Integer(), sa.ForeignKey("courses.course_id"), nullable=False),
        sa.Column("day_of_week", sa.String(length=10), nullable=False),
        sa.Column("start_time", sa.String(length=5), nullable=False),
        sa.Column("end_time", sa.String(length=5), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("course_schedules")
