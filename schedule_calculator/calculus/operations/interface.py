import datetime
from abc import ABC, abstractmethod
from typing import Tuple

from schedule_calculator.time.workday import Workday


class Operation(ABC):

    @abstractmethod
    def fulfill(self, work_day: Workday) -> bool:
        raise NotImplementedError

    @abstractmethod
    def calculate(self, work_day: Workday) -> Tuple[datetime.timedelta, datetime.timedelta]:
        raise NotImplementedError
