#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

try:
    print("try")
    myrectangle = Rectangle(2, -3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
