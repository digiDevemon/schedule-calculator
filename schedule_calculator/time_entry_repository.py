import datetime
import os
import tempfile
from pathlib import Path

from schedule_calculator.assemblers.time_assembler import TimeFormatter


class TimeEntryRepository:
    __TEMP_FILE_NAME = "schedule_calculator_time"

    def __init__(self, time_formatter: TimeFormatter = TimeFormatter()):
        self.time_formatter = time_formatter

    def repository_contains_time(self) -> bool:
        return os.path.isfile(self.__get_temporal_file_path())

    def get_time_entry(self) -> datetime.timedelta:
        saved_time = Path(self.__get_temporal_file_path()).read_text(encoding="utf-8")
        return self.time_formatter.get_delta_from_str(saved_time)

    def save_time_entry(self, time: datetime.timedelta):
        with open(self.__get_temporal_file_path(), "w", encoding="utf-8") as file:
            file.write(self.time_formatter.get_str_from_delta(time))

    def remove_time_entry(self):
        if os.path.isfile(self.__get_temporal_file_path()):
            os.remove(self.__get_temporal_file_path())

    def __get_temporal_file_path(self) -> str:
        return os.path.join(tempfile.gettempdir(), self.__TEMP_FILE_NAME)
