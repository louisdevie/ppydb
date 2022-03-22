class OperationABC:
    pass


class BaseTable(OperationABC):
    def __init__(self, table, db):
        self.table = table
        self.database = db


class Selection(OperationABC):
    def __init__(self, pred):
        self.predicate = pred
