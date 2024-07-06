import datetime
from dataclasses import dataclass
from typing import List, Optional

from schedule_calculator.time.date_period import DatePeriod


@dataclass
class Schedule:
    work_time: datetime.timedelta
    days: Optional[List[str]] = None
    period: Optional[DatePeriod] = None
