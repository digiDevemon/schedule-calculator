from datetime import timedelta

from pytest import fixture

from schedule_calculator.time.assemblers.workday_assembler import WorkDayAssembler
from tests.fakes.clock_fake import ClockFake


def it_should_not_return_none(clock):
    workday_assembler = WorkDayAssembler(clock)
    start_date = clock.get_current_time()
    end_date = start_date + timedelta(hours=1)

    assert workday_assembler.get_workday(start_date, end_date) is not None, "It should not return none"


def it_should_return_the_expected_workday_object_with_expected_start_date(clock):
    workday_assembler = WorkDayAssembler(clock)
    start_date = clock.get_current_time()
    end_date = start_date + timedelta(hours=1)

    workday = workday_assembler.get_workday(start_date, end_date)

    assert workday.start == start_date, f"It should return a workday with the expected start {workday}"


def it_should_return_the_expected_workday_object_with_expected_end_date(clock):
    workday_assembler = WorkDayAssembler(clock)
    start_date = clock.get_current_time()
    end_date = start_date + timedelta(hours=1)

    workday = workday_assembler.get_workday(start_date, end_date)

    assert workday.end == end_date, f"It should return a workday with the expected end date {end_date}"


def it_should_return_the_expected_workday_object_with_expected_end_date_when_end_date_is_not_specified(clock):
    workday_assembler = WorkDayAssembler(clock)
    start_date = clock.get_current_time()
    end_date = start_date + timedelta(hours=1)
    clock.set_current_time(end_date)

    workday = workday_assembler.get_workday(start_date)

    assert workday.end == end_date, f"It should return a workday with the expected end date {end_date}"


@fixture
def clock():
    return ClockFake()
