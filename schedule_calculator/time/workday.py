import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class Workday:
    start: datetime.datetime
    end: datetime.datetime

    def get_day(self) -> str:
        return self.start.strftime("%A")

    def is_in_period(self, init_date: datetime.date, end_date: datetime.date):
        return init_date <= self.start.date() <= end_date
