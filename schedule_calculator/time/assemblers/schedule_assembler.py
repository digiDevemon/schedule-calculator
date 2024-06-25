from schedule_calculator.time.assemblers.time_formatter import TimeFormatter
from schedule_calculator.time.schedule import Schedule


class ScheduleAssembler:

    def __init__(self, time_formatter: TimeFormatter):
        self.time_formatter = time_formatter

    def get_schedule(self, configuration: dict) -> Schedule:
        time_formatter = self.time_formatter

        delta_schedule_standard = time_formatter.get_delta_from_str(configuration["standard"])
        delta_schedule_short = time_formatter.get_delta_from_str(configuration["short"])
        delta_launch = time_formatter.get_delta_from_str(configuration["launch"])
        delta_continuous = time_formatter.get_delta_from_str(configuration["continuous"])

        short_days = configuration["short_days"]
        weekend_days = configuration["weekend_days"]
        continuous_period = self.__get_continuous_period(configuration)
        return Schedule(delta_schedule_standard, delta_schedule_short, delta_launch, delta_continuous,
                        short_days, weekend_days, continuous_period)

    def __get_continuous_period(self, configuration: dict):
        return {
            "start": self.time_formatter.get_date_from_str(configuration["continuous_period"]["start"]),
            "end": self.time_formatter.get_date_from_str(configuration["continuous_period"]["end"])
        }
