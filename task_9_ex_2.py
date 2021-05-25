import string


def is_palindrome(test_string: str) -> bool:
    if type(test_string) is not str:
        raise ValueError

    test_string = [x for x in test_string if x in string.ascii_letters]

    test_string = ''.join(test_string).lower()

    return ''.join(list(reversed(test_string))) == test_string
