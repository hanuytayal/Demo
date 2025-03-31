from typing import List
def two_sum(nums: List[int], target: int) -> List[int]:
    """
    This function takes in a list of integers 'nums' and an integer 'target'.
    It finds two numbers in 'nums' that add up to 'target' and returns their indices.
    It raises an error if 'nums' or 'target' are not of the correct type or out of range.
    """
    # Input validation
    if not isinstance(nums, list) or not all(isinstance(num, int) for num in nums):
        raise TypeError("'nums' must be a list of integers")
    if not isinstance(target, int):
        raise TypeError("'target' must be an integer")
    if len(nums) < 2 or len(nums) > 10**4:
        raise ValueError("'nums' must contain between 2 and 10^4 elements inclusive")
    if any(num < -10**9 or num > 10**9 for num in nums) or target < -10**9 or target > 10**9:
        raise ValueError("All elements of 'nums' and 'target' must be between -10**9 and 10**9 inclusive")
    # A hash map to store the difference of 'target' and the current element in 'nums' as the key 
    # and the index as the value
    num_map = {}
    # Iterate through 'nums'
    for i, num in enumerate(nums):
        # If the current element is present in the hash map, we have found the two numbers that add up to 'target'
        if num in num_map:
            return [num_map[num], i]
        else:
            # Store the difference of 'target' and the current element in 'nums' as the key 
            # and the index as the value in the hash map
            num_map[target - num] = i
    # If no two numbers that add up to 'target' are found, raise an error
    raise ValueError("No two numbers in 'nums' add up to 'target'")