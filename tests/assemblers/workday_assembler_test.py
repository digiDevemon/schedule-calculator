from schedule_calculator.assemblers.time_assembler import TimeFormatter
from schedule_calculator.assemblers.workday_assembler import WorkDayAssembler
from schedule_calculator.workday_calculator import WorkDayCalculator

__CONFIG = {
    "schedule": {
        "standard": "8:15",
        "short": "7:00",
        "launch": "0:45",
        "short_day": "Friday"
    }
}


def it_should_not_return_none():
    time_formatter = TimeFormatter()
    workday_assembler = WorkDayAssembler(time_formatter)
    assert workday_assembler.get_workday_from_configuration(__CONFIG) is not None


def it_should_return_the_expected_type_object():
    time_formatter = TimeFormatter()
    workday_assembler = WorkDayAssembler(time_formatter)
    assert type(workday_assembler.get_workday_from_configuration(__CONFIG)) is WorkDayCalculator
