def add(*args):
    """
    Add unlimited number of parameters.
    
    Args:
        *args: Variable number of numeric arguments
        
    Returns:
        Sum of all arguments
    """
    print(f"Performing addition operation with numbers: {args}")  # Combined both changes
    return sum(args)
    

def subtract(*args):
    """Subtract all subsequent arguments from the first argument"""
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result