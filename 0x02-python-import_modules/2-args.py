#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(len(argv)))
        for i in range(1, len(argv)):
            print("{0:d}: {1:s}".format(i, argv[i]))
