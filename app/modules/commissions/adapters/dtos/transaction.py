from dataclasses import dataclass

from app.modules.commissions.domain.enums import TransactionType


@dataclass
class CreateTransactionDTO:
    invoice_id: str
    gross_amount: float
    status: str
    transaction_type: TransactionType
