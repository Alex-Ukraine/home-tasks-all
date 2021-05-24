def remember_result(fn):
    def wrapper(*args, prev=[]):
        if prev:
            print(f"Last result = '{prev[-1]}'")
        else:
            print(f"Last result = '{None}'")
        prev.append(fn(*args))
    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result