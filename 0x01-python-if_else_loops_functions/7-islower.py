#!/usr/bin/python3
def islower(c):
    """Check for lowercase character"""
    n = ord(c)
    if n >= 97 and n <= 122:
        return True
    return False
