#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list.

    Args:
        my_list (list): The input list of integers.

    Returns:
        list: A new list with True or False
              element in the original list is a multiple of 2.
    """
    return [num % 2 == 0 for num in my_list]
