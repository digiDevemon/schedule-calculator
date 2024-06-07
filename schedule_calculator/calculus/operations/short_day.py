import datetime

from schedule_calculator.calculus.operations.interface import Operation
from schedule_calculator.time.schedule import Schedule


class ShortDayOperation(Operation):

    def calculate(self) -> datetime.timedelta:
        return datetime.timedelta(hours=1)

    def fulfill(self) -> bool:
        return True

    def __init__(self, schedule: Schedule):
        self.schedule = schedule
