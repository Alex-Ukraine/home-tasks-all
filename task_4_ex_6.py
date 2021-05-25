"""
Task04_6

Implement a function get_longest_word(s: str) -> str which returns the longest word in the given string.
The word can contain any symbols except whitespaces (`,\n,\tand so on).
If there are multiple longest words in the string with a same length return the word that occurs first.

Example: get_longest_word('Python is simple and effective!')
         #output: 'effective!'
         get_longest_word('Any pythonista like namespaces a lot.')
         #output: 'pythonista'

Note:
Raise ValueError in case of wrong data type
Usage of 're' library is prohibited
"""


def get_longest_word(str_to_parse: str) -> str:
    if not isinstance(str_to_parse, str):
        raise ValueError
    last = 0
    res = ''
    for index, char in enumerate(str_to_parse):
        if char == ' ':
            if len(str_to_parse[last:index]) > len(res):
                res = str_to_parse[last:index]
            last = index + 1
    if len(str_to_parse[last:]) > len(res):
        res = str_to_parse[last:]
    return res

# print(get_longest_word('Python is simple and effective!'))
# print(get_longest_word('Any pythonista like namespaces a lot.'))
