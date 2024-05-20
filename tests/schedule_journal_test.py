from pytest import fixture

from schedule_calculator.assemblers.time_assembler import TimeFormatter
from schedule_calculator.schedule_journal import ScheduleJournal
from schedule_calculator.time_entry_repository import TimeEntryRepository

__CONFIG = {
    "schedule": {
        "standard": "8:15",
        "short": "7:00",
        "launch": "0:45",
        "short_day": "Friday"
    }
}


def it_should_create_time_file_when_init_journal(temporal_repository):
    schedule_journal = ScheduleJournal(__CONFIG)
    schedule_journal.init()
    assert temporal_repository.repository_contains_time()


@fixture
def temporal_repository(time_formatter):
    temporal_repository = TimeEntryRepository(time_formatter)
    yield temporal_repository
    temporal_repository.remove_time_entry()


@fixture
def time_formatter():
    yield TimeFormatter()
