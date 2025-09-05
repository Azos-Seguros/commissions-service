from datetime import datetime, timedelta

from app.modules.commissions.domain.interfaces import IRecurrencyStrategy


class WeeklyStrategy(IRecurrencyStrategy):
    def get_period(self, created_at: datetime, cutoff_day: int | None = None):
        start = created_at - timedelta(days=created_at.weekday())
        start = start.replace(hour=0, minute=0, second=0, microsecond=0)
        end = start + timedelta(days=7)
        return start, end
