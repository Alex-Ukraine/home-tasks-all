"""
Implement a function `split_by_index(string: str, indexes: List[int]) -> List[str]`
which splits the `string` by indexes specified in `indexes`. 
Only positive index, larger than previous in list is considered valid.
Invalid indexes must be ignored.

Examples:
```python
>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 8, -4, 0, "u", 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]
```
"""


def split_by_index(string, indexes):
    last = 0
    res = []

    for index in indexes:
        if isinstance(index, int) and index > last:
            res.append(string[last:index])
            last = index
    if last < len(string):
        res.append(string[last:])
    return res

# print(split_by_index("pythoniscool,isn'tit?", [6, 8, 8, -4, 0, "u", 12, 13, 18]))
# split_by_index("no luck", [42])
# split_by_index("no luck", [])
# print(split_by_index("no luck", [2,7]))
