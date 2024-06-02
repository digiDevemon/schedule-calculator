import datetime

from schedule_calculator.time.schedule import Schedule
from datetime import timedelta


class WorkDayCalculator:

    def __init__(self, schedule: Schedule):
        self.schedule = schedule
        self.zero_time = timedelta(hours=0)

    def calculate_worked_time(self, today_day: str, start_hour: datetime.timedelta, end_hour=datetime.timedelta) -> (
            tuple)[datetime.timedelta, datetime.timedelta]:

        if self.__is_weekend(today_day):
            return self.__get_worked_time(end_hour, start_hour),  self.zero_time

        if self.__is_short_schedule(today_day):
            return self.__get_worked_time(end_hour, start_hour), self.schedule.short_time

        return self.__get_worked_time(end_hour, start_hour) - self.schedule.launch_time, self.schedule.standard_time

    def calculate_extra_time_today(self, today_day: str, start_hour: datetime.timedelta, end_hour=datetime.timedelta) \
            -> tuple[datetime.timedelta, datetime.timedelta]:

        if self.__is_short_schedule(today_day):
            return self.__get_worked_time(end_hour, start_hour) - self.schedule.short_time, self.schedule.short_time

        return (self.__get_worked_time(end_hour, start_hour) - self.schedule.launch_time -
                self.schedule.standard_time, self.schedule.standard_time)

    @staticmethod
    def __get_worked_time(end_hour, start_hour):
        return end_hour - start_hour

    def __is_short_schedule(self, today_day: str) -> bool:
        return today_day in self.schedule.short_days

    def __is_weekend(self, today_day: str) -> bool:
        return today_day in self.schedule.weekend_days


def create_work_day_calculator(schedule: Schedule):
    return WorkDayCalculator(schedule)
