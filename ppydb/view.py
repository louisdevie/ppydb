from . import _predicates, _operations


class View:
    @classmethod
    def from_table(cls, db, table):
        view = cls()
        view._operation = _operations.BaseTable(table, db)
        view._source = None
        return view

    def select(self, predicate):
        if not isinstance(predicate, _predicates.Predicate):
            raise TypeError(f"expected predicate, got '{type(predicate).__name__}'")

        view = type(self)()
        view._operation = _operations.Selection(predicate)
        view._source = self
        return view
