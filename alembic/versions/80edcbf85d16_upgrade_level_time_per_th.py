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
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("thing", sa.String(), nullable=False),
        sa.Column("category", sa.String(), nullable=False),
        *[sa.Column(c, sa.Integer(), nullable=False, server_default="0") for c in ['th2', 'th3', 'th4', 'th5', 'th6', 'th7', 'th8', 'th9', 'th10', 'th11', 'th12', 'th13', 'th14', 'th15', 'th16', 'th17', 'th18']],
    )

    op.create_table(
        "time_per_th_home",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("thing", sa.String(), nullable=False),
        sa.Column("category", sa.String(), nullable=False),
        *[sa.Column(c, sa.Integer(), nullable=True) for c in ['level1', 'level2', 'level3', 'level4', 'level5', 'level6', 'level7', 'level8', 'level9', 'level10', 'level11', 'level12', 'level13', 'level14', 'level15', 'level16', 'level17', 'level18', 'level19', 'level20', 'level21']],
    )

    op.create_table(
        "time_per_level_hero_pet",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("thing", sa.String(), nullable=False),
        sa.Column("category", sa.String(), nullable=False),
        *[sa.Column(c, sa.Integer(), nullable=True) for c in ['level1', 'level2', 'level3', 'level4', 'level5', 'level6', 'level7', 'level8', 'level9', 'level10', 'level11', 'level12', 'level13', 'level14', 'level15', 'level16', 'level17', 'level18', 'level19', 'level20', 'level21', 'level22', 'level23', 'level24', 'level25', 'level26', 'level27', 'level28', 'level29', 'level30', 'level31', 'level32', 'level33', 'level34', 'level35', 'level36', 'level37', 'level38', 'level39', 'level40', 'level41', 'level42', 'level43', 'level44', 'level45', 'level46', 'level47', 'level48', 'level49', 'level50', 'level51', 'level52', 'level53', 'level54', 'level55', 'level56', 'level57', 'level58', 'level59', 'level60', 'level61', 'level62', 'level63', 'level64', 'level65', 'level66', 'level67', 'level68', 'level69', 'level70', 'level71', 'level72', 'level73', 'level74', 'level75', 'level76', 'level77', 'level78', 'level79', 'level80', 'level81', 'level82', 'level83', 'level84', 'level85', 'level86', 'level87', 'level88', 'level89', 'level90', 'level91', 'level92', 'level93', 'level94', 'level95']],
    )


def downgrade():
    op.drop_table("time_per_level_hero_pet")
    op.drop_table("time_per_th_home")
    op.drop_table("levels_per_th_home")