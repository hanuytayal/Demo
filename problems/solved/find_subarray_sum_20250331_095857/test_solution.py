import pytest
from .solution import *

def test_find_subarray_sum():
    """
    This function includes tests for the function find_subarray_sum(nums: List[int], target_sum: int)
    """
    # Input validation tests
    def test_type_checking():
        """
        Test for checking the type of inputs.
        """
        with pytest.raises(TypeError, match="nums should be a list of integers"):
            find_subarray_sum("not a list", 10)
        with pytest.raises(TypeError, match="target_sum should be an integer"):
            find_subarray_sum([1, 2, 3], "not an integer")
    def test_invalid_input():
        """
        Test for handling invalid inputs.
        """
        with pytest.raises(ValueError, match="nums should not be empty"):
            find_subarray_sum([], 10)
    def test_boundary_conditions():
        """
        Test for handling boundary conditions.
        """
        assert find_subarray_sum([1, 2, 3, 4, 5], 1) == (0, 0), "The function should be able to find subarray at the start of the list"
        assert find_subarray_sum([1, 2, 3, 4, 5], 5) == (4, 4), "The function should be able to find subarray at the end of the list"
    # Error handling tests
    def test_exception_handling():
        """
        Test for handling exceptions.
        """
        with pytest.raises(Exception, match="nums should only contain integers"):
            find_subarray_sum([1, 2, 3, "not an integer"], 10)
    # Functional tests
    def test_basic_functionality():
        """
        Test for basic functionality.
        """
        assert find_subarray_sum([1, 2, 3, 4, 5], 10) == (1, 4), "The function should be able to find a valid subarray that sums up to the target sum"
    def test_complex_scenarios():
        """
        Test for complex scenarios.
        """
        assert find_subarray_sum([1, 4, 20, 3, 10, 5], 33) == (2, 4), "The function should be able to find subarray in complex scenarios"
    # Edge case tests
    def test_minimum_maximum_values():
        """
        Test for handling minimum and maximum values.
        """
        assert find_subarray_sum([1], 1) == (0, 0), "The function should be able to find subarray in list with only one element"
        assert find_subarray_sum([1, 1, 1, 1], 4) == (0, 3), "The function should be able to find subarray in list where all elements are the same and equal to target_sum"
        assert find_subarray_sum([0, 0, 0, 0], 0) == (0, 0), "The function should be able to find subarray in list where the target_sum is 0"
    # Performance tests
    def test_large_inputs():
        """
        Test for handling large inputs.
        """
        large_list = [1] * 10**6
        assert find_subarray_sum(large_list, 10**6) == (0, 10**6 - 1), "The function should be able to handle large inputs efficiently"