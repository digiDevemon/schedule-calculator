from schedule_calculator.clock import Clock
import datetime


class ClockFake:

    def __init__(self):
        self.original_clock = Clock()
        self.today_day = None
        self.delta_now = None

    def set_today_day(self, today_day: str):
        self.today_day = today_day

    def set_delta_now(self, delta_now: datetime.timedelta):
        self.delta_now = delta_now

    def get_today_day(self) -> str:
        if not self.today_day:
            return self.original_clock.get_today_day()

        return self.today_day

    def get_delta_now(self) -> datetime.timedelta:
        if not self.delta_now:
            return self.original_clock.get_delta_now()

        return self.delta_now
