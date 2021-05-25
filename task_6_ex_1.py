from string import ascii_lowercase


def combine_dicts(*args):
    res = {}
    for d in args:
        for k in d:
            if k not in list(ascii_lowercase):
                raise KeyError
            if type(d[k]) is not int:
                raise ValueError
            res[k] = res.get(k, 0) + d.get(k, 0)
    return res
