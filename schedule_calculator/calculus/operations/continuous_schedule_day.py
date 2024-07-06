import datetime
from typing import Tuple
from typing import cast

from schedule_calculator.calculus.operations.interface import Operation
from schedule_calculator.time.schedule import Schedule
from schedule_calculator.time.work_calendar import WorkCalendar
from schedule_calculator.time.workday import Workday


class ContinuousDayScheduleOperation(Operation):
    def fulfill(self, work_day: Workday) -> bool:
        if not self.schedule.continuous_schedule:
            return False

        if not self.schedule.continuous_schedule.period:
            return False

        return work_day.is_in_period(cast(datetime.date, self.schedule.continuous_schedule.period.start),
                                     cast(datetime.date, self.schedule.continuous_schedule.period.end))

    def calculate_extra_time(self, work_day: Workday) -> datetime.timedelta:
        return work_day.end - work_day.start - cast(Schedule, self.schedule.continuous_schedule).work_time

    def calculate_worked_time(self, work_day: Workday) -> Tuple[datetime.timedelta, datetime.timedelta]:
        return work_day.end - work_day.start, cast(Schedule, self.schedule.continuous_schedule).work_time

    def __init__(self, schedule: WorkCalendar):
        self.schedule = schedule
