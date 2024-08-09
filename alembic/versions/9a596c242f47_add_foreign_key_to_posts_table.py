"""add foreign key to posts table

Revision ID: 9a596c242f47
Revises: a2eea0496267
Create Date: 2024-08-09 21:40:43.637176

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a596c242f47'
down_revision: Union[str, None] = 'a2eea0496267'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users", 
                          local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", "posts")
    op.drop_column("posts", "owner_id")
    pass
