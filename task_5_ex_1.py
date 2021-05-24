"""
Write 2 functions:
1. Function 'is_sorted', determining whether a given list of integer values of arbitrary length
is sorted in a given order (the order is set up by enum value SortOrder).
List and sort order are passed by parameters. Function does not change the array, it returns
boolean value.

2. Function 'transform', replacing the value of each element of an integer list with the sum
of this element value and its index, only if the given list is sorted in the given order
(the order is set up by enum value SortOrder). List and sort order are passed by parameters.
To check, if the array is sorted, the function 'is_sorted' is called.

Example for 'transform' function,
For [5, 17, 24, 88, 33, 2] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “descending” sort order the values in the array are changing to [15, 11, 5]

Note:
Raise TypeError in case of wrong function arguments data type;
"""
#class Enum:
#    pass

from enum import Enum
from typing import List


class SortOrder(Enum):
    ASC = 'ascending'
    DESC = 'descending'


def is_sorted(num_list: List[int], sort_order: SortOrder) -> bool:
    check_data_type(num_list, sort_order)
    last = num_list[0]
    if sort_order == SortOrder.ASC:
        for item in num_list:
            if not (item >= last):
                return False
            last = item
    elif sort_order == SortOrder.DESC:
        for item in num_list:
            if not (item <= last):
                return False
            last = item
    return True

def check_data_type(num_list: List[int], sort_order: SortOrder):
    if not (isinstance(num_list, list) and isinstance(sort_order, SortOrder)):
        raise TypeError

    for item in num_list:
        if type(item) is not int:
            raise TypeError


def transform(num_list: List[int], sort_order: SortOrder) -> List[int]:
    check_data_type(num_list, sort_order)
    result = num_list[:]
    if is_sorted(num_list, sort_order):
        for index, item in enumerate(num_list):
            result[index] += index
    return result

#print(transform([5, 17, 24, 88], ''))
#print(transform(['', 5, 17, 24, 88], SortOrder.ASC))
#print(transform([5, 17, 24, 24], SortOrder.ASC))