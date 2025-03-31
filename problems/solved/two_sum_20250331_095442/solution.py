from typing import List, Tuple
def find_two_sum(array: List[int], target: int) -> Tuple[int, int]:
    """
    This function takes a list of integers and a target integer. It returns a tuple of two indices such that
    the numbers at those indices in the list add up to the target.
    :param array: List[int] - A list of integers.
    :param target: int - A target integer.
    :return: Tuple[int, int] - A tuple of two indices.
    :raises TypeError: If the array is not a list or the target is not an integer.
    :raises ValueError: If the array has less than two elements or no two numbers in the array add up to the target.
    """
    if not isinstance(array, list) or not all(isinstance(num, int) for num in array):
        raise TypeError("array must be a list of integers")
    if not isinstance(target, int):
        raise TypeError("target must be an integer")
    if len(array) < 2:
        raise ValueError("array must have at least two elements")
    num_to_index = {}
    for i, num in enumerate(array):
        if num in num_to_index:
            return num_to_index[num], i
        else:
            num_to_index[target - num] = i
    raise ValueError("No two sum solution exists in the array for the given target")