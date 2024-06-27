import datetime
from typing import Tuple

from schedule_calculator.calculus.operations.interface import Operation
from schedule_calculator.time.workcalendar import WorkCalendar
from schedule_calculator.time.workday import Workday


class ShortDayOperation(Operation):

    def calculate_worked_time(self, work_day: Workday) -> Tuple[datetime.timedelta, datetime.timedelta]:
        return work_day.end - work_day.start, self.schedule.short_time

    def calculate_extra_time(self, work_day: Workday) -> datetime.timedelta:
        return work_day.end - work_day.start - self.schedule.short_time

    def fulfill(self, work_day: Workday) -> bool:
        return work_day.get_day() in self.schedule.short_days

    def __init__(self, schedule: WorkCalendar):
        self.schedule = schedule
