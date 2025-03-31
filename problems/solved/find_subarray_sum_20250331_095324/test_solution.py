import pytest
from .solution import *

def test_find_subarray():
    """
    Testing the find_subarray function for various test cases
    """
    # Input validation tests
    # Testing for type checking
    with pytest.raises(TypeError, match="Input list must be a list of integers"):
        find_subarray([1, 2, '3'], 6)
    with pytest.raises(TypeError, match="target_sum must be an integer"):
        find_subarray([1, 2, 3], '6')
    # Testing for invalid input (empty list)
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_subarray([], 6)
    # Testing for boundary conditions
    assert find_subarray([1], 1) == (0, 0), "Failed on a single element list where element equals target sum"
    assert find_subarray([1], 2) is None, "Failed on a single element list where element does not equal target sum"
    assert find_subarray([0, 0, 0], 0) == (0, 0), "Failed on list with all zeros and target sum zero"
    # Error handling tests
    # Testing for Exception handling
    with pytest.raises(Exception):
        find_subarray([1, 2, 3], 6)
    # Testing for error message validation
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_subarray([], 6)
    # Testing for error condition handling
    with pytest.raises(TypeError):
        find_subarray([1, 2, '3'], 6)
    with pytest.raises(TypeError):
        find_subarray([1, 2, 3], '6')
    # Edge case tests
    assert find_subarray([1, 2, 3], 6) == (0, 2), "Failed on normal case"
    assert find_subarray([10, 2, 3], 5) == (1, 2), "Failed on case with multiple valid subarrays"
    assert find_subarray([1, 2, 3], 10) is None, "Failed on case where sum cannot be found"
    # Functional tests
    assert find_subarray([1, 2, 3, 4, 5], 15) == (0, 4), "Failed on basic functionality"
    assert find_subarray([-1, 0, 5, -2, 3], 6) == (2, 3), "Failed on complex scenario with negative numbers"
    # Performance tests
    import time
    long_list = [1] * 10**6
    start_time = time.time()
    assert find_subarray(long_list, 10**6) == (0, 10**6 - 1), "Failed on large input"
    execution_time = time.time() - start_time
    assert execution_time < 1, "Function took too long to execute on large input"