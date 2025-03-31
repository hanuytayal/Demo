from typing import List, Tuple, Optional
def find_subarray_sum(nums: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    """
    Function to find a contiguous subarray within an array (nums) of integers that sums to a given target sum.
    Parameters:
        nums (List[int]): Input list of integers.
        target_sum (int): Target sum to find in the subarray.
    Returns:
        Optional[Tuple[int, int]]: The range of indices for the subarray. None if no such subarray exists.
    """
    # input validation
    if not isinstance(nums, list):
        raise TypeError("nums should be a list of integers")
    if not all(isinstance(num, int) for num in nums):
        raise TypeError("nums should only contain integers")
    if not isinstance(target_sum, int):
        raise TypeError("target_sum should be an integer")
    if not nums:
        raise ValueError("nums should not be empty")
    # variables to keep track of the current sum and the start and end indices of the current subarray
    current_sum = 0
    start = 0
    # variables to keep track of the minimum length subarray that sums to the target
    min_len = float('inf')
    min_start = -1
    min_end = -1
    # iterate over the list
    for end in range(len(nums)):
        # add the current number to the current sum
        current_sum += nums[end]
        # while the current sum is greater than the target, move the start of the window forward
        while current_sum > target_sum:
            current_sum -= nums[start]
            start += 1
        # if the current sum is equal to the target and the length of the current subarray is less than the minimum length, update the minimum length and indices
        if current_sum == target_sum and end - start + 1 < min_len:
            min_len = end - start + 1
            min_start = start
            min_end = end
    # if no valid subarray was found, return None
    if min_start == -1:
        return None
    # return the start and end indices of the minimum length subarray
    return min_start, min_end