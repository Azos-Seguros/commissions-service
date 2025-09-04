from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship

from app.shared.infrastructure.postgres import db


class TransactionModel(db.Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    policy_id = Column(String, nullable=False)
    proposal_id = Column(String, nullable=False)
    external_receivable_id = Column(
        String, nullable=False
    )  # id da recebível no azos.dis
    external_invoice_id = Column(String, nullable=False)  # id da fatura no azos.dis
    gross_amount = Column(Numeric(15, 3), nullable=False)
    net_amount = Column(Numeric(15, 3), nullable=True)
    iss = Column(Numeric(15, 3), nullable=True)
    status = Column(String, nullable=False)
    transaction_type = Column(String, nullable=False)
    raw_transaction_id = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    invoice_id = Column(String, ForeignKey("invoices.id"), nullable=False)
    invoice = relationship("InvoiceModel", back_populates="transactions")
