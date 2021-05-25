"""
For a positive integer n calculate the result value, which is equal to the sum
of the odd numbers of n.

Example,
n = 1234 result = 4
n = 246 result = 0

Write it as function.

Note:
Raise TypeError in case of wrong data type or negative integer;
Use of 'functools' module is prohibited, you just need simple for loop.
"""


def sum_odd_numbers(n: int) -> int:
    sum = 0
    if not ((type(n) is int) and n > 0):
        raise TypeError
    for char in str(n):
        if int(char) % 2 == 1:
            sum += int(char)
    return sum

# print(sum_odd_numbers(True))
