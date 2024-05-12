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
__EXPECTED_WORDED_HOURS = timedelta(hours=8, minutes=15)
__EXPECTED_WORKED_HOURS_ON_FRIDAY = timedelta(hours=9)
__FRIDAY_DAY = datetime(2024, 5, 3)


def it_should_not_return_none():
    calculator = WorkDayCalculator(__CONFIG)
    assert calculator.calculate_time_today(__START_HOUR.strftime(__FORMATTER), __END_HOUR.strftime(__FORMATTER))


def it_should_return_the_expected_time():
    calculator = WorkDayCalculator(__CONFIG)
    assert calculator.calculate_time_today(__START_HOUR.strftime(__FORMATTER),
                                           __END_HOUR.strftime(__FORMATTER)) == __EXPECTED_WORDED_HOURS


def it_should_return_the_expected_time_when_is_friday(_datetime_friday):
    calculator = WorkDayCalculator(__CONFIG)
    print(calculator.calculate_time_today(__START_HOUR.strftime(__FORMATTER),
                                           __END_HOUR.strftime(__FORMATTER)))
    print(__EXPECTED_WORKED_HOURS_ON_FRIDAY)
    assert calculator.calculate_time_today(__START_HOUR.strftime(__FORMATTER),
                                           __END_HOUR.strftime(__FORMATTER)) == __EXPECTED_WORKED_HOURS_ON_FRIDAY


@fixture()
def _datetime_friday():
    with patch('datetime.date') as date_mock:
        date_mock.today.return_value = __FRIDAY_DAY
        yield
