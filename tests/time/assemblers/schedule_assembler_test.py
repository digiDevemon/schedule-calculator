from datetime import date

from schedule_calculator.time.assemblers.schedule_assembler import ScheduleAssembler
from schedule_calculator.time.date_period import DatePeriod

__EXPECTED_DAYS = ["Tuesday"]
__SCHEDULE_CONFIGURATION = {
    "continuous_schedule": {
        "work_time": "8:00",
        "period": {"start": "5-20",
                   "end": "9-27"},
        "days": __EXPECTED_DAYS
    }
}
__EXPECTED_PERIOD = DatePeriod(start=date(year=date.today().year, month=5, day=20),
                               end=date(year=date.today().year, month=9, day=27))


def it_should_not_return_none():
    schedule_assembler = ScheduleAssembler()
    schedule = schedule_assembler.get_schedule_from_config(__SCHEDULE_CONFIGURATION.get("continuous_schedule"))

    assert schedule is not None


def it_should_return_none_when_there_is_no_configuration():
    schedule_assembler = ScheduleAssembler()
    new_configuration = __SCHEDULE_CONFIGURATION.copy()
    new_configuration.pop("continuous_schedule")
    schedule = schedule_assembler.get_schedule_from_config(new_configuration.get("continuous_schedule"))
    assert schedule is None


def it_should_return_the_expected_schedule_with_expected_period():
    schedule_assembler = ScheduleAssembler()
    schedule = schedule_assembler.get_schedule_from_config(__SCHEDULE_CONFIGURATION.get("continuous_schedule"))

    assert schedule.period == __EXPECTED_PERIOD, f"It should return the expected period {__EXPECTED_PERIOD}"


def it_should_return_the_expected_schedule_without_period():
    schedule_assembler = ScheduleAssembler()
    new_configuration = __SCHEDULE_CONFIGURATION.copy()
    new_configuration["continuous_schedule"].pop("period")
    schedule = schedule_assembler.get_schedule_from_config(__SCHEDULE_CONFIGURATION.get("continuous_schedule"))

    assert not schedule.period, f"It should not contains period"


def it_should_return_the_expected_schedule_with_expected_days():
    schedule_assembler = ScheduleAssembler()
    schedule = schedule_assembler.get_schedule_from_config(__SCHEDULE_CONFIGURATION.get("continuous_schedule"))

    assert schedule.days == __EXPECTED_DAYS, f"It should return the expected days {__EXPECTED_DAYS}"


def it_should_return_the_expected_schedule_without_days():
    schedule_assembler = ScheduleAssembler()
    new_configuration = __SCHEDULE_CONFIGURATION.copy()
    new_configuration["continuous_schedule"].pop("days")
    schedule = schedule_assembler.get_schedule_from_config(__SCHEDULE_CONFIGURATION.get("continuous_schedule"))

    assert not schedule.days, f"It should not contains days"
