import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field

from app.modules.dmn.adapters.dtos import CreateDMNDTO
from app.modules.dmn.domain.enums import RecurrenceType


class DMN(BaseModel):
    model_config = {"arbitrary_types_allowed": True}

    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    account_id: str = Field(..., description="ID da conta")
    commission_percentage: float = Field(..., description="Porcentagem de comissão")
    take_rate_percentage: Optional[float] = Field(
        ..., description="Porcentagem de take rate"
    )
    recurrence_type: RecurrenceType = Field(..., description="Tipo de recorrência")
    created_at: datetime.datetime = Field(
        default_factory=datetime.datetime.now, description="Data de criação"
    )
    updated_at: datetime.datetime = Field(
        default_factory=datetime.datetime.now, description="Data de atualização"
    )

    @staticmethod
    def create(data: CreateDMNDTO) -> "DMN":
        return DMN(
            id=ObjectId(),
            account_id=data.account_id,
            commission_percentage=data.commission_percentage,
            take_rate_percentage=data.take_rate_percentage,
            recurrence_type=data.recurrence_type,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )
