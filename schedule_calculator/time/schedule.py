import datetime
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Schedule:
    standard_time: datetime.timedelta
    short_time: datetime.timedelta
    launch_time: datetime.timedelta
    continuous_time: datetime.timedelta
    short_days: List[str]
    weekend_days: List[str]
    continuous_period: dict
