class ScheduleParsingError(Exception):

    def __init__(self):
        super().__init__("Error parsing schedule")
