from datetime import timedelta

from schedule_calculator.assemblers.time_assembler import TimeFormatter

__TIME_STRING = "8:15"
__TIME_DELTA = timedelta(hours=8, minutes=15)


def it_should_not_return_none_when_retrieves_delta_from_str():
    time_formatter = TimeFormatter()
    assert time_formatter.get_delta_from_str(__TIME_STRING) is not None


def it_should_return_the_expected_delta_from_str():
    time_formatter = TimeFormatter()
    assert time_formatter.get_delta_from_str(__TIME_STRING) == __TIME_DELTA
