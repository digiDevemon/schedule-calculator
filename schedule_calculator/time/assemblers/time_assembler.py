import datetime


class TimeFormatter:
    HOUR_FORMATTER = "%Y-%m-%dT%H:%M:%SZ"
    DELTA_FORMATTER = "%H:%M"

    def get_delta_from_str(self, time: str) -> datetime.timedelta:
        time_parsed = datetime.datetime.strptime(time, self.DELTA_FORMATTER)
        return datetime.timedelta(hours=time_parsed.hour, minutes=time_parsed.minute)

    @staticmethod
    def get_str_from_delta(time_delta: datetime.timedelta) -> str:
        hours, minutes = time_delta.seconds // 3600, time_delta.seconds // 60 % 60
        return f'{hours:02d}:{minutes:02d}'

    def get_time_from_str(self, time: str) -> datetime.datetime:
        print(time)
        return datetime.datetime.strptime(time, self.HOUR_FORMATTER)

    def get_str_from_time(self, instant: datetime.datetime) -> str:
        return instant.strftime(self.HOUR_FORMATTER)
