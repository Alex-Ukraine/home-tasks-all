import collections
import string


def count_letters(some_string: str) -> dict:
    if type(some_string) is not str:
        raise TypeError
    res = [x for x in some_string if x in string.ascii_letters]
    return dict(collections.Counter(res))
