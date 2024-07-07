import datetime
from datetime import timedelta

from schedule_calculator.calculus.exceptions.unknown_operation_day import UnknownOperationDay
from schedule_calculator.calculus.operations import usual_day, short_day, free_day, continuous_schedule_day
from schedule_calculator.time.work_calendar import WorkCalendar
from schedule_calculator.time.workday import Workday


class WorkDayCalculator:

    def __init__(self, schedule: WorkCalendar):
        self.schedule = schedule
        self.operations = [free_day.FreeDayOperation(schedule),
                           continuous_schedule_day.ContinuousDayScheduleOperation(schedule),
                           short_day.ShortDayOperation(schedule),
                           usual_day.UsualDayOperation(schedule)]
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


def create_work_day_calculator(schedule: WorkCalendar):
    return WorkDayCalculator(schedule)
