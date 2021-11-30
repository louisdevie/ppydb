class Table:
	def select(self, condition):
		return self

	def order_by(self, column, order='asc'):
		return self

	def project(self, *columns):
		return self