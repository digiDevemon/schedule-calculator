import datetime

from schedule_calculator.time.clock import Clock

__DATE_FORMATTER = "%HH:%MM"


def it_should_not_return_none_when_retrieves_today_day():
    clock = Clock()
    assert clock.get_today_day() is not None, "It should not return none"


def it_should_return_the_expected_today_day():
    clock = Clock()
    today_day = datetime.date.today().strftime("%A")
    assert clock.get_today_day() == today_day, f"It should return {today_day}"


def it_should_return_the_expected_actual_time_delta():
    clock = Clock()
    now = datetime.datetime.now().strftime(__DATE_FORMATTER)
    assert clock.get_current_time().strftime(__DATE_FORMATTER) == now, f"It should return datetime"
