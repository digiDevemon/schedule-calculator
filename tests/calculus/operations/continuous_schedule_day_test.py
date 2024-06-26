from datetime import timedelta, datetime, date

import pytest

from schedule_calculator.calculus.operations.continuous_schedule_day import ContinuousDayScheduleOperation
from schedule_calculator.time.schedule import Schedule
from schedule_calculator.time.workday import Workday

__STANDARD_DELTA = timedelta(hours=8, minutes=15)
__SHORT_DELTA = timedelta(hours=7)
__LAUNCH_DELTA = timedelta(hours=0, minutes=45)
__CONTINUOUS_DELTA = timedelta(hours=8, minutes=0)

__SHORT_DAY = 'Friday'
__WEEKEND_DAYS = ['Saturday', 'Sunday']

__CONTINUOUS_PERIOD_START = date(year=datetime.now().year, month=5, day=20)
__CONTINUOUS_PERIOD_END = date(year=datetime.now().year, month=9, day=27)
__CONTINUOUS_SCHEDULE = {
    "start": __CONTINUOUS_PERIOD_START,
    "end": __CONTINUOUS_PERIOD_END
}

__SCHEDULE = Schedule(__STANDARD_DELTA, __SHORT_DELTA, __LAUNCH_DELTA, __CONTINUOUS_DELTA, [__SHORT_DAY],
                      __WEEKEND_DAYS,
                      __CONTINUOUS_SCHEDULE)

__START_HOUR = datetime(year=datetime.now().year, month=7, day=7, hour=7, minute=0, second=0)
__END_HOUR = datetime(year=datetime.now().year, month=7, day=7, hour=15, minute=0, second=0)
__CONTINUOUS_DAY = Workday(__START_HOUR, __END_HOUR)

__START_HOUR = datetime(year=datetime.now().year, month=1, day=1, hour=8, minute=0, second=0)
__END_HOUR = datetime(year=datetime.now().year, month=3, day=1, hour=15, minute=0, second=0)
__USUAL_WORKDAY = Workday(__START_HOUR, __END_HOUR)


@pytest.mark.parametrize("day,expected_result", [
    (__USUAL_WORKDAY, False),
    (__CONTINUOUS_DAY, True)])
def it_should_return_the_expected_response_fulfilling_the_schedule(day, expected_result):
    operation = ContinuousDayScheduleOperation(__SCHEDULE)
    assert operation.fulfill(day) == expected_result, f"It should return {expected_result} for {day}"


def it_should_return_false_fulfilling_a_schedule_without_continuous_period():
    schedule_properties = __SCHEDULE.__dict__
    schedule_properties.pop("continuous_period")
    new_schedule = Schedule(**schedule_properties)

    operation = ContinuousDayScheduleOperation(new_schedule)

    assert not operation.fulfill(__CONTINUOUS_DAY), f"It should return false for schedule without continuous period"


def it_should_return_the_expected_calculation():
    operation = ContinuousDayScheduleOperation(__SCHEDULE)

    assert operation.calculate_worked_time(__CONTINUOUS_DAY)[0] == __CONTINUOUS_DELTA, \
        f"It should return {__CONTINUOUS_DELTA} as calculation result"


def it_should_return_the_expected_delta_calculation():
    operation = ContinuousDayScheduleOperation(__SCHEDULE)

    assert operation.calculate_worked_time(__CONTINUOUS_DAY)[1] == __CONTINUOUS_DELTA, \
        f"It should return {__CONTINUOUS_DELTA} as expected calculation result"


def it_should_return_the_expected_extra_time_calculation():
    operation = ContinuousDayScheduleOperation(__SCHEDULE)
    expected_result = timedelta(hours=0)

    assert operation.calculate_extra_time(__CONTINUOUS_DAY) == expected_result, \
        f"It should return {expected_result} as calculation result"
