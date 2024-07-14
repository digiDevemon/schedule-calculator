import datetime
from datetime import timedelta

from schedule_calculator.calculus.exceptions.unknown_operation_day import UnknownOperationDay
from schedule_calculator.calculus.operations import usual_day, free_day, schedule
from schedule_calculator.time.work_calendar import WorkCalendar
from schedule_calculator.time.workday import Workday


class WorkDayCalculator:

    def __init__(self, work_calendar: WorkCalendar):
        self.schedule = work_calendar
        self.operations = [free_day.FreeDayOperation(work_calendar),
                           schedule.ScheduleOperation(work_calendar.continuous_schedule),
                           schedule.ScheduleOperation(work_calendar.short_schedule),
                           usual_day.UsualDayOperation(work_calendar)]
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


def create_work_day_calculator(work_calendar: WorkCalendar):
    return WorkDayCalculator(work_calendar)
