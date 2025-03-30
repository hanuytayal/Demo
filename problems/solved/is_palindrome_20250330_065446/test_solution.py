import pytest
import time
from .solution import *

def test_is_palindrome():
    """
    Test the is_palindrome function with various inputs
    """
    # Test with a simple palindrome
    assert is_palindrome("racecar") is True, "Failed on 'racecar'"
    # Test with a palindrome that includes capital letters
    assert is_palindrome("RaceCar") is True, "Failed on 'RaceCar'"
    # Test with a palindrome that includes spaces and special characters
    assert is_palindrome("Able , was I saw elba") is True, "Failed on 'Able , was I saw elba'"
    # Test with a palindrome that includes numbers
    assert is_palindrome("12321") is True, "Failed on '12321'"
    # Test with a string that is not a palindrome
    assert is_palindrome("Hello") is False, "Failed on 'Hello'"
    # Test with an empty string
    assert is_palindrome("") is True, "Failed on ''"
    # Test with a single character string
    assert is_palindrome("a") is True, "Failed on 'a'"

def test_is_palindrome_errors():
    """
    Test the is_palindrome function for proper error handling
    """
    # Test with a non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        is_palindrome(123)
    # Test with a None input
    with pytest.raises(TypeError, match="Input must be a string"):
        is_palindrome(None)

def test_is_palindrome_performance():
    """
    Test the performance of the is_palindrome function
    """
    # Generate a large palindrome
    large_palindrome = "a" * 1000000 + "b" * 1000000 + "a" * 1000000
    # Start the timer
    start_time = time.time()
    # Run the function
    is_palindrome(large_palindrome)
    # End the timer
    end_time = time.time()
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    # Assert that the function finishes in less than 1 second
    assert elapsed_time < 1, f"Function took too long to complete: {elapsed_time} seconds"