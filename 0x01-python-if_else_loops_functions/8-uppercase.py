#!/usr/bin/python3
def uppercase(str):
    """Prints a string in upper case"""
    for i in range(len(str)):
        temp = ord(str[i])
        if temp >= 97 and temp <= 122:
            temp = temp - 32
        print("{:c}".format(temp), end='')
    print()
