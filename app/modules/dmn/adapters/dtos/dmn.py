from dataclasses import dataclass
from typing import Optional

from app.modules.dmn.domain.enums import RecurrenceType


@dataclass
class CreateDMNDTO:
    broker_id: str
    commission_percentage: float
    recurrence_type: RecurrenceType
    take_rate_percentage: Optional[float] = None
