#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Args:
        roman_string (str): The Roman numeral string to convert.

    Returns:
        int: The integer representation of the Roman numeral, or 0 if input is invalid.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    integer_value = 0
    length = len(roman_string)

    for i in range(length):
        if i > 0 and roman_numerals[roman_string[i]] > roman_numerals[roman_string[i - 1]]:
            integer_value += roman_numerals[roman_string[i]] - 2 * roman_numerals[roman_string[i - 1]]
        else:
            integer_value += roman_numerals[roman_string[i]]

    return integer_value
