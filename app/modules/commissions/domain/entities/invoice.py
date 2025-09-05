import datetime
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

from app.modules.commissions.adapters.dtos import CreateInvoiceDTO, GetInvoiceDTO
from app.modules.commissions.domain.enums import InvoiceStatus, InvoiceType
from app.modules.commissions.domain.models import InvoiceModel


class Invoice(BaseModel):
    model_config = {"arbitrary_types_allowed": True}

    id: UUID = Field(default_factory=uuid4)
    status: InvoiceStatus = Field(..., description="Status")
    beneficiary_id: str = Field(..., description="ID do beneficiário")
    invoice_type: InvoiceType = Field(..., description="Tipo de fatura")
    gross_amount: float = Field(..., description="Valor bruto")
    net_amount: Optional[float] = Field(..., description="Valor líquido")
    payment_date: datetime = Field(..., description="Data de pagamento")
    created_at: datetime = Field(
        ..., default_factory=datetime.datetime.now, description="Data de criação"
    )
    updated_at: datetime = Field(
        ..., default_factory=datetime.datetime.now, description="Data de atualização"
    )
    sequence_number: Optional[int] = Field(None, description="Número da sequência")

    @staticmethod
    def create(data: CreateInvoiceDTO) -> "Invoice":
        return Invoice(
            status=data.status,
            net_amount=data.net_amount,
            invoice_type=data.invoice_type,
            gross_amount=data.gross_amount,
            payment_date=data.payment_date,
            beneficiary_id=data.beneficiary_id,
        )

    def to_model(self) -> "InvoiceModel":
        return InvoiceModel(
            id=self.id,
            status=self.status,
            net_amount=self.net_amount,
            invoice_type=self.invoice_type,
            payment_date=self.payment_date,
            gross_amount=self.gross_amount,
            beneficiary_id=self.beneficiary_id,
            sequence_number=self.sequence_number,
        )

    def to_dto(self) -> GetInvoiceDTO:
        return GetInvoiceDTO(
            id=self.id,
            status=self.status,
            net_amount=self.net_amount,
            invoice_type=self.invoice_type,
            payment_date=self.payment_date,
            gross_amount=self.gross_amount,
            beneficiary_id=self.beneficiary_id,
            sequence_number=self.sequence_number,
        )
