def call_once(func):
    def wrapper(*args, cached=[]):
        if cached:
            return cached[0]
        else:
            cached.append(func(*args))
            return func(*args)
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b