def count_vowels_and_consonants_in_even_indices(s: str) -> tuple:
    """
    Counts the number of vowels and consonants at even indices in the given string.

    Args:
        s (str): The input string.

    Returns:
        tuple: A tuple containing two integers:
            - The first integer is the count of vowels at even indices.
            - The second integer is the count of consonants at even indices.

    Example:
        >>> count_vowels_and_consonants_in_even_indices("example1")
        (3, 1)

        >>> count_vowels_and_consonants_in_even_indices("hello")
        (1, 2)
    """
    
    
    vowel_count = 0
    consonant_count = 0
    for c in s[::2].lower():
        if c in "aeiou":
            vowel_count += 1
        elif c.isalpha():
            consonant_count += 1
    return vowel_count, consonant_count

# #Another Method:

# def count_vowels_and_consonants_in_even_indices(s: str) -> tuple:
    
#     v=0
#     c=0
#     l=s[0::2]
#     for j in l:
#         if j.lower() in 'aeiou':
#             v=v+1 
#         if j.lower() in 'bcdfghjklmnpqrstvwxyz':
#             c=c+1 
    
#     return(v,c)


# Count Vowels and Consonants in Even Indices
# Given a string s, count the number of vowels and consonants that appear at even indices in the string (0-based indexing). Ignore non-alphabetical characters.

# Implement the function count_vowels_and_consonants_in_even_indices that returns the counts as described above.

# The string s can have both upper and lower case letters.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Examples

# "abcdeaeiou" -> (4, 1)
# Characters at even indices are: 'a', 'c', 'e', 'e', 'u'.
# Vowels: 'a', 'e', 'e', 'u' (4 vowels).
# Consonants: 'c' (1 consonant).
# "a11bc11de11" -> (2, 1)
# Characters at even indices are: 'a', '1', 'b', '1', 'd', '1'.
# Vowels: 'a' (1 vowel).
# Consonants: 'b', 'd' (2 consonants).
# "ABCDE" -> (2, 1)
# Characters at even indices are: 'A', 'C', 'E'.
# Vowels: 'A', 'E' (2 vowels).
# Consonants: 'C' (1 consonant).

    
