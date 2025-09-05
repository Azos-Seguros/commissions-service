from datetime import datetime

from app.modules.commissions.domain.interfaces import IRecurrencyStrategy


class MonthlyStrategy(IRecurrencyStrategy):
    def get_period(self, created_at: datetime, cutoff_day: int | None = None):
        if cutoff_day:
            if created_at.day <= cutoff_day:
                start = created_at.replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                )
                end = created_at.replace(
                    day=cutoff_day, hour=23, minute=59, second=59, microsecond=999999
                )
            else:
                start = created_at.replace(
                    day=cutoff_day + 1, hour=0, minute=0, second=0, microsecond=0
                )
                if created_at.month == 12:
                    end = datetime(
                        created_at.year + 1, 1, cutoff_day, 23, 59, 59, 999999
                    )
                else:
                    end = datetime(
                        created_at.year,
                        created_at.month + 1,
                        cutoff_day,
                        23,
                        59,
                        59,
                        999999,
                    )
        else:
            start = created_at.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            if created_at.month == 12:
                end = datetime(created_at.year + 1, 1, 1)
            else:
                end = datetime(created_at.year, created_at.month + 1, 1)
        return start, end
