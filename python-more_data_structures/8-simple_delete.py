#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key from a dictionary.

    Args:
        a_dictionary (dict): The dictionary to delete a key from.
        key (str): The key to delete.
    """
    a_dictionary.pop(key, None)
    return a_dictionary
