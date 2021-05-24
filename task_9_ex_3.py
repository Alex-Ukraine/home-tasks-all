import re


def get_longest_word(s: str):
    if type(s) is not str:
        raise ValueError
    temp = re.findall(r"[A-Za-z0-9]*", s)
    return sorted(list(temp), key=len, reverse=True)[0]