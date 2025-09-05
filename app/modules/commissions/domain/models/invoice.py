from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, DateTime, Numeric, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.shared.infrastructure.postgres import db


class InvoiceModel(db.Base):
    __tablename__ = "invoices"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    beneficiary_id = Column(String, nullable=False)
    sequence_number = Column(
        Integer,
        nullable=True,
    )
    invoice_type = Column(String, nullable=False)
    gross_amount = Column(Numeric(15, 3), nullable=False)
    net_amount = Column(Numeric(15, 3), nullable=True)
    status = Column(String, nullable=False)
    payment_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    transactions = relationship("TransactionModel", back_populates="invoice")
