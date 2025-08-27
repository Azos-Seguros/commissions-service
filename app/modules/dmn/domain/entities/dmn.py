from dataclasses import dataclass
import datetime
from typing import Optional
from uuid import UUID, uuid4

from app.modules.dmn.adapters.dtos import CreateDMNDTO
from app.modules.dmn.domain.enums import RecurrenceType
from app.modules.dmn.domain.models.dmn import DMNModel


@dataclass
class DMN:
    id: UUID
    account_id: str
    commission_percentage: float
    take_rate_percentage: Optional[float]
    recurrence_type: RecurrenceType
    created_at: datetime.datetime
    updated_at: datetime.datetime

    @staticmethod
    def create(data: CreateDMNDTO) -> "DMN":
        return DMN(
            id=uuid4(),
            account_id=data.account_id,
            commission_percentage=data.commission_percentage,
            take_rate_percentage=data.take_rate_percentage,
            recurrence_type=data.recurrence_type,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )

    def to_model(self) -> DMNModel:
        return DMNModel(
            id=str(self.id),
            account_id=self.account_id,
            commission_percentage=self.commission_percentage,
            take_rate_percentage=self.take_rate_percentage,
            recurrence_type=self.recurrence_type,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
