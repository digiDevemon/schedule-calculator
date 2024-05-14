import datetime


class Clock:

    @staticmethod
    def get_today_day() -> str:
        return datetime.date.today().strftime("%A")
