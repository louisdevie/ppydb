class Predicate:
    pass


class Contains:
    def __init__(self, constant, column):
        self._constant = constant
        self._column = column
