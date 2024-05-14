import datetime
from dataclasses import dataclass


@dataclass
class Schedule:
    standard_time: datetime.timedelta
    short_time: datetime.timedelta
    launch_time: datetime.timedelta
    short_day: str
