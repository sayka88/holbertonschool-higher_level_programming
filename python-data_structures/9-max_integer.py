#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer in a list.

    Args:
        my_list (list): The input list of integers.

    Returns:
        int: The biggest integer in the list, or None if the list is empty.
    """
    if not my_list:
        return None

    max_val = my_list[0]
    for num in my_list[1:]:
        if num > max_val:
            max_val = num

    return max_val
