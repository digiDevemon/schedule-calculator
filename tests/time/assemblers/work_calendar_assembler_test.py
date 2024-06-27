import datetime
from datetime import timedelta

from holidays import country_holidays
from pytest import fixture

from schedule_calculator.time.assemblers.time_formatter import TimeFormatter
from schedule_calculator.time.assemblers.work_calendar_assembler import WorkCalendarAssembler
from tests.fakes.clock_fake import ClockFake

__SHORT_DAYS = ["Friday"]
__WEEKEND_DAYS = ["Saturday", "Sunday"]
__WORK_CALENDAR_CONFIG = {
    "standard": "08:15",
    "short": "07:00",
    "location": "ES-MD",
    "launch": "00:45",
    "short_days": __SHORT_DAYS,
    "weekend_days": __WEEKEND_DAYS,
    "continuous_schedule": {
        "work_time": "8:00",
        "period": {"start": "5-20",
                   "end": "9-27"}
    }
}
__STANDARD_TIME = timedelta(hours=8, minutes=15)
__SHORT_TIME = timedelta(hours=7)
__LAUNCH_TIME = timedelta(minutes=45)
__CONTINUOUS_DELTA = timedelta(hours=8, minutes=0)

__CURRENT_DATE = datetime.date.today()
__FREE_DAYS = country_holidays("ES", subdiv="MD", years=__CURRENT_DATE.year)
__CONTINUOUS_PERIOD_START = datetime.date(year=__CURRENT_DATE.year, month=5, day=20)
__CONTINUOUS_PERIOD_END = datetime.date(year=__CURRENT_DATE.year, month=9, day=27)
__EXPECTED_CONTINUOUS_PERIOD_VALUE = {
    "start": __CONTINUOUS_PERIOD_START,
    "end": __CONTINUOUS_PERIOD_END
}


def it_should_not_return_none(time_formatter, clock):
    schedule_assembler = WorkCalendarAssembler(time_formatter, clock)

    assert schedule_assembler.get_schedule(__WORK_CALENDAR_CONFIG) is not None, "It should not return none"


def it_should_return_the_expected_schedule_with_standard_time_value(time_formatter, clock):
    schedule = WorkCalendarAssembler(time_formatter, clock).get_schedule(__WORK_CALENDAR_CONFIG)

    assert schedule.standard_time == __STANDARD_TIME, f"It should return {__STANDARD_TIME} as standard time"


def it_should_return_the_expected_schedule_with_short_time_value(time_formatter, clock):
    schedule = WorkCalendarAssembler(time_formatter, clock).get_schedule(__WORK_CALENDAR_CONFIG)

    assert schedule.short_time == __SHORT_TIME, f"It should return {__SHORT_TIME} as short time"


def it_should_return_the_expected_schedule_with_launch_time_value(time_formatter, clock):
    schedule = WorkCalendarAssembler(time_formatter, clock).get_schedule(__WORK_CALENDAR_CONFIG)

    assert schedule.launch_time == __LAUNCH_TIME, f"It should return {__LAUNCH_TIME} as launch time"


def it_should_return_the_expected_schedule_with_short_days_value(time_formatter, clock):
    schedule = WorkCalendarAssembler(time_formatter, clock).get_schedule(__WORK_CALENDAR_CONFIG)

    assert schedule.short_days == __SHORT_DAYS, f"It should return {__SHORT_DAYS} as launch time"


def it_should_return_the_expected_schedule_with_current_date_value(time_formatter, clock):
    schedule = WorkCalendarAssembler(time_formatter, clock).get_schedule(__WORK_CALENDAR_CONFIG)
    assert schedule.current_date == __CURRENT_DATE, f"It should return {__CURRENT_DATE} as current_date"


def it_should_return_the_expected_schedule_with_free_days_value(time_formatter, clock):
    schedule = WorkCalendarAssembler(time_formatter, clock).get_schedule(__WORK_CALENDAR_CONFIG)

    assert schedule.free_days == __FREE_DAYS, \
        f"It should return {__FREE_DAYS} as free day"


@fixture
def time_formatter():
    return TimeFormatter()


@fixture
def clock():
    clock = ClockFake()
    clock.set_current_date(__CURRENT_DATE)
    return ClockFake()
