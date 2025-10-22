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