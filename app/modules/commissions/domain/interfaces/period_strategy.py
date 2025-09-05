from abc import ABC, abstractmethod

from app.modules.commissions.domain.interfaces import (
    IRecurrencyStrategy,
)
from app.modules.dmn.domain.enums import RecurrenceType


class IPeriodStrategy(ABC):
    @abstractmethod
    def get_strategy(self, recurrence: RecurrenceType) -> IRecurrencyStrategy: ...

    pass
