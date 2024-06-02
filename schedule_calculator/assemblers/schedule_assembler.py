from schedule_calculator.assemblers.time_assembler import TimeFormatter
from schedule_calculator.schedule import Schedule


class ScheduleAssembler:

    def __init__(self, time_formatter: TimeFormatter):
        self.time_formatter = time_formatter

    def get_schedule(self, configuration: dict) -> Schedule:
        time_formatter = self.time_formatter

        delta_schedule_standard = time_formatter.get_delta_from_str(configuration["standard"])
        delta_schedule_short = time_formatter.get_delta_from_str(configuration["short"])
        delta_launch = time_formatter.get_delta_from_str(configuration["launch"])
        short_days = configuration["short_days"]
        weekend_days = configuration["weekend_days"]
        return Schedule(delta_schedule_standard, delta_schedule_short, delta_launch, short_days, weekend_days)
