import io
import os
from contextlib import redirect_stdout
from datetime import datetime

from pytest import fixture

from schedule_calculator.schedule_journal import create_schedule_journal_for_testing
from tests.fakes.clock_fake import ClockFake
from tests.fakes.presenter_fake import PresenterFake
from tests.fakes.time_entry_repository_fake import TimeEntryRepositoryFake

__CONFIG = {
    "schedule": {
        "standard": "08:15",
        "short": "07:00",
        "launch": "00:45",
        "short_days": ['Friday'],
        "weekend_days": ['Saturday', 'Sunday'],
    }
}
__CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
__EXTRA_HOURS_MESSAGE = "just a message for extra hours"
__WORKDAY_HOURS_MESSAGE = "just a message for workday hours"


def it_should_create_time_file_when_init_journal(temporal_repository, clock, presenter):
    schedule_journal = create_schedule_journal_for_testing(__CONFIG, temporal_repository, clock, presenter)
    schedule_journal.init()
    assert temporal_repository.repository_contains_time(), "It should save current time"


def it_should_print_the_expected_message(temporal_repository, clock, presenter):
    temporal_repository.set_saved_entry(datetime(year=1991, month=7, day=8, hour=8, minute=0, second=0))
    clock.set_current_time(datetime(year=1991, month=7, day=8, hour=17, minute=0, second=0))
    clock.set_today_day("Monday")
    schedule_journal = create_schedule_journal_for_testing(__CONFIG, temporal_repository, clock, presenter)

    output = io.StringIO()
    with redirect_stdout(output):
        schedule_journal.check()
    out_value = output.getvalue().replace("\n", "")

    assert out_value == __WORKDAY_HOURS_MESSAGE


def it_should_print_the_expected_message_when_the_time_vector_is_not_positive(temporal_repository, clock, presenter):
    temporal_repository.set_saved_entry(datetime(year=1991, month=7, day=8, hour=8, minute=0, second=0))
    clock.set_current_time(datetime(year=1991, month=7, day=8, hour=21, minute=15, second=0))
    clock.set_today_day("Monday")
    schedule_journal = create_schedule_journal_for_testing(__CONFIG, temporal_repository, clock, presenter)

    output = io.StringIO()
    with redirect_stdout(output):
        schedule_journal.check()
    out_value = output.getvalue().replace("\n", "")

    assert out_value == __EXTRA_HOURS_MESSAGE


@fixture
def temporal_repository():
    temporal_repository = TimeEntryRepositoryFake(__CURRENT_PATH)
    yield temporal_repository
    temporal_repository.remove_time_entry()


@fixture
def clock():
    return ClockFake()


@fixture
def presenter():
    presenter = PresenterFake()
    presenter.set_default_message_workday(__WORKDAY_HOURS_MESSAGE)
    presenter.set_default_message_extra_hours(__EXTRA_HOURS_MESSAGE)
    return presenter
