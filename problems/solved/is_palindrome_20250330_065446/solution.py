import re
from typing import Union
def is_palindrome(input_string: str) -> bool:
    """
    Returns True if the input string is a palindrome, False otherwise. 
    The function is case-insensitive and ignores spaces and special characters.
    An empty string is considered a palindrome. If input is not a string, raises a TypeError.
    Args:
        input_string (str): The string to check.
    Returns:
        bool: True if the input string is a palindrome, False otherwise.
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string, if not raise a TypeError
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use two pointers approach for better performance
    left, right = 0, len(input_string) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not input_string[left].isalnum():
            left += 1
            
        # Skip non-alphanumeric characters from right
        while left < right and not input_string[right].isalnum():
            right -= 1
            
        # Compare characters (case-insensitive)
        if input_string[left].lower() != input_string[right].lower():
            return False
            
        left += 1
        right -= 1
    
    return True