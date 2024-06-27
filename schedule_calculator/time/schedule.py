import datetime
from dataclasses import dataclass
from typing import List, Optional, Dict


@dataclass(frozen=True)
class Schedule:
    work_time: datetime.timedelta
    days: Optional[List[str]] = None
    period: Optional[Dict[str, datetime.date]] = None
