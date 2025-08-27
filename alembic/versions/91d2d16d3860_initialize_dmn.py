"""initialize dmn

Revision ID: 91d2d16d3860
Revises:
Create Date: 2025-08-26 04:01:34.623985

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "91d2d16d3860"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "dmn_rules",
        sa.Column("id", sa.String, primary_key=True),
        sa.Column("account_id", sa.String, nullable=False),
        sa.Column("commission_percentage", sa.Float, nullable=False),
        sa.Column("take_rate_percentage", sa.Float, nullable=True),
        sa.Column("recurrence_type", sa.String, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("dmn")
