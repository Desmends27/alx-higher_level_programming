#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, '5', 6]
]
new_list = 10
print(matrix_divided(new_list, 3))
print(matrix)
