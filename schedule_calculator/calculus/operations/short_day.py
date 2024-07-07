import datetime
from typing import Tuple
from typing import cast, List

from schedule_calculator.calculus.operations.interface import Operation
from schedule_calculator.time.schedule import Schedule
from schedule_calculator.time.work_calendar import WorkCalendar
from schedule_calculator.time.workday import Workday


class ShortDayOperation(Operation):

    def calculate_worked_time(self, work_day: Workday) -> Tuple[datetime.timedelta, datetime.timedelta]:
        return work_day.end - work_day.start, cast(Schedule, self.schedule.short_schedule).work_time

    def calculate_extra_time(self, work_day: Workday) -> datetime.timedelta:
        return work_day.end - work_day.start - cast(Schedule, self.schedule.short_schedule).work_time

    def fulfill(self, work_day: Workday) -> bool:
        if not self.schedule.short_schedule:
            return False

        return work_day.get_day() in cast(List[str], self.schedule.short_schedule.days)

    def __init__(self, schedule: WorkCalendar):
        self.schedule = schedule
