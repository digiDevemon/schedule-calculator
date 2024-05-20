from datetime import timedelta

from pytest import fixture
import os
from schedule_calculator.time_entry_repository import TimeEntryRepository
from tests.fakes.clock_fake import ClockFake

__HOUR = timedelta(hours=8)
__CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))


def it_should_return_false_when_check_data_exists_but_it_does_not_exist(time_repository):
    assert time_repository.repository_contains_time() == False


def it_should_return_true_when_check_data_exists_and_it_exists(time_repository):
    time_repository.save_time_entry(__HOUR)
    assert time_repository.repository_contains_time() == True


def it_should_return_false_when_check_data_exists_and_it_exists_but_we_remove_it(time_repository):
    time_repository.save_time_entry(__HOUR)
    time_repository.remove_time_entry()
    assert time_repository.repository_contains_time() == False


def it_should_return_the_expected_time_hour(time_repository):
    time_repository.save_time_entry(__HOUR)
    assert time_repository.get_time_entry() == __HOUR


@fixture
def time_repository():
    time_repository = TimeEntryRepository(temp_folder=__CURRENT_PATH)
    yield time_repository
    time_repository.remove_time_entry()


@fixture
def clock():
    clock = ClockFake()
    clock.set_current_hour(__HOUR)
    yield clock
