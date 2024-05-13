from schedule_calculator.workday_calculator import WorkDayCalculator


class ScheduleJournal:

    def __init__(self, configuration):
        self.workday_calculator = WorkDayCalculator(configuration)

    def init(self):
        pass

    def check(self):
        pass
