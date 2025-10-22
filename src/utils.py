def add(*args):
    """
    Add unlimited number of parameters.
    
    Args:
        *args: Variable number of numeric arguments
        
    Returns:
        Sum of all arguments
    """
    return sum(args)


def subtract(*args):
    """
    Subtract unlimited number of parameters from the first argument.
    
    Args:
        *args: Variable number of numeric arguments
        
    Returns:
        Result of subtracting all subsequent arguments from the first
    """
    if len(args) == 0:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result