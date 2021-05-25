"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('string', type=str, nargs=1)


def from_roman_numerals(args):
    inp = args.string
    numval = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    sum = 0
    previous = ''
    for char in inp[0]:
        if char in numval.keys():
            if previous == 'I' and char != 'I':
                sum -= 2
            sum += numval[char]
            previous = char
        else:
            raise ValueError
    else:
        return sum


def main():
    args = parser.parse_args()
    print(from_roman_numerals(args))


if __name__ == "__main__":
    main()
