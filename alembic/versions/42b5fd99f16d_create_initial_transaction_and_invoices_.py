"""create initial transaction and invoices tables

Revision ID: 42b5fd99f16d
Revises:
Create Date: 2025-09-02 09:40:05.996080

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "42b5fd99f16d"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "transactions",
        sa.Column("id", sa.String, primary_key=True),
        sa.Column("policy_id", sa.String, nullable=False),
        sa.Column("proposal_id", sa.String, nullable=False),
        sa.Column("invoice_id", sa.String, nullable=False),
        sa.Column("iss", sa.Numeric(precision=15, scale=3), nullable=True),
        sa.Column("status", sa.String, nullable=False),
        sa.Column("net_amount", sa.Numeric(precision=15, scale=3), nullable=True),
        sa.Column("gross_amount", sa.Numeric(precision=15, scale=3), nullable=False),
        sa.Column("transaction_type", sa.String, nullable=False),
        sa.Column("raw_transaction_id", sa.String, nullable=False),
        sa.Column("external_invoice_id", sa.String, nullable=False),
        sa.Column("external_receivable_id", sa.String, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
    )
    op.create_table(
        "invoices",
        sa.Column("id", sa.String, primary_key=True),
        sa.Column("status", sa.String, nullable=False),
        sa.Column("beneficiary_id", sa.String, nullable=False),
        sa.Column("net_amount", sa.Numeric(precision=15, scale=3), nullable=False),
        sa.Column("gross_amount", sa.Numeric(precision=15, scale=3), nullable=True),
        sa.Column("invoice_type", sa.String, nullable=False),
        sa.Column("sequence_number", sa.String, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
    )
    op.create_foreign_key(
        "fk_transactions_invoice_id",
        "transactions",
        "invoices",
        ["invoice_id"],
        ["id"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("fk_transactions_invoice_id", "transactions", type_="foreignkey")
    op.drop_table("transactions", if_exists=True)
    op.drop_table("invoices", if_exists=True)
