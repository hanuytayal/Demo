import pytest
from .solution import *

def test_input_validation():
    """
    Test input validation.
    """
    with pytest.raises(TypeError, match="array must be a list of integers"):
        find_two_sum('Not a list', 10)
    with pytest.raises(TypeError, match="target must be an integer"):
        find_two_sum([1, 2, 3], 'Not an integer')
    with pytest.raises(ValueError, match="array must have at least two elements"):
        find_two_sum([1], 10)
def test_error_handling():
    """
    Test error handling.
    """
    with pytest.raises(ValueError, match="No two sum solution"):
        find_two_sum([1, 2, 3], 10)
def test_edge_cases():
    """
    Test edge cases.
    """
    assert find_two_sum([1, 1], 2) == [0, 1], "Failed on two same elements"
    assert find_two_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19) == [8, 9], "Failed on two elements at the ends"
def test_functionality():
    """
    Test functionality.
    """
    assert find_two_sum([2, 7, 11, 15], 9) == [0, 1], "Failed on basic functionality"
    assert find_two_sum([3, 2, 4], 6) == [1, 2], "Failed on complex scenario"
    assert find_two_sum([2, 3, 4, 5], 7) == [0, 3], "Failed on multiple valid solutions"
def test_performance():
    """
    Test performance.
    """
    large_input = list(range(1, 10001))
    start_time = time.time()
    assert find_two_sum(large_input, 19999) == [9997, 9998], "Failed on large input"
    end_time = time.time()
    time_taken = end_time - start_time
    assert time_taken < 1, "Function took too long to find two sum in large input"