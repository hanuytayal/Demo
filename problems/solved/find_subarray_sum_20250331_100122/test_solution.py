import pytest
from .solution import *

def test_find_subarray_with_target_sum():
    """Test suite for find_subarray_with_target_sum function."""
    # Input validation tests
    def test_type_checking():
        """Test that function correctly handles inputs of incorrect types."""
        with pytest.raises(TypeError, match="nums must be a list"):
            find_subarray_with_target_sum("not a list", 10)
        with pytest.raises(TypeError, match="target_sum must be an integer"):
            find_subarray_with_target_sum([1, 2, 3], "not an integer")
    def test_invalid_input():
        """Test that function correctly handles invalid inputs."""
        with pytest.raises(ValueError, match="nums cannot be empty"):
            find_subarray_with_target_sum([], 10)
    def test_boundary_condition():
        """Test that function correctly handles boundary conditions."""
        assert find_subarray_with_target_sum([1], 1) == (0, 0), "Failed on single element list"
    def test_null_empty_input():
        """Test that function correctly handles null/empty inputs."""
        assert find_subarray_with_target_sum([0, 0, 0], 0) == (0, 0), "Failed on list with zeros"
        assert find_subarray_with_target_sum([1, 2, 3], 0) is None, "Failed on target_sum of zero"
    # Error handling tests
    def test_error_message_validation():
        """Test that function correctly validates error messages."""
        with pytest.raises(TypeError, match="nums must be a list"):
            find_subarray_with_target_sum("not a list", 10)
    # Edge case tests
    def test_minimum_maximum_values():
        """Test that function correctly handles minimum/maximum values."""
        assert find_subarray_with_target_sum([1, 2, 3], 6) == (0, 2), "Failed on entire list summing to target_sum"
        assert find_subarray_with_target_sum([1, 2, 3, 4, 5], 6) == (1, 2), "Failed on multiple valid subarrays"
        assert find_subarray_with_target_sum([-1, 2, 3], 2) == (0, 2), "Failed on list with negative numbers"
    # Functional tests
    def test_basic_functionality():
        """Test that function correctly handles basic functionality."""
        assert find_subarray_with_target_sum([1, 2, 3], 5) == (1, 2), "Failed on basic functionality"
        assert find_subarray_with_target_sum([5, 3, 1, 7, 6, 4, 2], 10) == (2, 4), "Failed on complex scenario"
    def test_complex_scenarios():
        """Test that function correctly handles complex scenarios."""
        assert find_subarray_with_target_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15) == (0, 4), "Failed on complex scenario"
    # Performance tests
    def test_large_input():
        """Test that function correctly handles large inputs."""
        nums = [1] * 1000000
        start_time = time.time()
        assert find_subarray_with_target_sum(nums, 1000000) == (0, 999999), "Failed on large input"
        assert time.time() - start_time < 1, "Function took too long to execute on large input"