#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    Returns a new list with all values multiplied by a number using map.

    Args:
        my_list (list): The list to multiply values.
        number (int): The number to multiply values by.

    Returns:
        list: A new list with multiplied values.
    """
    return list(map(lambda x: x * number, my_list))
