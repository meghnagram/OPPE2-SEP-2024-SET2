def number_with_more_unique_digits(n1:int, n2:int):
    """
    Compares two integers and returns the one with more unique digits.

    Args:
        n1 (int): The first integer.
        n2 (int): The second integer.

    Returns:
        int or tuple: The integer with more unique digits. 
        If both numbers have the same number of unique digits, 
        returns a tuple of both integers `(n1, n2)`.

    Example:
        >>> number_with_more_unique_digits(123, 1122)
        123

        >>> number_with_more_unique_digits(1122, 2211)
        (1122, 2211)
    """
    
    
    n1_n_unique = len(set(str(n1)))
    n2_n_unique = len(set(str(n2)))
    if n1_n_unique> n2_n_unique:
        return n1
    elif n2_n_unique> n1_n_unique:
        return n2
    else:
        return (n1,n2)


# #Another Method:

# def number_with_more_unique_digits(n1:int, n2:int):
   
#     s1=set(str(n1))
#     s2=set(str(n2))
    
#     if len(s1)>len(s2):
#         return n1
#     elif len(s1)<len(s2):
#         return n2
#     else:
#         return (n1,n2)
    
# Number with More Unique Digits
# Given two integers n1 and n2, return the number that contains more unique digits.

# If both numbers have the same number of unique digits, return the both as a tuple as (n1, n2).

# Assume both the integers n1 and n2 are positive integer.

# Hint: Use set to find the unique digits, as sets automatically eliminate duplicates.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# n1 = 2345, n2 = 1111 -> 2345

# Explanation

# n1 = 2345 has the unique digits 2, 3, 4, 5 (4 unique digits).
# n2 = 1111 has the unique digit 1 (1 unique digit).
# Since n1 has more unique digits, the output is 2345.
# Example

# n1 = 1243, n2 = 123344 -> (1243, 123344)

# Explanation

# n1 = 1243 - 4 unique digits.
# n2 = 123344 - 4 unique digits.
# Since n1 has same number of unique digits, the output is (1243, 123344).  
    

    
