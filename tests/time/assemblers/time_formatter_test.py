import datetime

from schedule_calculator.time.assemblers.time_formatter import TimeFormatter

__TIME_STRING = "1997-07-07T07:07:00Z"
__TIME_DELTA = datetime.datetime(year=1997, month=7, day=7, hour=7, minute=7, second=0)


def it_should_not_return_none_when_retrieves_time_from_str():
    time_formatter = TimeFormatter()
    assert time_formatter.get_time_from_str(__TIME_STRING) is not None, "It should not return none"


def it_should_return_the_expected_time_from_str():
    time_formatter = TimeFormatter()
    assert time_formatter.get_time_from_str(__TIME_STRING) == __TIME_DELTA, f"It should return {__TIME_DELTA}"


def it_should_return_the_expected_str_from_time():
    time_formatter = TimeFormatter()
    assert time_formatter.get_str_from_time(__TIME_DELTA) == __TIME_STRING, f"It should return {__TIME_STRING}"
