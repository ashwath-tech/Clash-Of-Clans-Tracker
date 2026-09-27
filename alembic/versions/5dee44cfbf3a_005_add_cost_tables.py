"""005_add_cost_tables

Revision ID: 5dee44cfbf3a
Revises: 586758cca3b5
Create Date: 2026-09-27 00:41:31.572394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5dee44cfbf3a'
down_revision: Union[str, Sequence[str], None] = '586758cca3b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "cost_buildings",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("thing", sa.String(), nullable=False),
        sa.Column("category", sa.String(), nullable=False),
        *[
            col
            for i in range(1, 19)  # level1..level18
            for col in (
                sa.Column(f"gold_level{i}", sa.Integer(), nullable=True),
                sa.Column(f"elixir_level{i}", sa.Integer(), nullable=True),
                sa.Column(f"dark_elixir_level{i}", sa.Integer(), nullable=True),
            )
        ],
    )

    op.create_table(
        "cost_troops",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("thing", sa.String(), nullable=False),
        sa.Column("category", sa.String(), nullable=False),
        *[
            col
            for i in range(1, 22)  # level1..level21
            for col in (
                sa.Column(f"gold_level{i}", sa.Integer(), nullable=True),
                sa.Column(f"elixir_level{i}", sa.Integer(), nullable=True),
                sa.Column(f"dark_elixir_level{i}", sa.Integer(), nullable=True),
            )
        ],
    )

    op.create_table(
        "cost_heroes",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("thing", sa.String(), nullable=False),
        sa.Column("category", sa.String(), nullable=False),
        *[
            col
            for i in range(1, 96)  # level1..level95
            for col in (
                sa.Column(f"gold_level{i}", sa.Integer(), nullable=True),
                sa.Column(f"elixir_level{i}", sa.Integer(), nullable=True),
                sa.Column(f"dark_elixir_level{i}", sa.Integer(), nullable=True),
            )
        ],
    )


def downgrade():
    op.drop_table("cost_heroes")
    op.drop_table("cost_troops")
    op.drop_table("cost_buildings")
