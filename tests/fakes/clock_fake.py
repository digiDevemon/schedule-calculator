import datetime

from schedule_calculator.clock import Clock


class ClockFake(Clock):

    def __init__(self):
        self.today_day = None
        self.current_hour = None

    def set_today_day(self, today_day: str):
        self.today_day = today_day

    def set_current_hour(self, current_hour: datetime.timedelta):
        self.current_hour = current_hour

    def get_today_day(self):
        if not self.today_day:
            return super().get_today_day()

        return self.today_day

    def get_current_hour(self) -> datetime.timedelta:
        if not self.current_hour:
            return super().get_current_hour()

        return self.current_hour
