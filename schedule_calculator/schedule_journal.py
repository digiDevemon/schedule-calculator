import datetime

from schedule_calculator.calculus.workday_calculator import WorkDayCalculator
from schedule_calculator.time.assemblers.schedule_assembler import ScheduleAssembler
from schedule_calculator.time.assemblers.time_assembler import TimeFormatter
from schedule_calculator.time.assemblers.workday_assembler import WorkDayAssembler
from schedule_calculator.time.clock import Clock
from schedule_calculator.time_entry_repository import TimeEntryRepository, create_time_entry_repository


class ScheduleJournal:

    def __init__(self,
                 work_day_calculator: WorkDayCalculator,
                 time_entry_repository: TimeEntryRepository,
                 workday_assembler: WorkDayAssembler,
                 clock: Clock):
        self.time_entry_repository = time_entry_repository
        self.clock = clock
        self.work_day_calculator = work_day_calculator
        self.workday_assembler = workday_assembler
        self.time_formatter = TimeFormatter()
        self.zero_time_vector = datetime.timedelta(hours=0)

    def init(self):
        current_hour = self.clock.get_current_time()
        self.time_entry_repository.save_time_entry(current_hour)

    def check(self):
        started_time = self.time_entry_repository.get_time_entry()

        worked_hours, expected_hours = self.work_day_calculator.calculate_worked_time(
            self.workday_assembler.get_workday(started_time))

        if worked_hours < self.zero_time_vector:
            worked_hours = datetime.timedelta(hours=0)

        print(
            f"You have worked {self.time_formatter.get_str_from_delta(worked_hours)}. "
            f"Today you have to work {self.time_formatter.get_str_from_delta(expected_hours)}.")


def create_schedule_journal(configuration: dict) -> ScheduleJournal:
    time_formatter = TimeFormatter()
    schedule = ScheduleAssembler(time_formatter).get_schedule(configuration["schedule"])
    time_entry_repository = create_time_entry_repository()
    clock = Clock()
    workday_assembler = WorkDayAssembler(clock)

    return ScheduleJournal(WorkDayCalculator(schedule), time_entry_repository, workday_assembler, clock)


def create_schedule_journal_with_repository(configuration, time_entry_repository) -> ScheduleJournal:
    time_formatter = TimeFormatter()
    schedule = ScheduleAssembler(time_formatter).get_schedule(configuration["schedule"])
    clock = Clock()
    workday_assembler = WorkDayAssembler(clock)

    return ScheduleJournal(WorkDayCalculator(schedule), time_entry_repository, workday_assembler, clock)


def create_schedule_journal_with_repository_and_clock(configuration: dict, time_entry_repository: TimeEntryRepository,
                                                      clock: Clock) -> ScheduleJournal:
    time_formatter = TimeFormatter()
    schedule = ScheduleAssembler(time_formatter).get_schedule(configuration["schedule"])
    workday_assembler = WorkDayAssembler(clock)

    return ScheduleJournal(WorkDayCalculator(schedule), time_entry_repository, workday_assembler, clock)
