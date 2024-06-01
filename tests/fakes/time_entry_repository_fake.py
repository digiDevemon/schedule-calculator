import datetime

from schedule_calculator.assemblers.time_assembler import TimeFormatter
from schedule_calculator.time_entry_repository import TimeEntryRepository


class TimeEntryRepositoryFake(TimeEntryRepository):

    def __init__(self, temp_folder: str):
        time_formatter = TimeFormatter()
        super().__init__(time_formatter, temp_folder)
        self.saved_entry = None

    def set_saved_entry(self, time_delta: datetime.timedelta):
        self.saved_entry = time_delta

    def get_time_entry(self) -> datetime.timedelta:
        if self.saved_entry:
            return self.saved_entry
        return super().get_time_entry()