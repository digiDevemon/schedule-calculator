import datetime


class TimeFormatter:
    HOUR_FORMATTER = "%H:%M"

    def get_delta_from_str(self, time: str) -> datetime.timedelta:
        time_parsed = datetime.datetime.strptime(time, self.HOUR_FORMATTER)
        return datetime.timedelta(hours=time_parsed.hour, minutes=time_parsed.minute)

    @staticmethod
    def get_str_from_delta(time_delta: datetime.timedelta) -> str:
        hours, minutes = time_delta.seconds // 3600, time_delta.seconds // 60 % 60
        return f'{hours:02d}:{minutes:02d}'
