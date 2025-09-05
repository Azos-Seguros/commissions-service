import datetime
from uuid import uuid4
from pydantic import BaseModel, Field

from app.modules.commissions.adapters.dtos import CreateTransactionDTO
from app.modules.commissions.domain.models import TransactionModel


class Transaction(BaseModel):
    model_config = {"arbitrary_types_allowed": True}

    id: str = Field(default=lambda: str(uuid4()))
    invoice_id: str = Field(..., description="ID da invoice")
    gross_amount: float = Field(..., description="Valor bruto")
    status: str = Field(..., description="Status")
    transaction_type: str = Field(..., description="Tipo de transação")
    external_transaction_id: str = Field(..., description="ID da transação externa")
    created_at: datetime = Field(
        ..., default_factory=datetime.datetime.now, description="Data de criação"
    )
    updated_at: datetime = Field(
        ..., default_factory=datetime.datetime.now, description="Data de atualização"
    )

    @staticmethod
    def create(
        data: CreateTransactionDTO,
    ) -> "Transaction":
        return Transaction(
            status=data.status,
            policy_id=data.policy_id,
            invoice_id=data.invoice_id,
            proposal_id=data.proposal_id,
            gross_amount=data.gross_amount,
            raw_transaction_id=data.raw_transaction_id,
            transaction_type=data.transaction_type,
            external_invoice_id=data.external_invoice_id,
            external_receivable_id=data.external_receivable_id,
        )

    def to_model(self) -> "TransactionModel":
        return TransactionModel(
            id=self.id,
            status=self.status,
            policy_id=self.policy_id,
            invoice_id=self.invoice_id,
            proposal_id=self.proposal_id,
            gross_amount=self.gross_amount,
            transaction_type=self.transaction_type,
            raw_transaction_id=self.raw_transaction_id,
            external_invoice_id=self.external_invoice_id,
            external_receivable_id=self.external_receivable_id,
        )
