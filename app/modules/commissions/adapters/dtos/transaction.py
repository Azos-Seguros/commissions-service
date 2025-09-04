from dataclasses import dataclass
from app.modules.commissions.domain.enums import TransactionType


@dataclass
class CreateTransactionDTO:
    status: str
    policy_id: str
    invoice_id: str
    proposal_id: str
    gross_amount: float
    raw_transaction_id: str
    external_invoice_id: str
    external_receivable_id: str
    transaction_type: TransactionType
