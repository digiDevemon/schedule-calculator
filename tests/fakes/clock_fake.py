import datetime

from schedule_calculator.time.clock import Clock


class ClockFake(Clock):

    def __init__(self):
        self.today_day = None
        self.current_hour = None
        self.current_date = None

    def set_today_day(self, today_day: str):
        self.today_day = today_day

    def set_current_time(self, current_hour: datetime.datetime):
        self.current_hour = current_hour

    def set_current_date(self, current_date: datetime.date):
        self.current_date = current_date

    def get_today_day(self):
        if not self.today_day:
            return super().get_today_day()

        return self.today_day

    def get_current_time(self) -> datetime.datetime:
        if not self.current_hour:
            return super().get_current_time()

        return self.current_hour

    def get_today_date(self):
        if not self.current_date:
            return super().get_today_day()

        return self.current_date
