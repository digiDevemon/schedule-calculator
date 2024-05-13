import datetime


class TimeFormatter:
    HOUR_FORMATTER = "%H:%M"

    def get_delta_from_str(self, time: str) -> datetime.timedelta:
        time_parsed = datetime.datetime.strptime(time, self.HOUR_FORMATTER)
        return datetime.timedelta(hours=time_parsed.hour, minutes=time_parsed.minute)
