import datetime
from datetime import timedelta

from schedule_calculator.time.schedule import Schedule
from schedule_calculator.time.workday import Workday
from schedule_calculator.calculus.operations import usual_day, short_day, weekend_day
from schedule_calculator.calculus.exceptions.unknown_operation_day import UnknownOperationDay


class WorkDayCalculator:

    def __init__(self, schedule: Schedule):
        self.schedule = schedule
        self.operations = [usual_day.UsualDayOperation(schedule),
                           short_day.ShortDayOperation(schedule),
                           weekend_day.WeekendDayOperation(schedule)]
        self.zero_time = timedelta(hours=0)

    def calculate_worked_time(self, today_day: str, start_hour: datetime.datetime, end_hour: datetime.datetime) -> (
            tuple)[datetime.timedelta, datetime.timedelta]:

        for operation in self.operations:
            if operation.fulfill(Workday(start_hour, end_hour)):
                return operation.calculate(Workday(start_hour, end_hour))

        raise UnknownOperationDay()

    def calculate_extra_time_today(self, today_day: str, start_hour: datetime.datetime, end_hour: datetime.datetime) \
            -> tuple[datetime.timedelta, datetime.timedelta]:

        if self.__is_weekend(today_day):
            return self.__get_worked_time(end_hour, start_hour), self.zero_time

        if self.__is_short_schedule(today_day):
            return self.__get_worked_time(end_hour, start_hour) - self.schedule.short_time, self.schedule.short_time

        return (self.__get_worked_time(end_hour, start_hour) - self.schedule.launch_time -
                self.schedule.standard_time, self.schedule.standard_time)

    @staticmethod
    def __get_worked_time(end_hour: datetime.datetime, start_hour: datetime.datetime):
        return end_hour - start_hour

    def __is_short_schedule(self, today_day: str) -> bool:
        return today_day in self.schedule.short_days

    def __is_weekend(self, today_day: str) -> bool:
        return today_day in self.schedule.weekend_days


def create_work_day_calculator(schedule: Schedule):
    return WorkDayCalculator(schedule)
