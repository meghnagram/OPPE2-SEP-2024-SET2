def surround_first_two_and_last_two_with_brackets(s: str):
    """
    Surrounds the first two and last two characters of the input string with square brackets.

    It is assumed that the input has atleast four characters.

    Args:
        s (str): The input string.

    Returns:
        str: A new string with the first two and last two characters surrounded by square brackets.

    Example:
        >>> surround_first_two_and_last_two_with_brackets("example")
        '[ex]amp[le]'
    """
    
    return f"[{s[:2]}]{s[2:-2]}[{s[-2:]}]"

# #Another Method:

# def surround_first_two_and_last_two_with_brackets(s: str):
    
#     return '['+s[0:2]+']'+s[2:-2]+'['+s[-2:]+']'

# Surround First Two and Last Two with Square Brackets
# Given a string s, you need to surround the first two and the last two characters of the string with square brackets [].

# Assueme the string s will have at least 4 characters.

# Example

# "hello" -> "[he]l[lo]"
# "python" -> "[py]th[on]"
# "brackets" -> "[br]acke[ts]"
# "four" -> "[fo][ur]"
    
