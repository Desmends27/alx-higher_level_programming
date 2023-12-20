#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for ele in matrix:
        sqlist = list(map(lambda i: i * i, ele))
        mat.append(sqlist)
    return mat
