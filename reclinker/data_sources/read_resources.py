from csv import DictReader
from reclinker.data_sources.paths import get_file_names
from reclinker.util.util import proc


def stream_nick_names_1():
    filename = get_file_names()['nick_names_1']
    raw_stream = DictReader(open(filename, 'r'))
    stream = ({'name': proc(row['name']), 'nickname': proc(row['nickname'])} for row in raw_stream)
    return stream


def stream_us_census_nick_names():
    filename = get_file_names()['us_census_nicknames']
    fp = open(filename, 'r')
    for line in fp:
        if line.startswith('#'):
            continue
        row = line.split()
        assert len(row) == 3
        row_dict = {'name': proc(row[1]),
                    'nickname': proc(row[0]),
                    'substitution_likelihood': float(proc(row[2]))}

        yield row_dict


def stream_domin():
    filename = get_file_names()['nicknames_domin']
    fp = open(filename, 'r')

    for line in fp:
        fields = line.split()
        actual_name = proc(fields[0])
        nicknames = [proc(n) for n in fields[1:]]
        for nickname in nicknames:
            yield {'name': actual_name, "nickname": nickname}

    fp.close()


def stream_variations():
    filename = get_file_names()['nicknames_variations']
    fp = open(filename, 'r')

    for line in fp:
        fields = line.split(',')
        actual_name = proc(fields[0])
        nicknames = [proc(n) for n in fields[1:]]
        for nickname in nicknames:
            yield {'name': actual_name, "nickname": nickname}

    fp.close()


class ResourceStreams:
    """
    This class is the ONLY point of coupling between the core application logic
    and it's required data input. This abstraction allows for multiple implementations
    using different data storage and streaming mechanisms.
    """

    def __init__(self):
        pass

    def __call__(self, stream_name):
        if stream_name == 'nicknames_1':
            return stream_nick_names_1()

        elif stream_name == 'us_census_nicknames':
            return stream_us_census_nick_names()

        elif stream_name == 'nicknames_domin':
            return stream_domin()

        elif stream_name == 'nicknames_variations':
            return stream_variations()

        else:
            raise ValueError('steam_name: %s unknown' % stream_name)
