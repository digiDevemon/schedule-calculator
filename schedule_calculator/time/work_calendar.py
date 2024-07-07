import datetime
from dataclasses import dataclass
from typing import Optional

from holidays import HolidayBase

from schedule_calculator.time.schedule import Schedule


@dataclass(frozen=True)
class WorkCalendar:
    current_date: datetime.date
    standard_time: datetime.timedelta
    launch_time: datetime.timedelta
    free_days: HolidayBase
    continuous_schedule: Optional[Schedule] = None
    short_schedule: Optional[Schedule] = None
