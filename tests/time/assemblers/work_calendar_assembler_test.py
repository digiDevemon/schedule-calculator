import datetime
from datetime import timedelta

from holidays import country_holidays
from pytest import fixture

from schedule_calculator.time.assemblers.work_calendar_assembler import WorkCalendarAssembler
from schedule_calculator.time.date_period import DatePeriod
from schedule_calculator.time.schedule import Schedule
from tests.fakes.clock_fake import ClockFake

__SHORT_DAYS = ["Friday"]
__WORK_CALENDAR_CONFIG = {
    "standard": "08:15",
    "location": "ES-MD",
    "launch": "00:45",
    "continuous_schedule": {
        "work_time": "8:00",
        "period": {"start": "5-20",
                   "end": "9-27"}
    },
    "short_schedule": {
        "work_time": "7:00",
        "days": __SHORT_DAYS
    }
}
__STANDARD_TIME = timedelta(hours=8, minutes=15)
__LAUNCH_TIME = timedelta(minutes=45)
__CONTINUOUS_DELTA = timedelta(hours=8, minutes=0)

__CURRENT_DATE = datetime.date.today()
__FREE_DAYS = country_holidays("ES", subdiv="MD", years=__CURRENT_DATE.year)
__CONTINUOUS_PERIOD_START = datetime.date(year=__CURRENT_DATE.year, month=5, day=20)
__CONTINUOUS_PERIOD_END = datetime.date(year=__CURRENT_DATE.year, month=9, day=27)

__EXPECTED_CONTINUOUS_SCHEDULE_VALUE = Schedule(work_time=__CONTINUOUS_DELTA,
                                                period=DatePeriod(start=__CONTINUOUS_PERIOD_START,
                                                                  end=__CONTINUOUS_PERIOD_END))
__SHORT_TIME = timedelta(hours=7)
__EXPECTED_SHORT_SCHEDULE = Schedule(work_time=__SHORT_TIME, days=__SHORT_DAYS)


def it_should_not_return_none(clock):
    work_calendar_assembler = WorkCalendarAssembler(clock)

    assert work_calendar_assembler.get_work_calendar(__WORK_CALENDAR_CONFIG) is not None, "It should not return none"


def it_should_return_the_expected_work_calendar_with_standard_time_value(clock):
    work_calendar = WorkCalendarAssembler(clock).get_work_calendar(__WORK_CALENDAR_CONFIG)

    assert work_calendar.standard_time == __STANDARD_TIME, f"It should return {__STANDARD_TIME} as standard time"


def it_should_return_the_expected_work_calendar_with_launch_time_value(clock):
    work_calendar = WorkCalendarAssembler(clock).get_work_calendar(__WORK_CALENDAR_CONFIG)

    assert work_calendar.launch_time == __LAUNCH_TIME, f"It should return {__LAUNCH_TIME} as launch time"


def it_should_return_the_expected_work_calendar_with_current_date_value(clock):
    work_calendar = WorkCalendarAssembler(clock).get_work_calendar(__WORK_CALENDAR_CONFIG)
    assert work_calendar.current_date == __CURRENT_DATE, f"It should return {__CURRENT_DATE} as current_date"


def it_should_return_the_expected_work_calendar_with_free_days_value(clock):
    work_calendar = WorkCalendarAssembler(clock).get_work_calendar(__WORK_CALENDAR_CONFIG)

    assert work_calendar.free_days == __FREE_DAYS, \
        f"It should return {__FREE_DAYS} as free day"


def it_should_return_the_expected_work_calendar_with_continuous_work_schedule(clock):
    work_calendar = WorkCalendarAssembler(clock).get_work_calendar(__WORK_CALENDAR_CONFIG)

    assert work_calendar.continuous_schedule == __EXPECTED_CONTINUOUS_SCHEDULE_VALUE, \
        f"It should return {__EXPECTED_CONTINUOUS_SCHEDULE_VALUE} as continuous schedule schedule"


def it_should_return_the_expected_work_calendar_without_continuous_work_schedule(clock):
    new_work_config = __WORK_CALENDAR_CONFIG.copy()
    new_work_config.pop("continuous_schedule")

    work_calendar = WorkCalendarAssembler(clock).get_work_calendar(new_work_config)

    assert not work_calendar.continuous_schedule


def it_should_return_the_expected_work_calendar_with_short_schedule(clock):
    work_calendar = WorkCalendarAssembler(clock).get_work_calendar(__WORK_CALENDAR_CONFIG)

    assert work_calendar.short_schedule == __EXPECTED_SHORT_SCHEDULE, \
        f"It should return {__EXPECTED_SHORT_SCHEDULE} as short schedule schedule"


def it_should_return_the_expected_work_calendar_without_short_schedule(clock):
    new_work_config = __WORK_CALENDAR_CONFIG.copy()
    new_work_config.pop("short_schedule")

    work_calendar = WorkCalendarAssembler(clock).get_work_calendar(new_work_config)

    assert not work_calendar.short_schedule


@fixture
def clock():
    clock = ClockFake()
    clock.set_current_date(__CURRENT_DATE)
    return ClockFake()
