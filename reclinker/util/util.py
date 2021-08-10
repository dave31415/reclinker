def check_schema(my_dict, schema):
    assert set(my_dict.keys()) == set(schema.keys())
    for key in my_dict.keys():
        assert isinstance(my_dict[key], schema[key])
