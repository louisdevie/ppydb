from ppydb import *

db = new_ppydb('example')

db.create_table(
	'table',
	Int('id', AutoNum(), PrimaryKey()),
	Str('lastname', NeverEmpty()),
	Str('firstname')  )

db.insert_values(
	'table',
	(None, 'Stickmin', 'Henry'),
	(None, 'Calvin', 'Charles'),
	(None, 'Rose', 'Ellie')  )

print(
	db.table('table')
	.select('l' in 'firstname')
	.order_by('id', 'desc')
	.project('firstname', 'lastname')  )