#!/usr/bin/python3
""" Append a string at the end of a text file """

def append_write(filename="", text=""):
    """ Append text to file """
    with open(filename, 'a+', encoding='utf-8') as f:
        f.write(text)
    return len(text)
