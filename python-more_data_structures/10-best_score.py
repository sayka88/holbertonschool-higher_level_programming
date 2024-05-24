#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to find the best score.

    Returns:
        Any: The key with the biggest integer value or None if no score found.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
