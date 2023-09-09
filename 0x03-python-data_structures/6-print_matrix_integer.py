#!/usr/bin/pytho3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("{}".format(""))
    for i in matrix:
        for j in range(len(i)):
            print(
                    "{:d}".format(int(i[j])),
                    end=" " if j < len(i) - 1 else "\n"
                )
