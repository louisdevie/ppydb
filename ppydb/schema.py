from .table import Table

class Schema:
	def __init__(self, provider):
		pass

	def create_table(self, table_name, *columns):
		pass

	def insert_values(self, table_name, *values):
		pass

	def table(self, table_name):
		return Table()