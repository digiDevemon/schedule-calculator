from typing import Optional

from schedule_calculator.time.assemblers.time_formatter import TimeFormatter
from schedule_calculator.time.date_period import DatePeriod
from schedule_calculator.time.schedule import Schedule


class ScheduleAssembler:
    def __init__(self):
        self.time_formatter = TimeFormatter()

    def get_schedule_from_config(self, configuration: Optional[dict]):
        if not configuration:
            return None

        schedule = Schedule(work_time=self.time_formatter.get_delta_from_str(configuration["work_time"]))

        if configuration.get("period"):
            schedule.period = DatePeriod(self.time_formatter.get_date_from_str(configuration["period"]["start"]),
                                         self.time_formatter.get_date_from_str(configuration["period"]["end"]))
        if configuration.get("days"):
            schedule.days = configuration["days"]

        return schedule
