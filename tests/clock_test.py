import datetime

from schedule_calculator.clock import Clock


def it_should_not_return_none_when_retrieves_today_day():
    clock = Clock()
    assert clock.get_today_day() is not None


def it_should_not_return_the_expected_today_day():
    clock = Clock()
    today_day = datetime.date.today().strftime("%A")
    assert clock.get_today_day() == today_day
