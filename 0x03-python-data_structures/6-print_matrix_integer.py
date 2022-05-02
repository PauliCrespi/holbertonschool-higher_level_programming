#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        lem1 = len(matrix)
        for i in range(lem1):
            for j in range(len(matrix[i])):
                if j < (len(matrix[i]) - 1):
                    print(f"{matrix[i][j]}", end=' ')
                else:
                    print(f"{matrix[i][j]}", end='')
            print("")
