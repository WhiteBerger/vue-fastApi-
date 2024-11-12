"""create_movies_table

Revision ID: a2e9a90c72a7
Revises: d8d274e8ba74
Create Date: 2024-06-17 21:15:17.917154

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2e9a90c72a7'
down_revision: Union[str, None] = 'd8d274e8ba74'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "movies",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.VARCHAR(30),  nullable=False),
        sa.Column("year", sa.VARCHAR(20), nullable=False),
        sa.Column("image", sa.VARCHAR(300), nullable=False)
    )
def downgrade() -> None:
    op.drop_table("movies")



