class _Keyword:
	def __init__(self, name):
		self._name = name

	def __repr__(self):
		return self._name

	def __eq__(self, other):
		return self is other

ASC = ASCENDING = _Keyword('ASCENDING')
DESC = DESCENDING = _Keyword('DESCENDING')

KEEPOLD = _Keyword('KEEPOLD')