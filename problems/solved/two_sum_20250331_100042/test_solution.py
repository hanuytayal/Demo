import pytest
from .solution import *

def test_two_sum():
    """
    Comprehensive test suite for the 'two_sum' function.
    """
    # Test with valid input
    def test_valid_input():
        assert two_sum([2, 7, 11, 15], 9) == [0, 1], "Failed on valid input"
        assert two_sum([3, 2, 4], 6) == [1, 2], "Failed on valid input"
        assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4], "Failed on valid input"
    # Test with input of length 2
    def test_length_two():
        assert two_sum([1, 2], 3) == [0, 1], "Failed on input length of two"
    # Test with input containing duplicate elements adding up to target
    def test_with_duplicates():
        assert two_sum([3, 4, 3], 6) == [0, 2], "Failed on input with duplicates"
    # Test with invalid type of 'nums' or 'target'
    def test_invalid_type():
        with pytest.raises(TypeError) as e_info:
            two_sum("invalid", 9)
        assert str(e_info.value) == "'nums' must be a list of integers"
        with pytest.raises(TypeError) as e_info:
            two_sum([2, 7, 11, 15], "invalid")
        assert str(e_info.value) == "'target' must be an integer"
    # Test with 'nums' being an empty list or containing only one element
    def test_invalid_length():
        with pytest.raises(ValueError) as e_info:
            two_sum([], 9)
        assert str(e_info.value) == "'nums' must contain at least two elements"
        with pytest.raises(ValueError) as e_info:
            two_sum([1], 9)
        assert str(e_info.value) == "'nums' must contain at least two elements"
    # Test with 'nums' or 'target' not being integers
    def test_not_integer():
        with pytest.raises(TypeError) as e_info:
            two_sum([1.1, 2.2, 3.3], 4.4)
        assert str(e_info.value) == "All elements of 'nums' and 'target' must be integers"
    # Test with 'nums' or 'target' being out of range
    def test_out_of_range():
        with pytest.raises(ValueError) as e_info:
            two_sum([10**9+1], 9)
        assert str(e_info.value) == "All elements of 'nums' and 'target' must be between -10**9 and 10**9 inclusive"
        with pytest.raises(ValueError) as e_info:
            two_sum([2, 7, 11, 15], 10**9+1)
        assert str(e_info.value) == "All elements of 'nums' and 'target' must be between -10**9 and 10**9 inclusive"
    # Performance test with 'nums' containing the maximum number of elements (10^4)
    def test_maximum_elements():
        start_time = time.time()
        nums = list(range(1, 10**4+1))
        target = nums[-1] + nums[-2]
        assert two_sum(nums, target) == [10**4-2, 10**4-1]
        execution_time = time.time() - start_time
        assert execution_time < 1, "Performance test failed. Execution time must be less than 1 second"