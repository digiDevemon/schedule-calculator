from holidays import country_holidays, HolidayBase


class HolidayCalendarAssembler:

    @staticmethod
    def get_calendar_from_str(_place: str) -> HolidayBase:
        return country_holidays("UK")
