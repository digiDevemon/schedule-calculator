from schedule_calculator.clock import Clock
from schedule_calculator.time_entry_repository import TimeEntryRepository


class ScheduleJournal:

    def __init__(self, time_entry_repository: TimeEntryRepository = TimeEntryRepository(), clock: Clock = Clock()):
        self.time_entry_repository = time_entry_repository
        self.clock = clock

    def init(self):
        current_hour = self.clock.get_current_hour()
        self.time_entry_repository.save_time_entry(current_hour)

    def check(self):
        pass
