"""create_watch_table

Revision ID: ed2985136f70
Revises: cd0413f59d01
Create Date: 2024-06-23 13:22:43.771909

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ed2985136f70'
down_revision: Union[str, None] = 'a2e9a90c72a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        "watch",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("movie_id", sa.Integer, sa.ForeignKey("movies.id") ,nullable=False),
        sa.Column("movie_name",sa.VARCHAR(30),nullable=False),
        sa.Column("movie_image",sa.VARCHAR(300),nullable=False),
        sa.Column("watchTime", sa.TIMESTAMP, nullable=False)
    )


def downgrade() -> None:
    op.drop_table("watch")
