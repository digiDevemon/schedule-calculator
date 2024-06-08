class UnknownOperationDay(Exception):

    def __init__(self):
        super().__init__("Not known operation")
