#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    zero = (0, )
    if len(tuple_a) == 1:
        tuple_a = tuple_a + zero
    elif len(tuple_a) == 0:
        tuple_a = 0, 0
    if len(tuple_b) == 1:
        tuple_b = tuple_b + zero
    elif (len(tuple_b)) == 0:
        tuple_b = 0, 0
    sum_tup = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return sum_tup
