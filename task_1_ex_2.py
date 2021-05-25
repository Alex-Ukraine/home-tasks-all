"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse
import operator
import math

parser = argparse.ArgumentParser()
parser.add_argument('expression', nargs='+')


def calculate(args):
    if args.expression[0] not in (dir(math) + dir(operator)):
        raise NotImplementedError
    try:
        string = 'math.' + args.expression[0] + '(' + ', '.join(args.expression[1:]) + ')'
        return eval(string)
    except AttributeError:
        try:
            string = 'operator.' + args.expression[0] + '(' + ', '.join(args.expression[1:]) + ')'
            return eval(string)
        except:
            raise AttributeError


def main():
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()
