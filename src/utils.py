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


def multiply(*args):
    """
    Multiply unlimited number of parameters.
    
    Args:
        *args: Variable number of numeric arguments
        
    Returns:
        Product of all arguments
    """
    if len(args) == 0:
        return 0
    result = 1
    for num in args:
        result *= num
    return result


def divide(*args):
    """
    Divide the first parameter by all subsequent parameters.
    
    Args:
        *args: Variable number of numeric arguments
        
    Returns:
        Result of dividing first argument by all subsequent arguments
        
    Raises:
        ZeroDivisionError: If any divisor is zero
        ValueError: If less than 2 arguments provided
    """
    if len(args) < 2:
        raise ValueError("Division requires at least 2 arguments")
    
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result /= num
    return result