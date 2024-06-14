from datetime import datetime

from schedule_calculator.time.clock import Clock
from schedule_calculator.time.workday import Workday


class WorkDayAssembler:

    def __init__(self, clock: Clock):
        self.clock = clock

    def get_workday(self, start_date: datetime, end_date=None) -> Workday:
        if not end_date:
            end_date = self.clock.get_current_time()

        return Workday(start_date, end_date)
