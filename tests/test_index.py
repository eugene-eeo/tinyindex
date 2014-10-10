from tinyindex import Index


def test_index_iter(db):
    idx = Index(db, 'k')
    assert [d['k'] for d in idx] == [1, 2, 3, 4, 5]


def test_index_reversed(db):
    idx = Index(db, 'k', reverse=True)
    assert [d['k'] for d in idx] == [5, 4, 3, 2, 1]


def test_index_multiple(multi_db):
    idx = Index(multi_db, 'k', 't')
    assert [d['t'] for d in idx] == [2, 3, 4, 4, 5]
    assert [d['k'] for d in idx] == [1, 2, 2, 3, 3]


def test_index_slice(db):
    idx = Index(db, 'k')
    assert [d['k'] for d in idx[1:3]] == [2, 3]
    assert idx[0] == {'k': 1}
