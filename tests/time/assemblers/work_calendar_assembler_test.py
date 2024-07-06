import datetime
from datetime import timedelta

from holidays import country_holidays
from pytest import fixture

from schedule_calculator.time.assemblers.time_formatter import TimeFormatter
from schedule_calculator.time.assemblers.work_calendar_assembler import WorkCalendarAssembler
from schedule_calculator.time.schedule import Schedule

    
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
__EXPECTED_CONTINUOUS_SCHEDULE_VALUE = Schedule(work_time=__CONTINUOUS_DELTA, period=__EXPECTED_CONTINUOUS_PERIOD_VALUE)


def it_should_not_return_none(time_formatter, clock):
    work_calendar_assembler = WorkCalendarAssembler(time_formatter, clock)

    assert work_calendar_assembler.get_work_calendar(__WORK_CALENDAR_CONFIG) is not None, "It should not return none"


def it_should_return_the_expected_work_calendar_with_standard_time_value(time_formatter, clock):
    work_calendar = WorkCalendarAssembler(time_formatter, clock).get_work_calendar(__WORK_CALENDAR_CONFIG)

    assert work_calendar.standard_time == __STANDARD_TIME, f"It should return {__STANDARD_TIME} as standard time"


def it_should_return_the_expected_work_calendar_with_short_time_value(time_formatter, clock):
    work_calendar = WorkCalendarAssembler(time_formatter, clock).get_work_calendar(__WORK_CALENDAR_CONFIG)

    assert work_calendar.short_time == __SHORT_TIME, f"It should return {__SHORT_TIME} as short time"


def it_should_return_the_expected_work_calendar_with_launch_time_value(time_formatter, clock):
    work_calendar = WorkCalendarAssembler(time_formatter, clock).get_work_calendar(__WORK_CALENDAR_CONFIG)

    assert work_calendar.launch_time == __LAUNCH_TIME, f"It should return {__LAUNCH_TIME} as launch time"


def it_should_return_the_expected_work_calendar_with_short_days_value(time_formatter, clock):
    work_calendar = WorkCalendarAssembler(time_formatter, clock).get_work_calendar(__WORK_CALENDAR_CONFIG)

    assert work_calendar.short_days == __SHORT_DAYS, f"It should return {__SHORT_DAYS} as launch time"


def it_should_return_the_expected_work_calendar_with_current_date_value(time_formatter, clock):
    work_calendar = WorkCalendarAssembler(time_formatter, clock).get_work_calendar(__WORK_CALENDAR_CONFIG)
    assert work_calendar.current_date == __CURRENT_DATE, f"It should return {__CURRENT_DATE} as current_date"


def it_should_return_the_expected_work_calendar_with_free_days_value(time_formatter, clock):
    work_calendar = WorkCalendarAssembler(time_formatter, clock).get_work_calendar(__WORK_CALENDAR_CONFIG)

    assert work_calendar.free_days == __FREE_DAYS, \
        f"It should return {__FREE_DAYS} as free day"


def it_should_return_the_expected_work_calendar_with_continuous_work_schedule(time_formatter, clock):
    work_calendar = WorkCalendarAssembler(time_formatter, clock).get_work_calendar(__WORK_CALENDAR_CONFIG)
    
    assert work_calendar.continuous_schedule == __EXPECTED_CONTINUOUS_SCHEDULE_VALUE, \
        f"It should return {__EXPECTED_CONTINUOUS_SCHEDULE_VALUE} as continuous schedule schedule"

def it_should_return_the_expected_work_calendar_without_continuous_work_schedule(time_formatter, clock):
    new_work_config = __WORK_CALENDAR_CONFIG.copy()
    new_work_config.pop("continuous_schedule")

    work_calendar = WorkCalendarAssembler(time_formatter, clock).get_work_calendar(new_work_config)

    assert not work_calendar.continuous_schedule

@fixture
def time_formatter():
    return TimeFormatter()


@fixture
def clock():
    clock = ClockFake()
    clock.set_current_date(__CURRENT_DATE)
    return ClockFake()
