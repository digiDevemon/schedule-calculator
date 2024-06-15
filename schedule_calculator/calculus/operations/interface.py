import datetime
from abc import ABC, abstractmethod
from typing import Tuple

from schedule_calculator.time.workday import Workday


class Operation(ABC):

    @abstractmethod
    def fulfill(self, work_day: Workday) -> bool:
        raise NotImplementedError

    @abstractmethod
    def calculate_worked_time(self, work_day: Workday) -> Tuple[datetime.timedelta, datetime.timedelta]:
        raise NotImplementedError

    @abstractmethod
    def calculate_extra_time(self, work_day: Workday) -> datetime.timedelta:
        raise NotImplementedError
