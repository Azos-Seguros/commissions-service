import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field

from app.modules.dmn.adapters.dtos import CreateDMNDTO, GetDMNDTO
from app.modules.dmn.domain.enums import RecurrenceType


class DMN(BaseModel):
    model_config = {"arbitrary_types_allowed": True}

    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    broker_id: str = Field(..., description="ID do broker")
    commission_percentage: float = Field(..., description="Porcentagem de comissão")
    take_rate_percentage: Optional[float] = Field(
        ..., description="Porcentagem de take rate"
    )
    cutoff_day: int = Field(..., description="Dia de corte")
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
            broker_id=data.broker_id,
            cutoff_day=data.cutoff_day,
            recurrence_type=data.recurrence_type,
            take_rate_percentage=data.take_rate_percentage,
            commission_percentage=data.commission_percentage,
        )

    def to_dto(self) -> GetDMNDTO:
        return GetDMNDTO(
            broker_id=self.broker_id,
            cutoff_day=self.cutoff_day,
            recurrence_type=self.recurrence_type,
            take_rate_percentage=self.take_rate_percentage,
            commission_percentage=self.commission_percentage,
        )
