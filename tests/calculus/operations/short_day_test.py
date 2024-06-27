from datetime import timedelta, datetime, date

import pytest
from holidays import country_holidays

from schedule_calculator.calculus.operations.short_day import ShortDayOperation
from schedule_calculator.time.schedule import Schedule
from schedule_calculator.time.workcalendar import WorkCalendar
from schedule_calculator.time.workday import Workday

__STANDARD_DELTA = timedelta(hours=8, minutes=15)
__SHORT_DELTA = timedelta(hours=7)
__LAUNCH_DELTA = timedelta(hours=0, minutes=45)

__SHORT_DAY = 'Friday'
__WEEKEND_DAYS = ['Saturday', 'Sunday']
__CURRENT_DATE = datetime(year=1997, month=5, day=20)
__FREE_DAYS = country_holidays("ES", years=__CURRENT_DATE.year)

__CONTINUOUS_DELTA = timedelta(hours=8, minutes=0)
__CONTINUOUS_PERIOD_START = date(year=__CURRENT_DATE.year, month=5, day=20)
__CONTINUOUS_PERIOD_END = date(year=__CURRENT_DATE.year, month=9, day=27)
__CONTINUOUS_PERIOD = {
    "start": __CONTINUOUS_PERIOD_START,
    "end": __CONTINUOUS_PERIOD_END
}
__CONTINUOUS_SCHEDULE = Schedule(work_time=__CONTINUOUS_DELTA, period=__CONTINUOUS_PERIOD)

__WORK_CALENDAR = WorkCalendar(__CURRENT_DATE, __STANDARD_DELTA, __SHORT_DELTA, __LAUNCH_DELTA,
                               [__SHORT_DAY], __FREE_DAYS, __CONTINUOUS_SCHEDULE)

__START_HOUR = datetime(year=__CURRENT_DATE.year, month=7, day=7, hour=8, minute=0, second=0)
__END_HOUR = datetime(year=__CURRENT_DATE.year, month=7, day=7, hour=17, minute=0, second=0)
__WORKDAY = Workday(__START_HOUR, __END_HOUR)

__START_HOUR = datetime(year=__CURRENT_DATE.year, month=7, day=11, hour=8, minute=0, second=0)
__END_HOUR = datetime(year=__CURRENT_DATE.year, month=7, day=11, hour=15, minute=0, second=0)
__SHORT_WORKDAY = Workday(__START_HOUR, __END_HOUR)


@pytest.mark.parametrize("day,expected_result", [
    (__SHORT_WORKDAY, True),
    (__WORKDAY, False)])
def it_should_return_the_expected_response_fulfilling_the_schedule(day, expected_result):
    operation = ShortDayOperation(__WORK_CALENDAR)
    assert operation.fulfill(day) == expected_result, f"It should return {expected_result} for {day}"


def it_should_return_the_expected_calculation():
    operation = ShortDayOperation(__WORK_CALENDAR)

    assert operation.calculate_worked_time(__SHORT_WORKDAY)[0] == __SHORT_DELTA, \
        f"It should return {__SHORT_DELTA} as calculation result"


def it_should_return_the_expected_delta_calculation():
    operation = ShortDayOperation(__WORK_CALENDAR)

    assert operation.calculate_worked_time(__SHORT_WORKDAY)[1] == __SHORT_DELTA, \
        f"It should return {__SHORT_DELTA} as expected calculation result"


def it_should_return_the_expected_extra_time_calculation():
    operation = ShortDayOperation(__WORK_CALENDAR)
    expected_result = timedelta(hours=0)

    assert operation.calculate_extra_time(__SHORT_WORKDAY) == expected_result, \
        f"It should return {expected_result} as calculation result"
