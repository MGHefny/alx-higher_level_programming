#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in range(len(matrix)):
        for x in range(len(matrix[r])):
            if x != len(matrix[r]) - 1:
            endspace = ' '
            else:
            endspace = ''
            print("{:d}".format(matrix[r][x]), end=endspace)
        print()
