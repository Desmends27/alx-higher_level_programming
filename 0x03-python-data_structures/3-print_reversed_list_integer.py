#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    if len(my_list) == 0:
        return None
    len_list = len(my_list)
    for i in reversed(my_list):
        print("{:d}".format(i))
