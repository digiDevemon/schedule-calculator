import datetime
from typing import Tuple

from schedule_calculator.calculus.operations.interface import Operation
from schedule_calculator.time.work_calendar import WorkCalendar
from schedule_calculator.time.workday import Workday


class UsualDayOperation(Operation):

    def calculate_worked_time(self, work_day: Workday) -> Tuple[datetime.timedelta, datetime.timedelta]:
        return work_day.end - work_day.start - self.schedule.launch_time, self.schedule.standard_time

    def calculate_extra_time(self, work_day: Workday) -> datetime.timedelta:
        return work_day.end - work_day.start - self.schedule.launch_time - self.schedule.standard_time

    def fulfill(self, work_day: Workday) -> bool:
        return self.schedule.free_days.is_workday(work_day.start)

    def __init__(self, schedule: WorkCalendar):
        self.schedule = schedule
