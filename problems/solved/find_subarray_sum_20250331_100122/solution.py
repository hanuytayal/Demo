from typing import List, Tuple, Optional
def find_subarray_with_target_sum(nums: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    """
    This function finds a subarray in the given list that sums to the target sum. 
    Args:
        nums (List[int]): The list of integers.
        target_sum (int): The target sum.
    Returns:
        Tuple[int, int]: The starting and ending indices of the subarray that sums to target_sum.
        None: If no such subarray exists.
    Raises:
        TypeError: If the provided nums is not a list or target_sum is not an integer.
        ValueError: If the provided nums is an empty list.
    """
    if not isinstance(nums, list):
        raise TypeError('nums must be a list')
    if not all(isinstance(num, int) for num in nums):
        raise TypeError('All elements in nums must be integers')
    if not isinstance(target_sum, int):
        raise TypeError('target_sum must be an integer')
    if len(nums) == 0:
        raise ValueError('nums cannot be empty')
    left, right = 0, 0
    current_sum = nums[0]
    while right < len(nums):
        if current_sum == target_sum:
            return (left, right)
        elif current_sum < target_sum:
            if right + 1 < len(nums):
                right += 1
                current_sum += nums[right]
            else:
                break
        else:
            current_sum -= nums[left]
            left += 1
    return None