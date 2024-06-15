import datetime
from datetime import timedelta

from schedule_calculator.calculus.exceptions.unknown_operation_day import UnknownOperationDay
from schedule_calculator.calculus.operations import usual_day, short_day, weekend_day
from schedule_calculator.time.schedule import Schedule
from schedule_calculator.time.workday import Workday


class WorkDayCalculator:

    def __init__(self, schedule: Schedule):
        self.schedule = schedule
        self.operations = [usual_day.UsualDayOperation(schedule),
                           short_day.ShortDayOperation(schedule),
                           weekend_day.WeekendDayOperation(schedule)]
        self.zero_time = timedelta(hours=0)

    def calculate_worked_time(self, workday: Workday) -> (
            tuple)[datetime.timedelta, datetime.timedelta]:

        for operation in self.operations:
            if operation.fulfill(workday):
                return operation.calculate_worked_time(workday)

        raise UnknownOperationDay()

    def calculate_extra_time_today(self, workday: Workday) -> datetime.timedelta:

        for operation in self.operations:
            if operation.fulfill(workday):
                return operation.calculate_extra_time(workday)

        raise UnknownOperationDay()


def create_work_day_calculator(schedule: Schedule):
    return WorkDayCalculator(schedule)
