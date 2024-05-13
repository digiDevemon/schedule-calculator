import datetime


class WorkDayCalculator:
    HOUR_FORMATTER = "%H:%M"

    def __init__(self, schedule_standard: datetime.timedelta, schedule_short: datetime.timedelta,
                 delta_launch: datetime.timedelta, short_day: str):
        self.delta_schedule_standard = schedule_standard
        self.delta_schedule_short = schedule_short
        self.delta_launch = delta_launch
        self.short_day = short_day

    def calculate_worked_time(self, start_hour: datetime.timedelta,
                              end_hour: datetime.timedelta = datetime.datetime.now().strftime(HOUR_FORMATTER)) -> (
            tuple)[datetime.timedelta, datetime.timedelta]:

        worked_time = end_hour - start_hour

        if self.__is_today_short_schedule():
            return worked_time, self.delta_schedule_short

        return worked_time - self.delta_launch, self.delta_schedule_standard

    def calculate_extra_time_today(self, start_hour: datetime.timedelta,
                                   end_hour: datetime.timedelta = datetime.datetime
                                   .now()
                                   .strftime(HOUR_FORMATTER)) \
            -> tuple[datetime.timedelta, datetime.timedelta]:

        worked_time = end_hour - start_hour

        if self.__is_today_short_schedule():
            return worked_time - self.delta_schedule_short, self.delta_schedule_short

        return (worked_time - self.delta_launch -
                self.delta_schedule_standard, self.delta_schedule_standard)

    def __is_today_short_schedule(self) -> bool:
        return datetime.date.today().strftime("%A") == self.short_day
