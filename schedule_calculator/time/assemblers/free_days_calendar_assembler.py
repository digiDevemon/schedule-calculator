from holidays import country_holidays, HolidayBase


class FreeDaysCalendarAssembler:

    @staticmethod
    def get_calendar_from_str(country_code: str, year: int) -> HolidayBase:
        country_code_tokens = country_code.split("-")

        if len(country_code_tokens) == 2:
            return country_holidays(country_code_tokens[0], subdiv=country_code_tokens[1], years=year)

        return country_holidays(country_code_tokens[0], years=year)
