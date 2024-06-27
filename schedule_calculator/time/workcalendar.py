import datetime
from dataclasses import dataclass
from typing import List, Optional

from holidays import HolidayBase

from schedule_calculator.time.schedule import Schedule


@dataclass(frozen=True)
class WorkCalendar:
    current_date: datetime.date
    standard_time: datetime.timedelta
    short_time: datetime.timedelta
    launch_time: datetime.timedelta
    short_days: List[str]
    free_days: HolidayBase
    continuous_schedule: Optional[Schedule] = None
