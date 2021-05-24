"""
Task04_3

Implement a function which works the same as str.split

Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""


def split_alternative(str_to_split: str, delimiter: str=' ') -> list:
    if not (isinstance(str_to_split, str) and isinstance(delimiter, str)):
        raise ValueError
    
    res=[]
    last=0

    for index, char in enumerate(str_to_split):
        if char==delimiter:
            res.append(str_to_split[last:index])
            last=index+1

    res.append(str_to_split[last:index+1])

    return res

#print(split_alternative('srth gst h'))
#print(split_alternative('srthgsth', ','))
#print(split_alternative('qwe,', ','))