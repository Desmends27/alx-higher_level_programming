#!/usr/bin/python3
""" A read file function """


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    print(text, end="")
