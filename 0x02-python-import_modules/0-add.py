#!/usr/bin/python3
if __name__ == "__main__":
    a = 1
    b = 2
    from add_0 import add
    num = add(a, b)
    print("{0:d} + {1:d} = {2:d}".format(a, b, num))
