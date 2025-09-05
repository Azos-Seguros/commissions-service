from app.modules.commissions.application.strategies import (
    DailyStrategy,
    WeeklyStrategy,
    MonthlyStrategy,
)
from app.modules.commissions.domain.interfaces import (
    IRecurrencyStrategy,
)
from app.modules.commissions.domain.interfaces import IPeriodStrategy
from app.modules.dmn.domain.enums import RecurrenceType


class PeriodStrategy(IPeriodStrategy):
    strategies = {
        RecurrenceType.DAILY: DailyStrategy(),
        RecurrenceType.WEEKLY: WeeklyStrategy(),
        RecurrenceType.MONTHLY: MonthlyStrategy(),
    }

    @classmethod
    def get_strategy(cls, recurrence: RecurrenceType) -> IRecurrencyStrategy:
        return cls.strategies[recurrence]
