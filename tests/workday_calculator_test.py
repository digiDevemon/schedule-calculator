from datetime import datetime, timedelta

from pytest import fixture
from unittest.mock import patch
from schedule_calculator.workday_calculator import WorkDayCalculator

__CONFIG = {'schedule':
    {
        'standard': '8:15',
        'short': '7:00',
        'launch': '0:45',
        'short_day': 'Friday'
    }
}
__FORMATTER = "%H:%M"

__START_HOUR = datetime(2024, 5, 2, 8)
__END_HOUR = datetime(2024, 5, 2, 17)
__END_HOUR_FRIDAY = datetime(2024, 5, 2, 15)
__FRIDAY_DAY = datetime(2024, 5, 3)

__EXPECTED_SHORT_DELTA_HOURS = timedelta(hours=7)
__EXPECTED_ZERO_DELTA_HOURS = timedelta(hours=0)
__EXPECTED_STANDARD_DELTA_HOURS = timedelta(hours=8, minutes=15)
__EXPECTED_WORDED_HOURS = timedelta(hours=8, minutes=15)
__EXPECTED_WORKED_HOURS_ON_FRIDAY = timedelta(hours=9)


def it_should_not_return_none_when_calculates_worked_time():
    calculator = WorkDayCalculator(__CONFIG)
    assert calculator.calculate_worked_time(__START_HOUR.strftime(__FORMATTER),
                                            __END_HOUR.strftime(__FORMATTER)) is not None


def it_should_return_the_expected_time_when_calculates_worked_time():
    calculator = WorkDayCalculator(__CONFIG)
    assert calculator.calculate_worked_time(__START_HOUR.strftime(__FORMATTER),
                                            __END_HOUR.strftime(__FORMATTER))[0] == __EXPECTED_WORDED_HOURS


def it_should_return_the_expected_time_when_is_friday_when_calculates_worked_time(_datetime_friday):
    calculator = WorkDayCalculator(__CONFIG)
    assert calculator.calculate_worked_time(__START_HOUR.strftime(__FORMATTER),
                                            __END_HOUR.strftime(__FORMATTER))[0] == __EXPECTED_WORKED_HOURS_ON_FRIDAY


def it_should_return_the_expected_standard_delta_hours_when_calculates_worked_time():
    calculator = WorkDayCalculator(__CONFIG)
    assert calculator.calculate_worked_time(__START_HOUR.strftime(__FORMATTER),
                                            __END_HOUR.strftime(__FORMATTER))[1] == __EXPECTED_STANDARD_DELTA_HOURS


def it_should_return_the_expected_short_delta_hours_when_calculates_worked_time(_datetime_friday):
    calculator = WorkDayCalculator(__CONFIG)
    assert calculator.calculate_worked_time(__START_HOUR.strftime(__FORMATTER),
                                            __END_HOUR.strftime(__FORMATTER))[1] == __EXPECTED_SHORT_DELTA_HOURS


def it_should_not_return_none_when_calculates_extra_time():
    calculator = WorkDayCalculator(__CONFIG)
    assert calculator.calculate_extra_time_today(__START_HOUR.strftime(__FORMATTER),
                                                 __END_HOUR.strftime(__FORMATTER)) is not None


def it_should_return_the_expected_result_when_calculates_extra_time():
    calculator = WorkDayCalculator(__CONFIG)
    assert calculator.calculate_extra_time_today(__START_HOUR.strftime(__FORMATTER),
                                                 __END_HOUR.strftime(__FORMATTER))[0] == __EXPECTED_ZERO_DELTA_HOURS


def it_should_return_the_expected_result_when_calculates_extra_time_on_friday(_datetime_friday):
    calculator = WorkDayCalculator(__CONFIG)
    assert calculator.calculate_extra_time_today(__START_HOUR.strftime(__FORMATTER),
                                                 __END_HOUR_FRIDAY.strftime(__FORMATTER))[
               0] == __EXPECTED_ZERO_DELTA_HOURS


@fixture()
def _datetime_friday():
    with patch('datetime.date') as date_mock:
        date_mock.today.return_value = __FRIDAY_DAY
        yield
