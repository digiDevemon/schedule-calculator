import datetime

from pytest import fixture, raises
from schedule_calculator.time.exceptions.schedule_parsing import ScheduleParsingError
from schedule_calculator.time.assemblers.time_formatter import TimeFormatter

__TIME_STRING = "1997-07-07T07:07:00Z"
__TIME_DELTA = datetime.datetime(year=1997, month=7, day=7, hour=7, minute=7, second=0)

__DATE_STRING = "05-27"
__EXPECTED_DATE_OBJECT = datetime.date(year=datetime.datetime.now().year, month=5, day=27)


def it_should_not_return_none_when_retrieves_time_from_str(time_formatter):
    assert time_formatter.get_time_from_str(__TIME_STRING) is not None, "It should not return none"


def it_should_return_the_expected_time_from_str(time_formatter):
    assert time_formatter.get_time_from_str(__TIME_STRING) == __TIME_DELTA, f"It should return {__TIME_DELTA}"


def it_should_return_the_expected_str_from_time(time_formatter):
    assert time_formatter.get_str_from_time(__TIME_DELTA) == __TIME_STRING, f"It should return {__TIME_STRING}"


def it_should_return_the_expected_date_from_str(time_formatter):
    assert time_formatter.get_date_from_str(__DATE_STRING) == __EXPECTED_DATE_OBJECT, \
        f"It should return {__EXPECTED_DATE_OBJECT}"


def it_should_raise_an_exception_when_it_is_not_able_to_get_date_from_str(time_formatter):
    with raises(ScheduleParsingError) as exc_info:
        time_formatter.get_date_from_str("foo")
    assert exc_info.type is ScheduleParsingError, "It should raise an exception"


@fixture
def time_formatter():
    return TimeFormatter()
