from schedule_calculator.time.assemblers.free_days_calendar_assembler import FreeDaysCalendarAssembler
from schedule_calculator.time.assemblers.schedule_assembler import ScheduleAssembler
from schedule_calculator.time.assemblers.time_formatter import TimeFormatter
from schedule_calculator.time.clock import Clock
from schedule_calculator.time.work_calendar import WorkCalendar


class WorkCalendarAssembler:

    def __init__(self, time_formatter: TimeFormatter, clock: Clock):
        self.time_formatter = time_formatter
        self.clock = clock
        self.holiday_calendar_assembler = FreeDaysCalendarAssembler()
        self.schedule_assembler = ScheduleAssembler()

    def get_work_calendar(self, configuration: dict) -> WorkCalendar:
        time_formatter = self.time_formatter

        current_date = self.clock.get_current_date()

        delta_schedule_standard = time_formatter.get_delta_from_str(configuration["standard"])
        delta_schedule_short = time_formatter.get_delta_from_str(configuration["short"])
        delta_launch = time_formatter.get_delta_from_str(configuration["launch"])

        short_days = configuration["short_days"]

        continuous_schedule = self.schedule_assembler.get_schedule_from_config(configuration.get("continuous_schedule"))

        free_days = self.holiday_calendar_assembler.get_calendar_from_str(configuration["location"],
                                                                          current_date.year)

        return WorkCalendar(current_date, delta_schedule_standard, delta_schedule_short, delta_launch,
                            short_days, free_days, continuous_schedule)
