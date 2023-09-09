#!/usr/bin/pytho3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("{}".format(""))
    for i in matrix:
        for j in range(len(i)):
            print("{}".format(int(i[j])), end=" " if j < len(i) - 1 else "")
        print("{}".format(""))
