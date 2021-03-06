import pytest
from reclinker.util.util import check_schema
from reclinker.data_sources.read_resources import ResourceStreams


rs = ResourceStreams()


def test_resource_streams_nick_names_1():
    nick_name_1 = rs('nicknames_1')
    first = next(nick_name_1)
    schema_expected = {'name': str, 'nickname': str}
    check_schema(first, schema_expected)


def test_resource_streams_us_census_nicknames():
    usc_nick_names = rs('us_census_nicknames')
    first = next(usc_nick_names)
    schema_expected = {'name': str, 'nickname': str, 'substitution_likelihood': float}
    check_schema(first, schema_expected)


def test_resource_streams_nicknames_domin():
    nick_names = rs('nicknames_domin')
    first = next(nick_names)
    schema_expected = {'name': str, 'nickname': str}
    check_schema(first, schema_expected)


def test_resource_streams_nicknames_variations():
    nick_names = rs('nicknames_variations')
    first = next(nick_names)
    schema_expected = {'name': str, 'nickname': str}
    check_schema(first, schema_expected)


def test_stream_unknown():
    with pytest.raises(ValueError):
        rs('this_stream_does_not_exist_dude')
