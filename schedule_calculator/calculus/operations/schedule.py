import datetime
from typing import Tuple, cast, Optional, List

from schedule_calculator.calculus.operations.interface import Operation
from schedule_calculator.time.date_period import DatePeriod
from schedule_calculator.time.schedule import Schedule
from schedule_calculator.time.workday import Workday


class ScheduleOperation(Operation):
    def fulfill(self, work_day: Workday) -> bool:
        if not self.schedule:
            return False

        if not self.schedule.period and not self.schedule.days:
            return False

        return self.__is_in_days(work_day) or self.__is_in_period(work_day)

    def __is_in_period(self, work_day: Workday) -> bool:
        return work_day.is_in_period(cast(DatePeriod, cast(Schedule, self.schedule).period).start,
                                     cast(DatePeriod, cast(Schedule, self.schedule).period).end)

    def __is_in_days(self, work_day: Workday) -> bool:
        return work_day.get_day() in cast(List[str], cast(Schedule, self.schedule).days)

    def calculate_extra_time(self, work_day: Workday) -> datetime.timedelta:
        return work_day.end - work_day.start - cast(Schedule, self.schedule).work_time

    def calculate_worked_time(self, work_day: Workday) -> Tuple[datetime.timedelta, datetime.timedelta]:
        return work_day.end - work_day.start, cast(Schedule, self.schedule).work_time

    def __init__(self, schedule: Optional[Schedule]):
        self.schedule = schedule
