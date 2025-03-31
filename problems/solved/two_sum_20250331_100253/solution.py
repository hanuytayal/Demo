from typing import List
def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    Args:
    nums (List[int]): List of integers
    target (int): Target sum
    Returns:
    List[int]: Indices of the two numbers from nums that add up to target
    Raises:
    TypeError: If nums is not a list or target is not an int or nums does not contain only integers
    ValueError: If nums does not contain at least two integers or more than 10^4 integers
    """
    # Type checking
    if not isinstance(nums, list) or not isinstance(target, int) or not all(isinstance(num, int) for num in nums):
        raise TypeError("nums must be a list of integers and target must be an integer")
    # Input size validation
    if len(nums) < 2 or len(nums) > 10**4:
        raise ValueError("nums must contain at least two integers and not more than 10^4 integers")
    # Create a dictionary to store the difference between the target and the current integer as the key 
    # and the index of the current integer as the value
    num_dict = {}
    # Iterate through the list of integers
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    # If no solution is found
    raise ValueError("No two sum solution")