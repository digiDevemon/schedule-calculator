from datetime import datetime, timedelta

from pytest import fixture

from schedule_calculator.schedule import Schedule
from schedule_calculator.workday_calculator import WorkDayCalculator, create_work_day_calculator
from tests.fakes.clock_fake import ClockFake

__STANDARD_DELTA = timedelta(hours=8, minutes=15)
__SHORT_DELTA = timedelta(hours=7)
__LAUNCH_DELTA = timedelta(hours=0, minutes=45)
__SHORT_DAY = 'Friday'
__SCHEDULE = Schedule(__STANDARD_DELTA, __SHORT_DELTA, __LAUNCH_DELTA, __SHORT_DAY)

__START_HOUR = timedelta(hours=8)
__END_HOUR = timedelta(hours=17)
__END_HOUR_FRIDAY = timedelta(hours=15)

__FRIDAY_DAY = datetime(2024, 5, 3)

__EXPECTED_SHORT_DELTA_HOURS = timedelta(hours=7)
__EXPECTED_ZERO_DELTA_HOURS = timedelta(hours=0)
__EXPECTED_STANDARD_DELTA_HOURS = timedelta(hours=8, minutes=15)
__EXPECTED_WORDED_HOURS = timedelta(hours=8, minutes=15)
__EXPECTED_WORKED_HOURS_ON_FRIDAY = timedelta(hours=9)


def it_should_not_return_none_when_calculates_worked_time():
    assert __get_workday_calculator().calculate_worked_time(__START_HOUR,
                                                            __END_HOUR) is not None, "It should return something"


def it_should_return_the_expected_time_when_calculates_worked_time():
    assert __get_workday_calculator().calculate_worked_time(__START_HOUR,
                                                            __END_HOUR)[0] == __EXPECTED_WORDED_HOURS, \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected {__EXPECTED_WORDED_HOURS} on a regular day")


def it_should_return_the_expected_time_when_is_friday_when_calculates_worked_time(_fake_clock):
    _fake_clock.set_today_day(__SHORT_DAY)
    assert (__get_workday_calculator(_fake_clock).calculate_worked_time(__START_HOUR,
                                                                        __END_HOUR)[0]
            == __EXPECTED_WORKED_HOURS_ON_FRIDAY), \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected {__EXPECTED_WORKED_HOURS_ON_FRIDAY} on a short day")


def it_should_return_the_expected_standard_delta_hours_when_calculates_worked_time():
    assert (__get_workday_calculator().calculate_worked_time(__START_HOUR,
                                                             __END_HOUR)[1]
            == __EXPECTED_STANDARD_DELTA_HOURS), \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected delta {__EXPECTED_STANDARD_DELTA_HOURS} on a regular day")


def it_should_return_the_expected_standard_delta_hours_when_calculates_worked_time_but_end_hour_is_not_defined(
        _fake_clock):
    _fake_clock.set_current_hour(__END_HOUR)
    assert (__get_workday_calculator(_fake_clock).calculate_worked_time(__START_HOUR)[1]
            == __EXPECTED_STANDARD_DELTA_HOURS), \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected delta {__EXPECTED_STANDARD_DELTA_HOURS} on a regular day")


def it_should_return_the_expected_short_delta_hours_when_calculates_worked_time(_fake_clock):
    _fake_clock.set_today_day(__SHORT_DAY)
    assert (__get_workday_calculator(_fake_clock).calculate_worked_time(__START_HOUR,
                                                                        __END_HOUR)[1]
            == __EXPECTED_SHORT_DELTA_HOURS), \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected delta {__EXPECTED_SHORT_DELTA_HOURS} on a short day")


def it_should_not_return_none_when_calculates_extra_time():
    assert __get_workday_calculator().calculate_extra_time_today(__START_HOUR,
                                                                 __END_HOUR) is not None, "It should return something"


def it_should_return_the_expected_result_when_calculates_extra_time():
    assert (__get_workday_calculator().calculate_extra_time_today(__START_HOUR,
                                                                  __END_HOUR)[0]
            == __EXPECTED_ZERO_DELTA_HOURS), \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected delta {__EXPECTED_ZERO_DELTA_HOURS} on a regular day for extra time")


def it_should_return_the_expected_result_when_calculates_extra_time_on_friday(_fake_clock):
    _fake_clock.set_today_day(__SHORT_DAY)
    assert (__get_workday_calculator(_fake_clock).calculate_extra_time_today(__START_HOUR,
                                                                             __END_HOUR_FRIDAY)[0]
            == __EXPECTED_ZERO_DELTA_HOURS), \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected delta {__EXPECTED_ZERO_DELTA_HOURS} on a short day for extra time")


def it_should_return_the_expected_result_when_calculates_extra_time_on_friday_without_end_hour(_fake_clock):
    _fake_clock.set_today_day(__SHORT_DAY)
    _fake_clock.set_current_hour(__END_HOUR_FRIDAY)
    assert (__get_workday_calculator(_fake_clock).calculate_extra_time_today(__START_HOUR)[0]
            == __EXPECTED_ZERO_DELTA_HOURS), \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected delta {__EXPECTED_ZERO_DELTA_HOURS} on a short day for extra time")


def __get_workday_calculator(fake_clock=None):
    if not fake_clock:
        return create_work_day_calculator(__SCHEDULE)
    return WorkDayCalculator(__SCHEDULE, fake_clock)


@fixture
def _fake_clock():
    yield ClockFake()
