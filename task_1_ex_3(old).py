""" Write a Python-script that determines whether the input string is the correct entry for the
'formula' according EBNF syntax (without using regular expressions).
Formula = Number | (Formula Sign Formula)
Sign = '+' | '-'
Number = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Input: string
Result: (True / False, The result value / None)

Example,
user_input = '1+2+4-2+5-1' result = (True, 9)
user_input = '123' result = (True, 123)
user_input = 'hello+12' result = (False, None)
user_input = '2++12--3' result = (False, None)
user_input = '' result = (False, None)

Example how to call the script from CLI:
python task_1_ex_3.py 1+5-2

Hint: use argparse module for parsing arguments from CLI
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('expression', nargs='+')
operations = ['+', '-']


def check_formula(args):
    try:
        expression = args.expression
        # базовый случай, только одна цифра
        if (len(expression) == 1) and (expression[0].isdigit()):
            return (True, int(expression[0]))
        else:
            n = ''

            # 1 исключение оперторы по краям
            if (expression[0] in operations) or (expression[-1] in operations):
                raise NotImplementedError
            for m in expression:
                if (m.isdigit()) or (m in operations):
                    # 2 исключение числа подряд
                    if (m.isdigit()) and (n.isdigit()):
                        raise NotImplementedError
                    # 3 исключение знаки подряд
                    elif (m in operations) and (n in operations):
                        raise NotImplementedError
                    else:
                        n = m
                else:
                    # 4 исключение аргумент не + ни - ни цифра
                    raise NotImplementedError
            return (True, eval(''.join(expression)))

    except:
        return (False, None)


def main():
    args = parser.parse_args()
    print(check_formula(args))


if __name__ == '__main__':
    main()
