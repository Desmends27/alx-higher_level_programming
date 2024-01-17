#!/usr/bin/python3
""" Write to a string of text to a file """


def write_file(filename="", text=""):
    """Write text to filename """

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    return len(text)
