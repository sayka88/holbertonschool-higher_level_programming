#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Prints a dictionary with keys sorted in alphabetic order.
    # Args:
    # a_dictionary (dict): The dictionary to print.
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
