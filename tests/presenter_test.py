import io
from contextlib import redirect_stdout
from datetime import timedelta

from schedule_calculator.presenter import Presenter


def it_should_print_the_expected_message_when_present_worked_hours():
    worked_hours = timedelta(hours=2)
    expected_worked_hours = timedelta(hours=3)

    presenter = Presenter()

    output = io.StringIO()
    with redirect_stdout(output):
        presenter.present_workday(worked_hours, expected_worked_hours)
    out_value = output.getvalue().replace("\n", "")

    assert out_value == f"You have worked 02:00. Today you have to work 03:00.", \
        "It should execute by standard output the expected message"


def it_should_print_the_expected_message_for_negative_hours_when_present_worked_hours():
    worked_hours = timedelta(hours=-2)
    expected_worked_hours = timedelta(hours=3)

    presenter = Presenter()

    output = io.StringIO()
    with redirect_stdout(output):
        presenter.present_workday(worked_hours, expected_worked_hours)
    out_value = output.getvalue().replace("\n", "")

    assert out_value == f"You have worked 00:00. Today you have to work 03:00.", \
        "It should execute by standard output the expected message"


def it_should_print_the_expected_message_when_present_extra_hours():
    extra_hours = timedelta(hours=2)

    presenter = Presenter()

    output = io.StringIO()
    with redirect_stdout(output):
        presenter.present_extra_hours(extra_hours)
    out_value = output.getvalue().replace("\n", "")

    assert out_value == f"You already have completed your workday. You have worked 02:00 extra hours.", \
        "It should execute by standard output the expected message"
