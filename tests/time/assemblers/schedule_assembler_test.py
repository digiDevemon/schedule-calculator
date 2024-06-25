import datetime
from datetime import timedelta

from schedule_calculator.time.assemblers.schedule_assembler import ScheduleAssembler
from schedule_calculator.time.assemblers.time_formatter import TimeFormatter

__SHORT_DAYS = ["Friday"]
__WEEKEND_DAYS = ["Saturday", "Sunday"]
__SCHEDULE_CONFIG = {
    "standard": "08:15",
    "short": "07:00",
    "launch": "00:45",
    "continuous": "8:00",
    "short_days": __SHORT_DAYS,
    "weekend_days": __WEEKEND_DAYS,
    "continuous_period": {
        "start": "5-20",
        "end": "9-27"
    }
}
__STANDARD_TIME = timedelta(hours=8, minutes=15)
__SHORT_TIME = timedelta(hours=7)
__LAUNCH_TIME = timedelta(minutes=45)
__CONTINUOUS_DELTA = timedelta(hours=8, minutes=0)

__CONTINUOUS_PERIOD_START = datetime.date(year=datetime.datetime.now().year, month=5, day=20)
__CONTINUOUS_PERIOD_END = datetime.date(year=datetime.datetime.now().year, month=9, day=27)
__EXPECTED_CONTINUOUS_PERIOD_VALUE = {
    "start": __CONTINUOUS_PERIOD_START,
    "end": __CONTINUOUS_PERIOD_END
}


def it_should_not_return_none():
    time_formatter = TimeFormatter()

    schedule_assembler = ScheduleAssembler(time_formatter)

    assert schedule_assembler.get_schedule(__SCHEDULE_CONFIG) is not None, "It should not return none"


def it_should_return_the_expected_schedule_with_standard_time_value():
    time_formatter = TimeFormatter()

    schedule = ScheduleAssembler(time_formatter).get_schedule(__SCHEDULE_CONFIG)

    assert schedule.standard_time == __STANDARD_TIME, f"It should return {__STANDARD_TIME} as standard time"


def it_should_return_the_expected_schedule_with_short_time_value():
    time_formatter = TimeFormatter()

    schedule = ScheduleAssembler(time_formatter).get_schedule(__SCHEDULE_CONFIG)

    assert schedule.short_time == __SHORT_TIME, f"It should return {__SHORT_TIME} as short time"


def it_should_return_the_expected_schedule_with_launch_time_value():
    time_formatter = TimeFormatter()

    schedule = ScheduleAssembler(time_formatter).get_schedule(__SCHEDULE_CONFIG)

    assert schedule.launch_time == __LAUNCH_TIME, f"It should return {__LAUNCH_TIME} as launch time"


def it_should_return_the_expected_schedule_with_short_days_value():
    time_formatter = TimeFormatter()

    schedule = ScheduleAssembler(time_formatter).get_schedule(__SCHEDULE_CONFIG)

    assert schedule.short_days == __SHORT_DAYS, f"It should return {__SHORT_DAYS} as launch time"


def it_should_return_the_expected_schedule_with_weekend_days_value():
    time_formatter = TimeFormatter()

    schedule = ScheduleAssembler(time_formatter).get_schedule(__SCHEDULE_CONFIG)

    assert schedule.weekend_days == __WEEKEND_DAYS, f"It should return {__WEEKEND_DAYS} as weekend time"


def it_should_return_the_expected_schedule_with_continuous_delta_value():
    time_formatter = TimeFormatter()

    schedule = ScheduleAssembler(time_formatter).get_schedule(__SCHEDULE_CONFIG)

    assert schedule.continuous_time == __CONTINUOUS_DELTA, \
        f"It should return {__CONTINUOUS_DELTA} as continuous delta"


def it_should_return_the_expected_schedule_with_continuous_period_days_value():
    time_formatter = TimeFormatter()

    schedule = ScheduleAssembler(time_formatter).get_schedule(__SCHEDULE_CONFIG)

    assert schedule.continuous_period == __EXPECTED_CONTINUOUS_PERIOD_VALUE, \
        f"It should return {__EXPECTED_CONTINUOUS_PERIOD_VALUE} as continuous period"
