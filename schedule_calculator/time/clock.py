import datetime


class Clock:

    @staticmethod
    def get_today_day() -> str:
        return datetime.date.today().strftime("%A")

    @staticmethod
    def get_current_time() -> datetime.datetime:
        return datetime.datetime.now()

    @staticmethod
    def get_current_date() -> datetime.date:
        return datetime.date.today()
