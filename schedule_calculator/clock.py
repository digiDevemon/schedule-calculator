import datetime


class Clock:

    @staticmethod
    def get_today_day() -> str:
        return datetime.date.today().strftime("%A")

    @staticmethod
    def get_delta_now() -> datetime.timedelta:
        instant_now = datetime.datetime.now()

        return datetime.timedelta(hours=instant_now.hour, minutes=instant_now.minute)
