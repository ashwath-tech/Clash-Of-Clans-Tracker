"""upgrade_level_time_per_th

Revision ID: 80edcbf85d16
Revises: 8026db6dd3b1
Create Date: 2026-09-23 15:04:26.111644

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80edcbf85d16'
down_revision: Union[str, Sequence[str], None] = '8026db6dd3b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table(
        "levels_per_th_home",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("thing", sa.String(), nullable=False),
        sa.Column("category", sa.String(), nullable=False),
        sa.Column("th_level", sa.Integer(), nullable=False),
        sa.Column("unlocked_level", sa.Integer(), nullable=False, server_default="0"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("thing", "category", "th_level"),
    )

    op.create_table(
        "time_per_th_home",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("thing", sa.String(), nullable=False),
        sa.Column("category", sa.String(), nullable=False),
        sa.Column("level", sa.Integer(), nullable=False),
        sa.Column("upgrade_time_seconds", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("thing", "category", "level"),
    )

    op.create_table(
        "time_per_level_hero_pet",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("thing", sa.String(), nullable=False),
        sa.Column("category", sa.String(), nullable=False),
        sa.Column("level", sa.Integer(), nullable=False),
        sa.Column("upgrade_time_seconds", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("thing", "category", "level"),
    )


def downgrade():
    op.drop_table("time_per_level_hero_pet")
    op.drop_table("time_per_th_home")
    op.drop_table("levels_per_th_home")