"""
Task 04-Task 1.8
Implement a function which takes a list of elements and returns a list of tuples containing pairs of this elements.
Pairs should be formed as in the example. If there is only one element in the list return `None`
instead.
Using zip() is prohibited.

Examples:
>>> get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]

>>> get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

>>> get_pairs([1])
None
"""


def get_pairs(lst: list) -> list:
    res = []
    last = None
    if len(lst) > 1:
        for item in lst:
            if last:
                res.append((last, item))
            last = item
        return res
    else:
        return None


print(get_pairs(['need', 'to', 'sleep', 'more']))
