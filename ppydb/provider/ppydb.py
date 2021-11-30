from .base import Schema, BaseProvider

def new_ppydb(path):
	return Schema(PPyDBProvider())

class PPyDBProvider (BaseProvider):
	pass