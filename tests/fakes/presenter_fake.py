import datetime

from schedule_calculator.presenter import Presenter
from schedule_calculator.time.workday import Workday


class PresenterFake(Presenter):

    def __init__(self):
        super().__init__()
        self.default_message_workday = None
        self.default_message_extra_hours = None

    def present_workday(self, workday: datetime.timedelta, expected_hours: datetime.timedelta):
        if self.default_message_workday:
            print(self.default_message_workday)
            return
        super().present_workday(workday, expected_hours)

    def present_extra_hours(self, extra_hours: datetime.timedelta):
        if self.default_message_extra_hours:
            print(self.default_message_extra_hours)
            return
        super().present_extra_hours(extra_hours)

    def set_default_message_workday(self, message: str):
        self.default_message_workday = message

    def set_default_message_extra_hours(self, message: str):
        self.default_message_extra_hours = message
