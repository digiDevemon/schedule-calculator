import datetime


class Clock:

    @staticmethod
    def get_today_day() -> str:
        return datetime.date.today().strftime("%A")

    @staticmethod
    def get_current_hour() -> datetime.timedelta:
        time_now = datetime.datetime.now()
        return datetime.timedelta(hours=time_now.hour, minutes=time_now.minute)
