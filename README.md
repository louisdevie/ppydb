[![PyPI](https://img.shields.io/pypi/v/ppydb)](https://pypi.org/project/ppydb/)
[![Documentation Status](https://readthedocs.org/projects/ppydb/badge/?version=latest)](https://ppydb.readthedocs.io/en/latest/?badge=latest)
[![MIT license](https://img.shields.io/badge/license-MIT-yellowgreen)](https://github.com/louisdevie/ezcli/blob/main/LICENSE)
[![Tests](https://github.com/louisdevie/ppydb/actions/workflows/coverage.yml/badge.svg)](https://github.com/louisdevie/ppydb/actions/workflows/coverage.yml)
[![codecov](https://codecov.io/gh/louisdevie/ppydb/branch/main/graph/badge.svg)](https://codecov.io/gh/louisdevie/ppydb)
[![code quality](https://img.shields.io/badge/code_quality-terrible-critical)](https://github.com/louisdevie/ezcli)
# ![logo](ppydb_logo_flat.svg)

## Demo
```python

from ppydb import *

db = new_ppydb('example')

table = db.create_table(
	'table',
	Int('id', AutoNum(), PrimaryKey()),
	Str('lastname', NeverEmpty()),
	Str('firstname')  )

table.insert_values(
	(None, 'Stickmin', 'Henry'),
	(None, 'Calvin', 'Charles'),
	(None, 'Rose', 'Ellie')  )

query = table.select(Col('l') in 'firstname').sort_by('id', DESC).project('firstname', 'lastname')

print(query.toSQL())

print(db.query(query))
```
