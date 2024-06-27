import datetime

import pytest
from holidays import country_holidays

from schedule_calculator.time.assemblers.free_days_calendar_assembler import FreeDaysCalendarAssembler

__YEAR = datetime.datetime.now().year
__COUNTRY_CODE = "GB"


def it_should_not_return_none():
    free_days_calendar = FreeDaysCalendarAssembler()
    assert free_days_calendar.get_calendar_from_str(__COUNTRY_CODE, __YEAR) is not None


@pytest.mark.parametrize("country,expected_result", [
    ("DE-ST", country_holidays("DE", subdiv="ST", years=datetime.datetime.now().year)),
    ("ES-MD", country_holidays("ES", subdiv="MD", years=datetime.datetime.now().year)),
    ("FR", country_holidays("FR", years=datetime.datetime.now().year))])
def it_should_return_the_expected_holiday_base_object(country, expected_result):
    free_days_calendar = FreeDaysCalendarAssembler()
    assert free_days_calendar.get_calendar_from_str(country, datetime.datetime.now().year) == expected_result, \
        f"It should return the expected {expected_result}"
