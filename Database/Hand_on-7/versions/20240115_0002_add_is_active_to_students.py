"""add is_active to students

Hands-On 7 : Task 2 (Steps 98-101)
Generated via: alembic revision --autogenerate -m "add is_active to students"

Revision ID: 0002
Revises: 0001
Create Date: 2024-01-15 10:30:00
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "0002"
down_revision: Union[str, None] = "0001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "students",
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
    )


def downgrade() -> None:
    op.drop_column("students", "is_active")
