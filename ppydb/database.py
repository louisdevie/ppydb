from . import table, exceptions, view


class Database:
    def __init__(self, name):
        self._name = name
        self._tables = list()

    def __repr__(self):
        return f"<{self._name}>"

    def create_table(self, name, *columns):
        new_table = table.Table(name, self, columns)
        self._tables.append(new_table)
        return new_table

    def table(self, table):
        if table._database is not self:
            raise exceptions.QueryError(
                f"can't query a table that doesn't belong to the database "
                f"(tried querying {table} from {self})"
            )

        return view.View.from_table(self, table)

    def insert_values(self, table, *rows):
        pass
