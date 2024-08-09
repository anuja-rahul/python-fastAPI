"""add title column to post table

Revision ID: a2eea0496267
Revises: f994931c3ca8
Create Date: 2024-08-09 21:36:32.009061

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2eea0496267'
down_revision: Union[str, None] = 'f994931c3ca8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "title")
    pass
