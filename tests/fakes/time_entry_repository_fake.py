import datetime

from schedule_calculator.time.repository.time_entry_repository import TimeEntryRepository


class TimeEntryRepositoryFake(TimeEntryRepository):

    def __init__(self, temp_folder: str):
        super().__init__(temp_folder)
        self.saved_entry = None

    def set_saved_entry(self, time_delta: datetime.datetime):
        self.saved_entry = time_delta

    def get_time_entry(self) -> datetime.datetime:
        if self.saved_entry:
            return self.saved_entry
        return super().get_time_entry()
