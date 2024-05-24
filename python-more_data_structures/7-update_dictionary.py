#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    #    Updates a dictionary by adding or replacing a key/value pair
    #    Args:
    #       a_dictionary (dict): The dictionary to update.
    #       key (str): The key to add or replace.
    #    value: The value to add or replace
    a_dictionary[key] = value
    return a_dictionary
