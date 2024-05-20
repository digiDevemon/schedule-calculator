from schedule_calculator.assemblers.time_assembler import TimeFormatter
from schedule_calculator.assemblers.workday_assembler import WorkDayAssembler
from schedule_calculator.workday_calculator import WorkDayCalculator

__SCHEDULE_CONFIG = {
        "standard": "08:15",
        "short": "07:00",
        "launch": "00:45",
        "short_day": "Friday"
}


def it_should_not_return_none():
    time_formatter = TimeFormatter()
    workday_assembler = WorkDayAssembler(time_formatter)
    assert workday_assembler.get_workday_from_configuration(__SCHEDULE_CONFIG) is not None


def it_should_return_the_expected_type_object():
    time_formatter = TimeFormatter()
    workday_assembler = WorkDayAssembler(time_formatter)
    assert type(workday_assembler.get_workday_from_configuration(__SCHEDULE_CONFIG)) is WorkDayCalculator
