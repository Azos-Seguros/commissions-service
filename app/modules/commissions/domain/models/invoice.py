from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, Numeric, String
from sqlalchemy.orm import relationship

from app.shared.infrastructure.postgres import db


class InvoiceModel(db.Base):
    __tablename__ = "invoices"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    beneficiary_id = Column(String, nullable=False)
    sequence_number = Column(String, nullable=False)
    invoice_type = Column(String, nullable=False)
    gross_amount = Column(Numeric(15, 3), nullable=False)
    net_amount = Column(Numeric(15, 3), nullable=True)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    transactions = relationship("Transaction", back_populates="invoice")
