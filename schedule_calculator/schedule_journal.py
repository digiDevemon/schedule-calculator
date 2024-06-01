import logging
import sys
from logging import Logger

from schedule_calculator.assemblers.time_assembler import TimeFormatter
from schedule_calculator.assemblers.workday_assembler import WorkDayAssembler
from schedule_calculator.clock import Clock
from schedule_calculator.time_entry_repository import TimeEntryRepository
from schedule_calculator.workday_calculator import WorkDayCalculator


class ScheduleJournal:

    def __init__(self,
                 work_day_calculator: WorkDayCalculator,
                 time_entry_repository: TimeEntryRepository,
                 clock: Clock):
        self.time_entry_repository = time_entry_repository
        self.clock = clock
        self.logger = self.__get_logger()
        self.work_day_calculator = work_day_calculator

    def init(self):
        current_hour = self.clock.get_current_hour()
        self.time_entry_repository.save_time_entry(current_hour)

    def check(self):
        started_time = self.time_entry_repository.get_time_entry()
        worked_hours, expected_hours = self.work_day_calculator.calculate_worked_time(started_time)
        self.logger.info("You have worked %s. Today you have to work %s.", worked_hours, expected_hours)

    @staticmethod
    def __get_logger() -> Logger:
        log = logging.getLogger("my-logger")
        log.setLevel(logging.INFO)
        log.addHandler(logging.StreamHandler(sys.stdout))
        return log


def create_schedule_journal(configuration):
    time_formatter = TimeFormatter()
    work_day_calculator = WorkDayAssembler(time_formatter).get_workday_from_configuration(configuration)
    time_entry_repository = TimeEntryRepository(time_formatter)
    clock = Clock()
    return ScheduleJournal(work_day_calculator, time_entry_repository, clock)


def create_schedule_journal_with_repository(configuration, time_entry_repository):
    time_formatter = TimeFormatter()
    work_day_calculator = WorkDayAssembler(time_formatter).get_workday_from_configuration(configuration)
    clock = Clock()
    return ScheduleJournal(work_day_calculator, time_entry_repository, clock)
