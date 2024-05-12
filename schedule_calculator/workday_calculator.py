import datetime


class WorkDayCalculator:

    def __init__(self, configuration):
        self.hour_formatter = "%H:%M"
        self.delta_schedule_standard = self.__get_delta_schedule_standard(configuration)
        self.delta_schedule_short = self.__get_delta_schedule_short(configuration)
        self.delta_launch = self.__get_delta_launch(configuration)
        self.short_day = configuration["schedule"]["short_day"]

    def calculate_time_today(self, start_hour: str, end_hour: str) -> datetime.timedelta:
        if self.__is_today_short_schedule():
            return self.__get_delta_from_string(end_hour) - self.__get_delta_from_string(start_hour)
        return (self.__get_delta_from_string(end_hour) - self.__get_delta_from_string(start_hour)
                - self.delta_launch)

    def calculate_extra_time_today(self):
        pass

    def __is_today_short_schedule(self) -> bool:
        return datetime.date.today().strftime(("%A")) == self.short_day

    def __get_delta_schedule_standard(self, configuration: dict) -> datetime.timedelta:
        return self.__get_delta_from_string(configuration["schedule"]["standard"])

    def __get_delta_schedule_short(self, configuration: dict) -> datetime.timedelta:
        return self.__get_delta_from_string(configuration["schedule"]["short"])

    def __get_delta_launch(self, configuration: dict) -> datetime.timedelta:
        return self.__get_delta_from_string(configuration["schedule"]["launch"])

    def __get_delta_from_string(self, time: str) -> datetime.timedelta:
        time_parsed = datetime.datetime.strptime(time, self.hour_formatter)
        return datetime.timedelta(hours=time_parsed.hour, minutes=time_parsed.minute)
