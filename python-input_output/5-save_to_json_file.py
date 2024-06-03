#!/usr/bin/python3
"""4. From JSON string to Object"""
import json


def save_to_json_file(my_obj, filename):
    """save to json"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
