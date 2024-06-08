from datetime import datetime, timedelta

from schedule_calculator.time.schedule import Schedule
from schedule_calculator.calculus.workday_calculator import WorkDayCalculator

__STANDARD_DELTA = timedelta(hours=8, minutes=15)
__SHORT_DELTA = timedelta(hours=7)
__LAUNCH_DELTA = timedelta(hours=0, minutes=45)
__SHORT_DAY = 'Friday'
__STANDARD_DAY = 'Monday'
__WEEKEND_DAY = 'Saturday'
__WEEKEND_DAYS = [__WEEKEND_DAY, 'Sunday']
__SCHEDULE = Schedule(__STANDARD_DELTA, __SHORT_DELTA, __LAUNCH_DELTA, [__SHORT_DAY], __WEEKEND_DAYS)

__START_HOUR = datetime(year=1997, month=7, day=7, hour=8, minute=0, second=0)
__END_HOUR = datetime(year=1997, month=7, day=7, hour=17, minute=0, second=0)
__EFFECTIVE_HOURS = timedelta(hours=9)
__END_HOUR_FRIDAY = datetime(year=1997, month=7, day=7, hour=15, minute=0, second=0)

__FRIDAY_DAY = datetime(2024, 5, 3)

__EXPECTED_SHORT_DELTA_HOURS = timedelta(hours=7)
__EXPECTED_ZERO_DELTA_HOURS = timedelta(hours=0)
__EXPECTED_STANDARD_DELTA_HOURS = timedelta(hours=8, minutes=15)
__EXPECTED_WORDED_HOURS = timedelta(hours=8, minutes=15)
__EXPECTED_WORKED_HOURS_ON_FRIDAY = timedelta(hours=9)


def it_should_not_return_none_when_calculates_worked_time():
    assert WorkDayCalculator(__SCHEDULE).calculate_worked_time(__STANDARD_DAY, __START_HOUR, __END_HOUR) is not None, \
        "It should return something"


def it_should_return_the_expected_time_when_calculates_worked_time():
    assert (WorkDayCalculator(__SCHEDULE).calculate_worked_time(__STANDARD_DAY, __START_HOUR, __END_HOUR)[0]
            == __EXPECTED_WORDED_HOURS), \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected {__EXPECTED_WORDED_HOURS} on a regular day")


def it_should_return_the_expected_standard_delta_hours_when_calculates_worked_time():
    assert (WorkDayCalculator(__SCHEDULE).calculate_worked_time(__STANDARD_DAY, __START_HOUR,
                                                                __END_HOUR)[1]
            == __EXPECTED_STANDARD_DELTA_HOURS), \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected delta {__EXPECTED_STANDARD_DELTA_HOURS} on a regular day")


def it_should_not_return_none_when_calculates_extra_time():
    assert WorkDayCalculator(__SCHEDULE).calculate_extra_time_today(__STANDARD_DAY, __START_HOUR,
                                                                    __END_HOUR) is not None, \
        "It should return something"


def it_should_return_the_expected_result_when_calculates_extra_time():
    assert (WorkDayCalculator(__SCHEDULE).calculate_extra_time_today(__STANDARD_DAY, __START_HOUR, __END_HOUR)[0]
            == __EXPECTED_ZERO_DELTA_HOURS), \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected delta {__EXPECTED_ZERO_DELTA_HOURS} on a regular day for extra time")


def it_should_return_the_expected_result_when_calculates_extra_time_on_friday():
    assert (WorkDayCalculator(__SCHEDULE).calculate_extra_time_today(__SHORT_DAY, __START_HOUR,
                                                                     __END_HOUR_FRIDAY)[0]
            == __EXPECTED_ZERO_DELTA_HOURS), \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected delta {__EXPECTED_ZERO_DELTA_HOURS} on a short day for extra time")


def it_should_return_the_expected_result_when_calculates_extra_time_for_weekend():
    assert (WorkDayCalculator(__SCHEDULE).calculate_extra_time_today(__WEEKEND_DAY, __START_HOUR, __END_HOUR)[0]
            == __EFFECTIVE_HOURS), \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected extra time delta {__EFFECTIVE_HOURS} on a weekend")


def it_should_return_the_expected_expected_hours_when_calculates_extra_time_for_weekend():
    assert (WorkDayCalculator(__SCHEDULE).calculate_extra_time_today(__WEEKEND_DAY, __START_HOUR, __END_HOUR)[1]
            == timedelta(hours=0)), \
        (f"For a schedule started at {__START_HOUR} and ended at {__END_HOUR} it "
         f"should return the expected time delta {timedelta(hours=0)} on a weekend")
