def sum_of_floored_to_tens(a:int, b:int):
    """
    Calculate the sum of two integers floored to the nearest lower multiple of 10.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers after flooring each to the nearest lower multiple of 10.

    Examples:
        >>> sum_of_floored_to_tens(23, 47)
        60
        >>> sum_of_floored_to_tens(35, 19)
        40
        >>> sum_of_floored_to_tens(0, 105)
        100
    """
    
    
    a = a // 10 * 10
    b = b // 10 * 10
    return a + b
    
# #Another Method:

# def sum_of_floored_to_tens(a:int, b:int):
#     return (a//10)*10+(b//10)*10

# Sum of Floored to Tens
# Given two integers a and b, return the sum of the two numbers where both numbers are floored to the nearest ten.

# Flooring to the nearest ten means removing the unit digit and rounding the number down to the nearest multiple of 10.

# Assume both the numbers are positive integers.

# Example
# Input:

# 35, 46
# Output:

# 70
# Explanation:

# 35 floored to tens is 30.
# 46 floored to tens is 40.
# Sum: 30 + 40 = 70.
    
