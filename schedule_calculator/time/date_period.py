import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class DatePeriod:
    start: datetime.date
    end: datetime.date
