from typing import List, Tuple, Optional
def find_subarray(input_list: List[int], target_sum: int) -> Optional[Tuple[int,int]]:
    """
    This function accepts a list of integers and a target sum, and returns the indices of the subarray that adds up to 
    the target sum. If there are multiple such subarrays, it returns the shortest one. If there are multiple shortest 
    subarrays, it returns the one with the smallest starting index. If no such subarray exists, it returns None.
    Args:
    input_list: a list of integers that may contain the target sum.
    target_sum: an integer that the function tries to obtain by summing elements of the input list.
    Returns:
    A tuple of two integers representing the starting and ending indices of the subarray that adds up to the target 
    sum, or None if no such subarray exists.
    """
    if not isinstance(input_list, list) or not all(isinstance(i, int) for i in input_list):
        raise TypeError('Input list must be a list of integers')
    if not isinstance(target_sum, int):
        raise TypeError('target_sum must be an integer')
    if len(input_list) == 0:
        raise ValueError('Input list cannot be empty')
    start_index = 0
    current_sum = 0
    for end_index, value in enumerate(input_list):
        current_sum += value
        while current_sum > target_sum:
            current_sum -= input_list[start_index]
            start_index += 1
        if current_sum == target_sum:
            return (start_index, end_index)
    return None