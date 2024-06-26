import datetime
from typing import Tuple

from schedule_calculator.calculus.operations.interface import Operation
from schedule_calculator.time.schedule import Schedule
from schedule_calculator.time.workday import Workday


class ContinuousDayScheduleOperation(Operation):
    def fulfill(self, work_day: Workday) -> bool:
        if not self.schedule.continuous_period:
            return False

        return work_day.is_in_period(self.schedule.continuous_period["start"], self.schedule.continuous_period["end"])

    def calculate_extra_time(self, work_day: Workday) -> datetime.timedelta:
        return work_day.end - work_day.start - self.schedule.continuous_time

    def calculate_worked_time(self, work_day: Workday) -> Tuple[datetime.timedelta, datetime.timedelta]:
        return work_day.end - work_day.start, self.schedule.continuous_time

    def __init__(self, schedule: Schedule):
        self.schedule = schedule
