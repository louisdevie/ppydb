class Condition:
	pass

class Col:
	def __init__(self, name):
		self._name = name

	# Unary operators and functions
	def __pos__(self): pass						# To get called for unary positive e.g. +someobject.
	def __neg__(self): pass						# To get called for unary negative e.g. -someobject.
	def __abs__(self): pass						# To get called by built-in abs() function.
	def __invert__(self): pass					# To get called for inversion using the ~ operator.
	def __round__(self,n): pass					# To get called by built-in round() function.
	def __floor__(self): pass					# To get called by built-in math.floor() function.
	def __ceil__(self): pass					# To get called by built-in math.ceil() function.
	def __trunc__(self): pass					# To get called by built-in math.trunc() function.

	# Type Conversion Magic Methods
	def __int__(self): pass						# To get called by built-int int() method to convert a type to an int.
	def __float__(self): pass					# To get called by built-int float() method to convert a type to float.
	def __complex__(self): pass					# To get called by built-int complex() method to convert a type to complex.
	def __oct__(self): pass						# To get called by built-int oct() method to convert a type to octal.
	def __hex__(self): pass						# To get called by built-int hex() method to convert a type to hexadecimal.
	def __index__(self): pass					# To get called on type conversion to an int when the object is used in a slice expression.
	def __trunc__(self): pass					# To get called from math.trunc() method.

	# String Magic Methods
	def __str__(self): pass						# To get called by built-int str() method to return a string representation of a type.
	def __repr__(self): pass					# To get called by built-int repr() method to return a machine readable representation of a type.
	def __unicode__(self): pass					# To get called by built-int unicode() method to return an unicode string of a type.
	def __format__(self, formatstr): pass		# To get called by built-int string.format() method to return a new style of string.
	def __hash__(self): pass					# To get called by built-int hash() method to return an integer.
	def __nonzero__(self): pass					# To get called by built-int bool() method to return True or False.
	def __dir__(self): pass						# To get called by built-int dir() method to return a list of attributes of a class.
	def __sizeof__(self): pass					# To get called by built-int sys.getsizeof() method to return the size of an object.

	# Operator Magic Methods
	def __add__(self, other): pass				# To get called on add operation using + operator
	def __sub__(self, other): pass				# To get called on subtraction operation using - operator.
	def __mul__(self, other): pass				# To get called on multiplication operation using * operator.
	def __floordiv__(self, other): pass			# To get called on floor division operation using // operator.
	def __truediv__(self, other): pass			# To get called on division operation using / operator.
	def __mod__(self, other): pass				# To get called on modulo operation using % operator.
	def __pow__(self, other[, modulo]): pass	# To get called on calculating the power using ** operator.
	def __lt__(self, other): pass				# To get called on comparison using < operator.
	def __le__(self, other): pass				# To get called on comparison using <= operator.
	def __eq__(self, other): pass				# To get called on comparison using == operator.
	def __ne__(self, other): pass				# To get called on comparison using != operator.
	def __ge__(self, other): pass				# To get called on comparison using >= operator.