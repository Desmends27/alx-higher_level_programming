#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv)-1 == 0:
        print("0 arguments.")
    else:
        print('''{:d} argument'''.format(len(argv) - 1),
              end="s:\n" if len(argv) - 1 != 1 else ":\n")

        for i in range(1, len(argv)):
            print("{0:d}: {1:s}".format(i, argv[i]))
