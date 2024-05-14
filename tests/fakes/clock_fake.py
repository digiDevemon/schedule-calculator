from schedule_calculator.clock import Clock


class ClockFake:

    def __init__(self):
        self.original_clock = Clock()
        self.today_day = None

    def set_today_day(self, today_day: str):
        self.today_day = today_day

    def get_today_day(self):
        if not self.today_day:
            return self.original_clock.get_today_day()

        return self.today_day
