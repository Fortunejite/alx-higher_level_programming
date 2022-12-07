#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    tmp = []
    tmp_1 = []
    for i in matrix:
        for j in i:
            tmp.append(j ** 2)
        tmp_1.append(tmp)
        tmp = []
    return tmp_1
