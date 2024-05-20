from schedule_calculator.assemblers.time_assembler import TimeFormatter
from schedule_calculator.schedule import Schedule
from schedule_calculator.workday_calculator import WorkDayCalculator


class WorkDayAssembler:

    def __init__(self, time_formatter: TimeFormatter = TimeFormatter()):
        self.time_formatter = time_formatter

    def get_workday_from_configuration(self, configuration: dict) -> WorkDayCalculator:
        return WorkDayCalculator(self.__get_schedule(configuration))

    def __get_schedule(self, configuration: dict) -> Schedule:
        time_formatter = self.time_formatter

        delta_schedule_standard = time_formatter.get_delta_from_str(configuration["schedule"]["standard"])
        delta_schedule_short = time_formatter.get_delta_from_str(configuration["schedule"]["short"])
        delta_launch = time_formatter.get_delta_from_str(configuration["schedule"]["launch"])
        short_day = configuration["schedule"]["short_day"]
        return Schedule(delta_schedule_standard, delta_schedule_short, delta_launch, short_day)
