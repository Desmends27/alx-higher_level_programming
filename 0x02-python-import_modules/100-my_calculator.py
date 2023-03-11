#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    c = argv[2]
    b = int(argv[3])
    result = 0
    if c == '+':
        result = add(a, b)
    elif c == '-':
        result = sub(a, b)
    elif c == '*':
        result = mul(a, b)
    elif c == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{0:d} {1:s} {2:d} = {3:d}".format(a, c, b, result))
