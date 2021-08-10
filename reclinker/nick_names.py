from collections import defaultdict
from reclinker.data_sources.read_resources import ResourceStreams
from reclinker.util.util import proc


def collect_nicknames():
    rs = ResourceStreams()
    stream_names = ['nicknames_1', 'us_census_nicknames',
                    'nicknames_domin', 'nicknames_variations']

    data = defaultdict(set)

    for stream_name in stream_names:
        stream = rs(stream_name)
        for row in stream:
            data[row['name']].add(row['nickname'])

    return data


def create_name_pair_lookup():
    lookup = set()
    nick_name_dict = collect_nicknames()
    for name, nicknames in nick_name_dict.items():
        all = nicknames.copy()
        all.add(name)
        all = list(all)
        for name_1 in all:
            for name_2 in all:
                if name_1 != name_2:
                    lookup.add((name_1, name_2))

    return lookup


def get_name_similar_func():
    lookup = create_name_pair_lookup()

    def func(name_1, name_2):
        n_1 = proc(name_1)
        n_2 = proc(name_2)

        if n_1 == n_2:
            return True

        return (n_1, n_2) in lookup

    return func
