class Table:
    def __init__(self, name, database, columns):
        self._name = name
        self._database = database
        self._columns = {col._name: col for col in columns}

    def __str__(self):
        return f"<{self._database._name}:{self._name}>"

    def __getattr__(self, attr):
        if attr.startswith("_"):
            return object.__getattr__(self, attr)
        else:
            return self._columns[attr]
