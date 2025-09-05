from datetime import datetime, timedelta

from app.modules.commissions.domain.interfaces import IRecurrencyStrategy


class DailyStrategy(IRecurrencyStrategy):
    def get_period(self, created_at: datetime, cutoff_day: int | None = None):
        start = created_at.replace(hour=0, minute=0, second=0, microsecond=0)
        end = start + timedelta(days=1)
        return start, end
