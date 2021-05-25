"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""


def swap_quotes(string: str) -> str:
    res = []
    for char in string:
        if char == "'":
            res.append("\"")
        elif char == "\"":
            res.append("'")
        else:
            res.append(char)
    return "".join(res)

# print("ftyftyj'ftyjftyjftyj\"")
# print(swap_quotes("ftyftyj'ftyjftyjftyj\""))
