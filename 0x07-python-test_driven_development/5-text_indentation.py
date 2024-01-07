#!/usr/bin/python3
""" This function prints 2 lines after each of these chars . ? : """


def text_indentation(text):
    """
    Args:
        text: text input
    Raises:
        TypeError: if text is not a string
    """
    result = ""
    check = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:
        if i in ['.', '?', ':']:
            result += i + '\n\n'
            check = True
        elif check and i == ' ':
            continue
        else:
            result += i
            check = False
    print(result, end="")
