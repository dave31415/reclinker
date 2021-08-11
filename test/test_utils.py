from reclinker.util.util import proc, take, truncate_stream


def test_proc():
    assert proc('hello there') == 'hello there'
    assert proc(' Hello   TheRe 1\t\n') == 'hello   there 1'


def test_take():
    n = 22
    stream = (i for i in range(n))

    # first 10
    data_0 = take(stream, 10)
    assert len(data_0) == 10
    assert data_0 == list(range(10))

    # next 10
    data_1 = take(stream, 10)
    assert len(data_1) == 10
    assert data_1 == list(range(10, 20))

    # last two
    data_2 = take(stream, 10)
    assert data_2 == [20, 21]

    # this should still work and just return empty list
    data_3 = take(stream, 5)
    assert data_3 == []


def test_truncate_stream():
    stream = iter(range(100))

    truncated_stream = truncate_stream(stream, 10)
    my_list = list(truncated_stream)
    assert my_list == list(range(10))
