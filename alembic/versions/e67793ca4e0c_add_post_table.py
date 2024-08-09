"""add post table

Revision ID: e67793ca4e0c
Revises: b3576ed23e90
Create Date: 2024-08-09 21:33:01.114611

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e67793ca4e0c'
down_revision: Union[str, None] = 'b3576ed23e90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
