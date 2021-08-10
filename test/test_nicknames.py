from reclinker.nick_names import get_name_similar_func


def test_name_similarity_func():
    # 10,337 unique pairs of similar names (at last check)
    is_similar = get_name_similar_func()

    # same after processed
    assert is_similar('foo-bar', ' FOO-baR   ')

    # similar
    assert is_similar('David', 'dave')
    assert is_similar('james', 'jim')
    assert is_similar('jim', 'james')
    assert is_similar('jim', 'jimmy')
    assert is_similar('\thelen', 'ellen')
    assert is_similar('winnie', 'winifred   ')
    assert is_similar('susan', 'sue')
    assert is_similar('william', 'bILLY')
    assert is_similar('bess', 'lizzie')
    assert is_similar('vin', 'vincenzo')
    assert is_similar('vin', 'vinny')
    assert is_similar('Lawrence', 'Lonny')
    assert is_similar('lolly', 'delores')
    assert is_similar('kathryn', 'catherine')
    assert is_similar('kathryn', 'cathy')
    assert is_similar('mary', 'margaretta')
    assert is_similar('tori', 'victoria')

    # not similar
    assert not is_similar('david', 'john')
    assert not is_similar('brandon', 'brad')
    assert not is_similar('  susan', 'helen')
