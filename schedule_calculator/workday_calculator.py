import datetime

from schedule_calculator.clock import Clock
from schedule_calculator.schedule import Schedule


class WorkDayCalculator:

    def __init__(self, schedule: Schedule, clock: Clock):
        self.schedule = schedule
        self.clock = clock

    def calculate_worked_time(self, start_hour: datetime.timedelta,
                              end_hour=None) -> (
            tuple)[datetime.timedelta, datetime.timedelta]:

        if self.__is_today_short_schedule():
            return self.__get_worked_time(end_hour, start_hour), self.schedule.short_time

        return self.__get_worked_time(end_hour, start_hour) - self.schedule.launch_time, self.schedule.standard_time

    def calculate_extra_time_today(self, start_hour: datetime.timedelta,
                                   end_hour=None) \
            -> tuple[datetime.timedelta, datetime.timedelta]:

        if self.__is_today_short_schedule():
            return self.__get_worked_time(end_hour, start_hour) - self.schedule.short_time, self.schedule.short_time

        return (self.__get_worked_time(end_hour, start_hour) - self.schedule.launch_time -
                self.schedule.standard_time, self.schedule.standard_time)

    def __get_worked_time(self, end_hour, start_hour):
        if not end_hour:
            end_hour = self.clock.get_current_hour()

        return end_hour - start_hour

    def __is_today_short_schedule(self) -> bool:
        return self.clock.get_today_day() == self.schedule.short_day


def create_work_day_calculator(schedule: Schedule):
    clock = Clock()
    return WorkDayCalculator(schedule, clock)
