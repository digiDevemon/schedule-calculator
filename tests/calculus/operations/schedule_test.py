from datetime import timedelta, date, datetime

import pytest

from schedule_calculator.calculus.operations.schedule import ScheduleOperation
from schedule_calculator.time.date_period import DatePeriod
from schedule_calculator.time.schedule import Schedule
from schedule_calculator.time.workday import Workday

__CURRENT_DATE = datetime(year=1997, month=5, day=20)

__SCHEDULE_DELTA = timedelta(hours=8, minutes=0)
__SCHEDULE_PERIOD_START = date(year=__CURRENT_DATE.year, month=5, day=20)
__SCHEDULE_PERIOD_END = date(year=__CURRENT_DATE.year, month=9, day=27)
__SCHEDULE_PERIOD = {
    "start": __SCHEDULE_PERIOD_START,
    "end": __SCHEDULE_PERIOD_END
}
__SCHEDULE_DAYS = ["Friday"]
__TESTED_SCHEDULE = Schedule(work_time=__SCHEDULE_DELTA,
                             period=DatePeriod(start=__SCHEDULE_PERIOD_START, end=__SCHEDULE_PERIOD_END),
                             days=__SCHEDULE_DAYS)

__START_HOUR = datetime(year=__CURRENT_DATE.year, month=7, day=7, hour=7, minute=0, second=0)
__END_HOUR = datetime(year=__CURRENT_DATE.year, month=7, day=7, hour=15, minute=0, second=0)
__SCHEDULE_DAY = Workday(__START_HOUR, __END_HOUR)

__START_HOUR = datetime(year=__CURRENT_DATE.year, month=7, day=11, hour=7, minute=0, second=0)
__END_HOUR = datetime(year=__CURRENT_DATE.year, month=7, day=11, hour=15, minute=0, second=0)
__FRIDAY_SCHEDULE_DAY = Workday(__START_HOUR, __END_HOUR)

__START_HOUR = datetime(year=__CURRENT_DATE.year, month=1, day=1, hour=8, minute=0, second=0)
__END_HOUR = datetime(year=__CURRENT_DATE.year, month=3, day=1, hour=15, minute=0, second=0)
__USUAL_WORKDAY = Workday(__START_HOUR, __END_HOUR)


@pytest.mark.parametrize("day,expected_result", [
    (__USUAL_WORKDAY, False),
    (__SCHEDULE_DAY, True),
    (__FRIDAY_SCHEDULE_DAY, True)
])
def it_should_return_the_expected_response_fulfilling_the_schedule(day, expected_result):
    operation = ScheduleOperation(__TESTED_SCHEDULE)
    assert operation.fulfill(day) == expected_result, f"It should return {expected_result} for {day}"


def it_should_not_fulfill_when_there_is_no_schedule():
    operation = ScheduleOperation(None)
    assert not operation.fulfill(__SCHEDULE_DAY), f"It should not fulfill for non existing schedule"


def it_should_return_the_expected_calculation():
    operation = ScheduleOperation(__TESTED_SCHEDULE)

    assert operation.calculate_worked_time(__SCHEDULE_DAY)[0] == __SCHEDULE_DELTA, \
        f"It should return {__SCHEDULE_DELTA} as calculation result"


def it_should_return_the_expected_delta_calculation():
    operation = ScheduleOperation(__TESTED_SCHEDULE)

    assert operation.calculate_worked_time(__SCHEDULE_DAY)[1] == __SCHEDULE_DELTA, \
        f"It should return {__SCHEDULE_DELTA} as expected calculation result"


def it_should_return_the_expected_extra_time_calculation():
    operation = ScheduleOperation(__TESTED_SCHEDULE)
    expected_result = timedelta(hours=0)

    assert operation.calculate_extra_time(__SCHEDULE_DAY) == expected_result, \
        f"It should return {expected_result} as calculation result"

