from ppydb import *

db = new_ppydb('example')

print(db)

table = db.create_table(
	'table',
	Int('id', AutoNum(), PrimaryKey()),
	Str('lastname', NeverEmpty()),
	Str('firstname')  )

print(table)

table.insert_values(
	(None, 'Stickmin', 'Henry'),
	(None, 'Calvin', 'Charles'),
	(None, 'Rose', 'Ellie')  )

print(db.query(table))

query = table.select(Col('l') in 'firstname').sort_by('id', DESC).project('firstname', 'lastname')

print(query.toSQL())

print(db.query(query))