import datetime

from schedule_calculator.clock import Clock


def it_should_not_return_none_when_retrieves_today_day():
    clock = Clock()
    assert clock.get_today_day() is not None


def it_should_return_the_expected_today_day():
    clock = Clock()
    today_day = datetime.date.today().strftime("%A")
    assert clock.get_today_day() == today_day


def it_should_return_the_expected_actual_time_delta():
    clock = Clock()
    today = datetime.datetime.now()
    expected_delta = datetime.timedelta(hours=today.hour, minutes=today.minute)
    assert clock.get_delta_now() == expected_delta
