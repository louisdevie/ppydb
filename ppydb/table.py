class Table:
	def __init__(self, name, schema=None, initial_cols=tuple()):
		self._name = name
		self._schema = schema

	def __str__(self):
		if self._schema:
			return f'<{self._schema._name}:{self._name}>'
		else:
			return f'<$:{self._name}>'

	@property
	def name(self):
		return self._name

	def insert_values(self, *values):
		pass