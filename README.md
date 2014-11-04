tinyindex
=========

Document indexing for TinyDB. Basically ensures
deterministic (as long as there aren't any changes
to the table) yielding of documents. A very trivial
example usage:

```python
from tinyindex import Index

idx = Index(table, *keys)
for item in idx:
   ...

idx[0]
idx[0:4]
```
