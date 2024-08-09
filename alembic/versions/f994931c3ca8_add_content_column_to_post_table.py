"""add content column to post table

Revision ID: f994931c3ca8
Revises: e67793ca4e0c
Create Date: 2024-08-09 21:34:50.007934

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f994931c3ca8'
down_revision: Union[str, None] = 'e67793ca4e0c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
