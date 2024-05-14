import datetime

from schedule_calculator.clock import Clock
from schedule_calculator.schedule import Schedule


class WorkDayCalculator:

    def __init__(self, schedule: Schedule, clock: Clock = Clock()):
        self.schedule = schedule
        self.clock = clock

    def calculate_worked_time(self, start_hour: datetime.timedelta,
                              end_hour: datetime.timedelta = datetime.datetime.now()) -> (
            tuple)[datetime.timedelta, datetime.timedelta]:

        worked_time = end_hour - start_hour

        if self.__is_today_short_schedule():
            return worked_time, self.schedule.short_time

        return worked_time - self.schedule.launch_time, self.schedule.standard_time

    def calculate_extra_time_today(self, start_hour: datetime.timedelta,
                                   end_hour: datetime.timedelta = datetime.datetime.now()) \
            -> tuple[datetime.timedelta, datetime.timedelta]:

        worked_time = end_hour - start_hour

        if self.__is_today_short_schedule():
            return worked_time - self.schedule.short_time, self.schedule.short_time

        return (worked_time - self.schedule.launch_time -
                self.schedule.standard_time, self.schedule.standard_time)

    def __is_today_short_schedule(self) -> bool:
        return self.clock.get_today_day() == self.schedule.short_day
