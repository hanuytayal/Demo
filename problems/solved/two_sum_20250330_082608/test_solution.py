import pytest
import time
from .solution import *

def test_two_sum_solution():
    """
    Test the two sum solution function to ensure it correctly identifies the two numbers in the array that add up to the target.
    """
    assert two_sum([2, 7, 11, 15], 9) == [0, 1], "Error: Expected [0, 1]"
    assert two_sum([3, 2, 4], 6) == [1, 2], "Error: Expected [1, 2]"
    assert two_sum([3, 3], 6) == [0, 1], "Error: Expected [0, 1]"

def test_two_sum_input_validation():
    """
    Test the two sum function with edge cases and invalid inputs to ensure the function handles error conditions correctly.
    """
    # Test with less than two elements
    with pytest.raises(ValueError, match="The array should contain at least two elements"):
        two_sum([1], 1)
    # Test with non-integer elements
    with pytest.raises(TypeError, match="The elements in the array and the target should be integers"):
        two_sum([1, 'a'], 1)
    # Test with non-integer target
    with pytest.raises(TypeError, match="The elements in the array and the target should be integers"):
        two_sum([1, 2], 'a')

def test_two_sum_edge_cases():
    """
    Test the two sum function with edge cases such as the two numbers being at the start, in the middle, or at the end of the array, or the two numbers being the same.
    """
    assert two_sum([1, 2, 3, 4, 5], 3) == [0, 1], "Error: Expected [0, 1]"
    assert two_sum([1, 2, 3, 4, 5], 5) == [1, 2], "Error: Expected [1, 2]"
    assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4], "Error: Expected [3, 4]"
    assert two_sum([5, 5], 10) == [0, 1], "Error: Expected [0, 1]"

def test_two_sum_performance():
    """
    Test the two sum function with a large array to verify the function can handle the maximum allowed input size.
    """
    # Create a large array with known sum
    large_array = list(range(1, 1001))  # 1000 elements
    target = 1999  # Sum of last two elements (999 + 1000)
    
    # Start timer
    start = time.time()
    
    # Call function with large input
    result = two_sum(large_array, target)
    
    # End timer
    end = time.time()
    
    # Verify result
    assert result == [998, 999], "Error: Expected [998, 999]"
    
    # Check execution time (should be under 1 second)
    assert end - start < 1, "Error: Function took longer than expected"