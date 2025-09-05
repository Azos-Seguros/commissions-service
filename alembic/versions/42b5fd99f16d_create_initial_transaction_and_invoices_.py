"""create initial transaction and invoices tables

Revision ID: 42b5fd99f16d
Revises:
Create Date: 2025-09-02 09:40:05.996080

"""

from typing import Sequence, Union
from uuid import uuid4

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
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, default=uuid4),
        sa.Column("policy_id", sa.String, nullable=False),
        sa.Column("proposal_id", sa.String, nullable=False),
        sa.Column("invoice_id", sa.UUID(as_uuid=True), nullable=False),
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

    # Criar sequência para sequence_number
    op.execute(
        """
        CREATE SEQUENCE invoice_sequence_number_seq
        START WITH 1
        INCREMENT BY 1
        NO MINVALUE
        NO MAXVALUE
        CACHE 1;
    """
    )

    op.create_table(
        "invoices",
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, default=uuid4),
        sa.Column("status", sa.String, nullable=False),
        sa.Column("beneficiary_id", sa.String, nullable=False),
        sa.Column("net_amount", sa.Numeric(precision=15, scale=3), nullable=False),
        sa.Column("gross_amount", sa.Numeric(precision=15, scale=3), nullable=True),
        sa.Column("invoice_type", sa.String, nullable=False),
        sa.Column(
            "sequence_number",
            sa.Integer,
            nullable=True,
            server_default=sa.text("nextval('invoice_sequence_number_seq')"),
        ),
        sa.Column("payment_date", sa.DateTime, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
    )

    # Criar índice único para garantir sequência única por beneficiary_id + invoice_type
    op.create_index(
        "idx_invoices_beneficiary_type_sequence",
        "invoices",
        ["beneficiary_id", "invoice_type", "sequence_number"],
        unique=True,
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
    op.drop_index("idx_invoices_beneficiary_type_sequence", "invoices")
    op.drop_table("transactions", if_exists=True)
    op.drop_table("invoices", if_exists=True)
    op.execute("DROP SEQUENCE IF EXISTS invoice_sequence_number_seq")
