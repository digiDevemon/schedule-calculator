from schedule_calculator.workday_calculator import WorkDayCalculator


class ScheduleJournal:
    HOUR_FORMATTER = "%H:%M"

    def __init__(self, configuration):
        self.workday_calculator = WorkDayCalculator(configuration)

    def fuu(self):
        pass

    def fee(self):
        pass
