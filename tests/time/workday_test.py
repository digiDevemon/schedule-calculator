import datetime

from schedule_calculator.time.workday import Workday
import pytest

__START_DAY = datetime.datetime(year=2024, month=6, day=7, hour=7)
__END_DAY = datetime.datetime(year=2024, month=6, day=7, hour=15)


def it_should_return_the_expected_as_day():
    assert Workday(__START_DAY, __END_DAY).get_day() == "Friday", \
        f"It should return Friday"


@pytest.mark.parametrize("init_date,end_date,expected_result", [
    (datetime.date(year=2024, month=4, day=1), datetime.date(year=2024, month=7, day=1), True),
    (datetime.date(year=2024, month=1, day=1), datetime.date(year=2024, month=2, day=1), False)])
def it_should_return_the_expected_value_date_period(init_date, end_date, expected_result):
    assert Workday(__START_DAY, __END_DAY).is_in_period(init_date, end_date) == expected_result, \
        f"It should return for a given period between {init_date} and {end_date} the expected result {expected_result}"
