from abc import ABC, abstractmethod
from datetime import datetime


class IRecurrencyStrategy(ABC):
    @abstractmethod
    def get_period(
        self, created_at: datetime, cutoff_day: int | None = None
    ) -> tuple[datetime, datetime]: ...

    pass
