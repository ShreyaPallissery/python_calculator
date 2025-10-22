def add(*args):
    """Return the sum of all arguments"""
    if not args:
        return 0
    result = 0
    for num in args:
        result += num
    return result


def subtract(*args):
    """Subtract all subsequent arguments from the first argument"""
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result


def multiply(*args):
    """Return the product of all arguments"""
    if not args:
        return 0
    result = 1
    for num in args:
        result *= num
    return result


def divide(*args):
    """Divide the first argument by all subsequent arguments"""
    if not args:
        raise ValueError("At least one argument is required")
    if len(args) == 1:
        raise ValueError("At least two arguments are required")
    result = args[0]
    for num in args[1:]:
        result /= num
    return result
