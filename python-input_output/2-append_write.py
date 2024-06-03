#!/usr/bin/python3
'''2. Append to a file'''


def append_write(filename="", text=""):
    """append

    Args:
        filename: name of file
        text: text to append
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return len(text)
