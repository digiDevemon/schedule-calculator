import os

from pytest import fixture

from schedule_calculator.assemblers.time_assembler import TimeFormatter
from schedule_calculator.schedule_journal import create_schedule_journal_with_repository
from schedule_calculator.time_entry_repository import TimeEntryRepository

__CONFIG = {
    "schedule": {
        "standard": "08:15",
        "short": "07:00",
        "launch": "00:45",
        "short_day": "Friday"
    }
}
__CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))


def it_should_create_time_file_when_init_journal(temporal_repository):
    schedule_journal = create_schedule_journal_with_repository(__CONFIG, temporal_repository)
    schedule_journal.init()
    assert temporal_repository.repository_contains_time(), "It should saved current time"


@fixture
def temporal_repository(time_formatter):
    temporal_repository = TimeEntryRepository(time_formatter, __CURRENT_PATH)
    yield temporal_repository
    temporal_repository.remove_time_entry()


@fixture
def time_formatter():
    yield TimeFormatter()
