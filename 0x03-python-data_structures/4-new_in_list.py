#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 and idx >= len(my_list):
        return new_list
    new_list = my_list[:]
    for i in range(len(my_list) - 1):
        if idx == i:
            new_list[i] = element
    return new_list
