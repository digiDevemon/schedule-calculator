from typing import Optional

from schedule_calculator.time.assemblers.free_days_calendar_assembler import FreeDaysCalendarAssembler
from schedule_calculator.time.assemblers.time_formatter import TimeFormatter
from schedule_calculator.time.clock import Clock
from schedule_calculator.time.schedule import Schedule
from schedule_calculator.time.workcalendar import WorkCalendar


class WorkCalendarAssembler:

    def __init__(self, time_formatter: TimeFormatter, clock: Clock):
        self.time_formatter = time_formatter
        self.clock = clock
        self.holiday_calendar_assembler = FreeDaysCalendarAssembler()

    def get_schedule(self, configuration: dict) -> WorkCalendar:
        time_formatter = self.time_formatter

        current_date = self.clock.get_current_date()

        delta_schedule_standard = time_formatter.get_delta_from_str(configuration["standard"])
        delta_schedule_short = time_formatter.get_delta_from_str(configuration["short"])
        delta_launch = time_formatter.get_delta_from_str(configuration["launch"])

        short_days = configuration["short_days"]

        continuous_schedule = self.__get_continuous_schedule(configuration)
        free_days = self.holiday_calendar_assembler.get_calendar_from_str(configuration["location"],
                                                                          current_date.year)

        return WorkCalendar(current_date, delta_schedule_standard, delta_schedule_short, delta_launch,
                            short_days, free_days, continuous_schedule)

    def __get_continuous_schedule(self, configuration: dict) -> Optional[Schedule]:
        continuous_schedule = configuration.get("continuous_schedule")
        if not continuous_schedule:
            return None
        continuous_period = {
            "start": self.time_formatter.get_date_from_str(continuous_schedule["period"]["start"]),
            "end": self.time_formatter.get_date_from_str(continuous_schedule["period"]["end"])
        }
        return Schedule(
            work_time=self.time_formatter.get_delta_from_str(continuous_schedule["work_time"]), period=continuous_period)
