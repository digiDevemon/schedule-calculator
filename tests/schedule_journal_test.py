import os
from datetime import timedelta
from pathlib import Path

from pytest import fixture

from schedule_calculator.schedule_journal import ScheduleJournal
from schedule_calculator.time_entry_repository import TimeEntryRepository
from tests.fakes.clock_fake import ClockFake

__CONFIG = {
    "schedule": {
        "standard": "08:15",
        "short": "07:00",
        "launch": "00:45",
        "short_day": "Friday"
    }
}
__CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
__HOUR = timedelta(hours=8)
__EXPECTED_HOUR_STRING = "08:00"


def it_should_create_time_file_when_init_journal(temporal_repository, clock):
    schedule_journal = ScheduleJournal(__CONFIG, time_entry_repository=temporal_repository, clock=clock)
    schedule_journal.init()
    assert temporal_repository.repository_contains_time()


def it_should_set_current_hour_in_repository(temporal_repository, clock):
    schedule_journal = ScheduleJournal(__CONFIG, time_entry_repository=temporal_repository, clock=clock)
    schedule_journal.init()
    text = Path(os.path.join(__CURRENT_PATH, temporal_repository.get_temp_file_name())).read_text()
    assert text == __EXPECTED_HOUR_STRING


@fixture
def temporal_repository():
    temporal_repository = TimeEntryRepository(temp_folder=__CURRENT_PATH)
    yield temporal_repository
    temporal_repository.remove_time_entry()


@fixture
def clock():
    clock = ClockFake()
    clock.set_current_hour(__HOUR)
    yield clock
