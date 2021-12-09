from .table import Table
from .keywords import KEEPOLD

class Schema:
	def __init__(self, name, provider):
		self._name = name
		self._tables = dict()

	def __str__(self):
		return f'<{self._name}>'

	@property
	def name(self):
		return self._name

	def create_table(self, table_name, *columns):
		if table_name in self._tables:
			raise ValueError(f'<{self._name}:{table_name}> already exists')

		new = Table(schema=self, name=table_name, initial_cols=columns)
		self._tables[table_name] = new
		return new

	def edit_table(self, table_name, *args, **kwargs):
		if not table_name in self._tables:
			raise ValueError(f'<{self._name}:{table_name}> doesn\'t exists')

		self._tables[table_name].edit(*args, **kwargs)

	def remove_table(self, table_name, *args, **kwargs):
		if not table_name in self._tables:
			raise ValueError(f'<{self._name}:{table_name}> doesn\'t exists')

		self._tables[table_name].remove(*args, **kwargs)		

	def insert_values(self, table_name, *args, **kwargs):
		pass