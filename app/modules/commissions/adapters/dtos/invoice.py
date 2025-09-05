from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from app.modules.commissions.domain.enums import InvoiceStatus, InvoiceType


@dataclass
class CreateInvoiceDTO:
    beneficiary_id: str
    gross_amount: float
    status: InvoiceStatus
    payment_date: datetime
    invoice_type: InvoiceType
    net_amount: Optional[float]


@dataclass
class GetInvoiceDTO(CreateInvoiceDTO):
    id: str
    sequence_number: Optional[int]
