from reclinker.data_sources.paths import get_file_names


def test_paths():
    file_names = get_file_names()
    # assert the keys exactly so don't end up with unused files etc
    assert set(file_names.keys()) == {'nick_names_1',
                                      'us_census_nicknames',
                                      'nicknames_domin',
                                      'nicknames_variations'}
