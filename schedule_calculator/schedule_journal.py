import datetime

from schedule_calculator.calculus.workday_calculator import WorkDayCalculator
from schedule_calculator.presenter import Presenter
from schedule_calculator.time.assemblers.work_calendar_assembler import WorkCalendarAssembler
from schedule_calculator.time.assemblers.time_formatter import TimeFormatter
from schedule_calculator.time.assemblers.workday_assembler import WorkDayAssembler
from schedule_calculator.time.clock import Clock
from schedule_calculator.time.repository.time_entry_repository import TimeEntryRepository, create_time_entry_repository


class ScheduleJournal:

    def __init__(self,
                 work_day_calculator: WorkDayCalculator,
                 time_entry_repository: TimeEntryRepository,
                 presenter: Presenter,
                 clock: Clock):
        self.time_entry_repository = time_entry_repository
        self.clock = clock
        self.work_day_calculator = work_day_calculator
        self.workday_assembler = WorkDayAssembler(clock)
        self.presenter = presenter
        self.zero_time_vector = datetime.timedelta(hours=0)

    def init(self) -> None:
        current_hour = self.clock.get_current_time()
        self.time_entry_repository.save_time_entry(current_hour)

    def check(self) -> None:
        started_time = self.time_entry_repository.get_time_entry()
        workday = self.workday_assembler.get_workday(started_time)

        worked_hours, expected_hours = self.work_day_calculator.calculate_worked_time(workday)

        if worked_hours > expected_hours:
            extra_hours = self.work_day_calculator.calculate_extra_time_today(workday)
            self.presenter.present_extra_hours(extra_hours)
            return

        self.presenter.present_workday(worked_hours, expected_hours)


def create_schedule_journal(configuration: dict) -> ScheduleJournal:
    time_formatter = TimeFormatter()
    clock = Clock()

    work_calendar = WorkCalendarAssembler(time_formatter, clock).get_work_calendar(configuration["work_calendar"])
    time_entry_repository = create_time_entry_repository()
    presenter = Presenter()

    return ScheduleJournal(WorkDayCalculator(work_calendar), time_entry_repository, presenter, clock)


def create_schedule_journal_for_testing(configuration: dict, time_entry_repository: TimeEntryRepository,
                                        clock: Clock, presenter: Presenter) -> ScheduleJournal:
    time_formatter = TimeFormatter()
    work_calendar = WorkCalendarAssembler(time_formatter, clock).get_work_calendar(configuration["work_calendar"])

    return ScheduleJournal(WorkDayCalculator(work_calendar), time_entry_repository, presenter, clock)
