def proc(string):
    return string.lower().strip()


def check_schema(my_dict, schema):
    assert set(my_dict.keys()) == set(schema.keys())
    for key in my_dict.keys():
        assert isinstance(my_dict[key], schema[key])


def take(stream, n):
    results = []
    for i, item in enumerate(stream):
        results.append(item)
        if i == n - 1:
            break

    return results


def truncate_stream(stream, n_max):
    for n, item in enumerate(stream):
        yield item
        if n == n_max - 1:
            break
