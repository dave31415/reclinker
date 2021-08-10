from reclinker.util.util import proc


def test_proc():
    assert proc('hello there') == 'hello there'
    assert proc(' Hello   TheRe 1\t\n') == 'hello   there 1'
