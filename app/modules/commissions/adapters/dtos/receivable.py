from typing import List
from pydantic import BaseModel, Field


class PremiumDiscrimination(BaseModel):
    """The premium discrimination"""

    pass  # Adicione propriedades específicas conforme necessário


class CommissionMember(BaseModel):
    """The commission member"""

    pass  # Adicione propriedades específicas conforme necessário


class ReceivableValidity(BaseModel):
    """The receivable validity"""

    start_date: str = Field(..., description="The receivable start date")
    end_date: str = Field(..., description="The receivable end date")


class Receivable(BaseModel):
    """The receivable"""

    id: str = Field(..., description="The receivable ID")
    start: str = Field(..., description="The receivable start date")
    end: str = Field(..., description="The receivable end date")
    value: float = Field(..., description="The receivable value")
    status: str = Field(..., description="The receivable status")
    coverage_id: str = Field(..., description="The coverage ID")
    settlement_id: str = Field(..., description="The settlement ID")
    commission_members: List[CommissionMember] = Field(
        ..., description="The commission members"
    )
    premium_discrimination: PremiumDiscrimination = Field(
        ..., description="The premium discrimination"
    )


class ReceivableActivatedDTO(BaseModel):
    """azos.dis-a.receivable.activated"""

    proposal_id: str = Field(..., description="The proposal ID")
    policy_number: str = Field(..., description="The policy number")
    policy_id: str = Field(..., description="The policy ID")
    activation_date: str = Field(..., description="The activation date")
    receivable: Receivable = Field(..., description="The receivable")


class ReceivableSettledDTO(BaseModel):
    """azos.dis-a.receivable.settled"""

    policy_number: str = Field(..., description="The policy number")
    proposal_id: str = Field(..., description="The proposal ID")
    policy_id: str = Field(..., description="The policy ID")
    settlement_id: str = Field(..., description="The settlement ID")
    payment_method: str = Field(..., description="The payment method")
    payment_gateway: str = Field(..., description="The payment gateway")
    invoice_id: str = Field(..., description="The invoice ID")
    receivable_id: str = Field(..., description="The receivable ID")
    receivable_validity: ReceivableValidity = Field(
        ..., description="The receivable validity"
    )
    value: float = Field(..., description="The receivable value")
    paid_at: str = Field(..., description="The paid at date")
    commission_members: List[CommissionMember] = Field(
        ..., description="The commission members"
    )
    premium_discrimination: PremiumDiscrimination = Field(
        ..., description="The premium discrimination"
    )
    activate_receivable: bool = Field(..., description="The activate receivable flag")
