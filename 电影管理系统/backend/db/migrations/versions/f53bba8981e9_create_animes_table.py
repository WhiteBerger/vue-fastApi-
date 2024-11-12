"""create_animes_table

Revision ID: f53bba8981e9
Revises: ed2985136f70
Create Date: 2024-07-05 21:15:00.828663

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f53bba8981e9'
down_revision: Union[str, None] = 'ed2985136f70'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "animes",
        sa.Column("id",sa.Integer,primary_key=True,index=True),
        sa.Column("name",sa.VARCHAR(100)),
        sa.Column("year",sa.VARCHAR(20)),
        sa.Column("image",sa.VARCHAR(300)),
        sa.Column("video",sa.VARCHAR(400))
    )


def downgrade() -> None:
    op.drop_table("animes")
