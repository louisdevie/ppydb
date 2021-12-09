from .base import Schema, BaseProvider

def new_ppydb(schema_name):
	return Schema(schema_name, PPyDBProvider())

class PPyDBProvider (BaseProvider):
	pass