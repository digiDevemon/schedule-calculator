import datetime

from schedule_calculator.time.assemblers.time_assembler import TimeFormatter
from schedule_calculator.time.assemblers.schedule_assembler import ScheduleAssembler
from schedule_calculator.time.clock import Clock
from schedule_calculator.time_entry_repository import TimeEntryRepository, create_time_entry_repository
from schedule_calculator.calculus.workday_calculator import WorkDayCalculator


class ScheduleJournal:

    def __init__(self,
                 work_day_calculator: WorkDayCalculator,
                 time_entry_repository: TimeEntryRepository,
                 time_formatter: TimeFormatter,
                 clock: Clock):
        self.time_entry_repository = time_entry_repository
        self.clock = clock
        self.work_day_calculator = work_day_calculator
        self.time_formatter = time_formatter
        self.zero_time_vector = datetime.timedelta(hours=0)

    def init(self):
        current_hour = self.clock.get_current_time()
        self.time_entry_repository.save_time_entry(current_hour)

    def check(self):
        started_time = self.time_entry_repository.get_time_entry()
        worked_hours, expected_hours = self.work_day_calculator.calculate_worked_time(self.clock.get_today_day(),
                                                                                      started_time,
                                                                                      self.clock.get_current_time())
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
    return ScheduleJournal(WorkDayCalculator(schedule), time_entry_repository, time_formatter, clock)


def create_schedule_journal_with_repository(configuration, time_entry_repository) -> ScheduleJournal:
    time_formatter = TimeFormatter()
    schedule = ScheduleAssembler(time_formatter).get_schedule(configuration["schedule"])
    clock = Clock()
    return ScheduleJournal(WorkDayCalculator(schedule), time_entry_repository, time_formatter, clock)


def create_schedule_journal_with_repository_and_clock(configuration: dict, time_entry_repository: TimeEntryRepository,
                                                      clock: Clock) -> ScheduleJournal:
    time_formatter = TimeFormatter()
    schedule = ScheduleAssembler(time_formatter).get_schedule(configuration["schedule"])
    return ScheduleJournal(WorkDayCalculator(schedule), time_entry_repository, time_formatter, clock)
