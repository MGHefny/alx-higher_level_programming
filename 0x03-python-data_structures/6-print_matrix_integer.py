#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for r in range(len(matrix)):
            for x in range(len(matrix[r])):
                if x != len(matrix[r]) - 1:
                    e = ' '
                else:
                    e = ''
                print("{:d}".format(matrix[r][x]), end=e)
            print()
