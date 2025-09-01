from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from app.shared.infrastructure.postgres import db


class TransactionModel(db.Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    invoice_id = Column(String, ForeignKey("invoices.id"), nullable=False)
    gross_amount = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    transaction_type = Column(String, nullable=False)
    external_transaction_id = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # Relação: uma Transaction pertence a uma Invoice
    invoice = relationship("Invoice", back_populates="transactions")
