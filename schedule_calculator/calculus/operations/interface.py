import datetime
from abc import ABC, abstractmethod


class Operation(ABC):

    @abstractmethod
    def fulfill(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def calculate(self) -> datetime.timedelta:
        raise NotImplementedError
