from datetime import timedelta

from schedule_calculator.time.assemblers.time_formatter import TimeFormatter


class Presenter:

    def __init__(self):
        self.time_formatter = TimeFormatter()
        self.zero_time_vector = timedelta(hours=0)

    def present_workday(self, worked_hours: timedelta, expected_hours: timedelta):
        worked_hours = max(worked_hours, self.zero_time_vector)
        print(
            f"You have worked {self.time_formatter.get_str_from_delta(worked_hours)}. "
            f"Today you have to work {self.time_formatter.get_str_from_delta(expected_hours)}.")

    def present_extra_hours(self, extra_hours: timedelta):
        print(
            f"You already have completed your workday. You have worked "
            f"{self.time_formatter.get_str_from_delta(extra_hours)} extra hours.")
