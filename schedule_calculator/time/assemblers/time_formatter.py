import datetime
import re
from typing import Match

from schedule_calculator.time.exceptions.schedule_parsing import ScheduleParsingError


class TimeFormatter:
    HOUR_FORMATTER = "%Y-%m-%dT%H:%M:%SZ"
    DELTA_FORMATTER = "%H:%M"
    DATE_PATTERN = r'^(\d{1,2})-(\d{1,2})$'

    def get_delta_from_str(self, time: str) -> datetime.timedelta:
        time_parsed = datetime.datetime.strptime(time, self.DELTA_FORMATTER)
        return datetime.timedelta(hours=time_parsed.hour, minutes=time_parsed.minute)

    @staticmethod
    def get_str_from_delta(time_delta: datetime.timedelta) -> str:
        hours, minutes = time_delta.seconds // 3600, time_delta.seconds // 60 % 60
        return f'{hours:02d}:{minutes:02d}'

    def get_time_from_str(self, time: str) -> datetime.datetime:
        return datetime.datetime.strptime(time, self.HOUR_FORMATTER)

    def get_str_from_time(self, instant: datetime.datetime) -> str:
        return instant.strftime(self.HOUR_FORMATTER)

    def get_date_from_str(self, literal_date: str) -> datetime.date:
        date_match = self.__match_date_expression(literal_date)

        month = int(date_match.group(1))
        day = int(date_match.group(2))

        return datetime.date(year=datetime.datetime.now().year, month=month, day=day)

    def __match_date_expression(self, literal_date: str) -> Match[str]:
        date_match = re.search(self.DATE_PATTERN, literal_date)
        if not date_match:
            raise ScheduleParsingError
        return date_match
