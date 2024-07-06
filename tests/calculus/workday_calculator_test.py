from datetime import datetime, timedelta, date

from holidays import country_holidays

from schedule_calculator.calculus.workday_calculator import WorkDayCalculator
from schedule_calculator.time.date_period import DatePeriod
from schedule_calculator.time.schedule import Schedule
from schedule_calculator.time.work_calendar import WorkCalendar
from schedule_calculator.time.workday import Workday

__STANDARD_DELTA = timedelta(hours=8, minutes=15)
__SHORT_DELTA = timedelta(hours=7)
__LAUNCH_DELTA = timedelta(hours=0, minutes=45)

__SHORT_DAYS = ['Friday']
__WEEKEND_DAYS = ['Saturday', 'Sunday']
__CURRENT_DATE = datetime(year=1997, month=5, day=20)

__FREE_DAYS = country_holidays("ES", years=1997)

__CONTINUOUS_DELTA = timedelta(hours=8, minutes=0)
__CONTINUOUS_PERIOD_START = date(year=__CURRENT_DATE.year, month=5, day=20)
__CONTINUOUS_PERIOD_END = date(year=__CURRENT_DATE.year, month=9, day=27)
__CONTINUOUS_SCHEDULE = Schedule(work_time=__CONTINUOUS_DELTA,
                                 period=DatePeriod(start=__CONTINUOUS_PERIOD_START, end=__CONTINUOUS_PERIOD_END))

__WORK_CALENDAR = WorkCalendar(__CURRENT_DATE, __STANDARD_DELTA, __SHORT_DELTA, __LAUNCH_DELTA, __SHORT_DAYS,
                               __FREE_DAYS, __CONTINUOUS_SCHEDULE)

__START_HOUR = datetime(year=__CURRENT_DATE.year, month=1, day=7, hour=8, minute=0, second=0)
__END_HOUR = datetime(year=__CURRENT_DATE.year, month=1, day=7, hour=17, minute=0, second=0)

__EXPECTED_ZERO_DELTA_HOURS = timedelta(hours=0)
__EXPECTED_STANDARD_DELTA_HOURS = timedelta(hours=8, minutes=15)
__EXPECTED_WORDED_HOURS = timedelta(hours=8, minutes=15)


def it_should_not_return_none_when_calculates_worked_time():
    assert WorkDayCalculator(__WORK_CALENDAR).calculate_worked_time(Workday(__START_HOUR, __END_HOUR)) is not None, \
        "It should return something"


def it_should_return_the_expected_time_when_calculates_worked_time():
    assert (WorkDayCalculator(__WORK_CALENDAR).calculate_worked_time(Workday(__START_HOUR, __END_HOUR))[0]
            == __EXPECTED_WORDED_HOURS), \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected {__EXPECTED_WORDED_HOURS} on a regular day")


def it_should_return_the_expected_standard_delta_hours_when_calculates_worked_time():
    assert (WorkDayCalculator(__WORK_CALENDAR).calculate_worked_time(Workday(__START_HOUR, __END_HOUR))[1]
            == __EXPECTED_STANDARD_DELTA_HOURS), \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected delta {__EXPECTED_STANDARD_DELTA_HOURS} on a regular day")


def it_should_not_return_none_when_calculates_extra_time():
    assert WorkDayCalculator(__WORK_CALENDAR).calculate_extra_time_today(Workday(__START_HOUR, __END_HOUR)) is not None, \
        "It should return something"


def it_should_return_the_expected_result_when_calculates_extra_time():
    assert WorkDayCalculator(__WORK_CALENDAR).calculate_extra_time_today(
        Workday(__START_HOUR, __END_HOUR)) == __EXPECTED_ZERO_DELTA_HOURS, \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected delta {__EXPECTED_ZERO_DELTA_HOURS} on a regular day for extra time")
