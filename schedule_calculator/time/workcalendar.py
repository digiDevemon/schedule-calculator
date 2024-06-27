import datetime
from dataclasses import dataclass
from typing import List, Optional

from holidays import HolidayBase


@dataclass(frozen=True)
class Schedule:
    current_date: datetime.date
    standard_time: datetime.timedelta
    short_time: datetime.timedelta
    launch_time: datetime.timedelta
    continuous_time: datetime.timedelta
    short_days: List[str]
    free_days: HolidayBase
    continuous_period: Optional[dict] = None
