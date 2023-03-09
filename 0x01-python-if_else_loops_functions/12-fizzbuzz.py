#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if not i % 5 and not i % 3:
            print("FizzBuzz", end=' ')
        if i % 5 == 0:
            print("Buzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        else:
            print(i, end=' ')
