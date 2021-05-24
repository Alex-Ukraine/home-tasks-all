"""01-Task1-Task1
Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. The type of operator and
data are set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py 1 * 2

Notes:
For other operations need to raise NotImplementedError.
Do not dynamically execute your code (for example, using exec()).
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse
import operator

parser = argparse.ArgumentParser()
parser.add_argument('first', type=float, nargs=1)
parser.add_argument('sign', type=str, nargs=1)
parser.add_argument('second', type=float, nargs=1)


def calculate(args):
    first = args.first[0]
    sign = args.sign[0]
    second = args.second[0]

    operators = {
                '+' : operator.add,
                '-' : operator.sub,
                '*' : operator.mul,
                '/' : operator.truediv,
                  }

    if sign not in ['+', '-', '*', '/']:
        raise NotImplementedError
    return operators[sign](first, second)


def main():
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()
