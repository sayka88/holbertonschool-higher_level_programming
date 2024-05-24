#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Convert the list to a set to get unique elements
    unique_elements = set(my_list)
    # Sum all unique elements and return the result
    return sum(unique_elements)
