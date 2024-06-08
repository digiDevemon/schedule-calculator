from datetime import timedelta, datetime

import pytest

from schedule_calculator.calculus.operations.short_day import ShortDayOperation
from schedule_calculator.time.schedule import Schedule
from schedule_calculator.time.workday import Workday

__STANDARD_DELTA = timedelta(hours=8, minutes=15)
__SHORT_DELTA = timedelta(hours=7)
__LAUNCH_DELTA = timedelta(hours=0, minutes=45)
__SHORT_DAY = 'Friday'
__WEEKEND_DAYS = ['Saturday', 'Sunday']
__SCHEDULE = Schedule(__STANDARD_DELTA, __SHORT_DELTA, __LAUNCH_DELTA, [__SHORT_DAY], __WEEKEND_DAYS)

__START_HOUR = datetime(year=1997, month=7, day=7, hour=8, minute=0, second=0)
__END_HOUR = datetime(year=1997, month=7, day=7, hour=17, minute=0, second=0)
__WORKDAY = Workday(__START_HOUR, __END_HOUR)

__START_HOUR = datetime(year=1997, month=7, day=11, hour=8, minute=0, second=0)
__END_HOUR = datetime(year=1997, month=7, day=11, hour=15, minute=0, second=0)
__SHORT_WORKDAY = Workday(__START_HOUR, __END_HOUR)


@pytest.mark.parametrize("day,expected_result", [
    (__SHORT_WORKDAY, True),
    (__WORKDAY, False)])
def it_should_return_the_expected_response_fulfilling_the_schedule(day, expected_result):
    operation = ShortDayOperation(__SCHEDULE)
    assert operation.fulfill(day) == expected_result, f"It should return {expected_result} for {day}"


def it_should_return_the_expected_calculation():
    expected_result = timedelta(hours=7)
    operation = ShortDayOperation(__SCHEDULE)

    assert operation.calculate(__SHORT_WORKDAY)[0] == expected_result, \
        f"It should return {expected_result} as calculation result"


def it_should_return_the_expected_delta_calculation():
    operation = ShortDayOperation(__SCHEDULE)

    assert operation.calculate(__SHORT_WORKDAY)[1] == __SHORT_DELTA, \
        f"It should return {__SHORT_DELTA} as expected calculation result"