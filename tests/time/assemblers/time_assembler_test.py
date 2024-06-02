from datetime import timedelta

from schedule_calculator.time.assemblers.time_assembler import TimeFormatter

__TIME_STRING = "08:15"
__TIME_DELTA = timedelta(hours=8, minutes=15)


def it_should_not_return_none_when_retrieves_delta_from_str():
    time_formatter = TimeFormatter()
    assert time_formatter.get_delta_from_str(__TIME_STRING) is not None, "It should not return none"


def it_should_return_the_expected_delta_from_str():
    time_formatter = TimeFormatter()
    assert time_formatter.get_delta_from_str(__TIME_STRING) == __TIME_DELTA, f"It should return {__TIME_DELTA}"


def it_should_return_the_expected_str_from_delta():
    time_formatter = TimeFormatter()
    assert time_formatter.get_str_from_delta(__TIME_DELTA) == __TIME_STRING, f"It should return {__TIME_STRING}"
