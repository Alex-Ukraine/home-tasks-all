import string
from functools import reduce


def check(strings):
    """check type function"""
    for x in strings:
        if type(x) is not str:
            raise TypeError


def chars_in_all(*strings):
    """characters that appear in all strings"""
    check(strings)
    return reduce(lambda x, y: set(x).intersection(set(y)), strings)


def chars_in_one(*strings):
    """characters that appear in at least one string"""
    check(strings)
    return reduce(lambda x, y: set(x).union(set(y)), strings)


def chars_in_two(*strings):
    """characters that appear at least in two strings"""
    check(strings)
    if len(strings)<2:
        raise ValueError
    res = set()
    for index, x in enumerate(strings):
        others = strings[ :index ] + strings[ index + 1: ]
        res = res.union(set(x).intersection(chars_in_one(*others)))
    return res


def not_used_chars(*strings):
    """characters of alphabet, that were not used in any string
        Note: use `string.ascii_lowercase` for list of alphabet letters"""
    check(strings)
    temp = chars_in_one(*strings)
    return {x for x in string.ascii_lowercase if x not in temp}
