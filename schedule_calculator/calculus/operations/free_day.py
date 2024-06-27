import datetime
from typing import Tuple

from schedule_calculator.calculus.operations.interface import Operation
from schedule_calculator.time.workcalendar import WorkCalendar
from schedule_calculator.time.workday import Workday


class FreeDayOperation(Operation):

    def calculate_worked_time(self, work_day: Workday) -> Tuple[datetime.timedelta, datetime.timedelta]:
        return work_day.end - work_day.start, datetime.timedelta(hours=0)

    def calculate_extra_time(self, work_day: Workday) -> datetime.timedelta:
        return work_day.end - work_day.start

    def fulfill(self, work_day: Workday) -> bool:
        return not self.schedule.free_days.is_workday(work_day.start)

    def __init__(self, schedule: WorkCalendar):
        self.schedule = schedule
