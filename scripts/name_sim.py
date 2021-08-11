from reclinker.nick_names import get_name_similar_func


def main(*args):
    is_similar = get_name_similar_func()
    print(is_similar(*args))
