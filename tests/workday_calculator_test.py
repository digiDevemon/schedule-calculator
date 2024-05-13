from datetime import datetime, timedelta
from unittest.mock import patch

from pytest import fixture

from schedule_calculator.workday_calculator import WorkDayCalculator

__STANDARD_DELTA = timedelta(hours=8, minutes=15)
__SHORT_DELTA = timedelta(hours=7)
__LAUNCH_DELTA = timedelta(hours=0, minutes=45)
__SHORT_DAY = 'Friday'

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
                                            __END_HOUR) is not None


def it_should_return_the_expected_time_when_calculates_worked_time():
    assert __get_workday_calculator().calculate_worked_time(__START_HOUR,
                                            __END_HOUR)[0] == __EXPECTED_WORDED_HOURS


def it_should_return_the_expected_time_when_is_friday_when_calculates_worked_time(_datetime_friday):
    assert __get_workday_calculator().calculate_worked_time(__START_HOUR,
                                            __END_HOUR)[0] == __EXPECTED_WORKED_HOURS_ON_FRIDAY


def it_should_return_the_expected_standard_delta_hours_when_calculates_worked_time():
    assert __get_workday_calculator().calculate_worked_time(__START_HOUR,
                                            __END_HOUR)[1] == __EXPECTED_STANDARD_DELTA_HOURS


def it_should_return_the_expected_short_delta_hours_when_calculates_worked_time(_datetime_friday):
    assert __get_workday_calculator().calculate_worked_time(__START_HOUR,
                                            __END_HOUR)[1] == __EXPECTED_SHORT_DELTA_HOURS


def it_should_not_return_none_when_calculates_extra_time():
    assert __get_workday_calculator().calculate_extra_time_today(__START_HOUR,
                                                 __END_HOUR) is not None


def it_should_return_the_expected_result_when_calculates_extra_time():
    assert __get_workday_calculator().calculate_extra_time_today(__START_HOUR,
                                                 __END_HOUR)[0] == __EXPECTED_ZERO_DELTA_HOURS


def it_should_return_the_expected_result_when_calculates_extra_time_on_friday(_datetime_friday):
    assert __get_workday_calculator().calculate_extra_time_today(__START_HOUR,
                                                 __END_HOUR_FRIDAY)[
               0] == __EXPECTED_ZERO_DELTA_HOURS


def __get_workday_calculator():
    return WorkDayCalculator(__STANDARD_DELTA, __SHORT_DELTA, __LAUNCH_DELTA, __SHORT_DAY)


@fixture()
def _datetime_friday():
    with patch('datetime.date') as date_mock:
        date_mock.today.return_value = __FRIDAY_DAY
        yield
