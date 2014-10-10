from random import shuffle
from tinydb import TinyDB
from tinydb.storages import MemoryStorage
from pytest import fixture

@fixture
def db():
    db = TinyDB(storage=MemoryStorage).table()
    db.insert_multiple([
        {'k': i} for i in [4,2,1,3,5]
    ])
    return db


@fixture
def multi_db():
    db = TinyDB(storage=MemoryStorage).table()
    pairs = [
        [1, 2],
        [2, 3],
        [2, 4],
        [3, 4],
        [3, 5],
    ]
    shuffle(pairs)
    db.insert_multiple([
        {'k': k, 't': t} for k, t in pairs
    ])
    return db
