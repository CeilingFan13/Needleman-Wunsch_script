#!/usr/bin/env python3
# Needleman-Wunsch

import sys
import re
import pandas

def create_matrix(rows, cols, str1, str2):
    matrix = []
    for y in range(rows + 3):
        matrix.append([])
        for x in range(cols + 3):
            matrix[-1].append(0)
    for n in range(len(str1)):
        matrix[n+2][0] = str1[n]
    for i in range(len(str2)):
        matrix[0][i+2] = str2[i]

    return matrix

def scoring_matrix(match, mismatch, gap):
    matrix[1][1] = 0
    row = 0
    for n in range(len(matrix)-2):
        matrix[n+2][1] = matrix[n+1][1] + gap
    for n in range(len(matrix[1])-2):
        matrix [1][n+2] = matrix[1][n+1] + gap
    for n in range(len(matrix)-2):
        row = n
        for i in range(len(matrix[1])-2):
            vertical = matrix[row+1][i+2] + gap
            horizontal = matrix[row+2][i+1] + gap
            if matrix[n+2][0] == matrix[0][i+2]:
                diagonal = matrix[row+1][i+1] + match
            else:
                diagonal = matrix[row+1][i+1] + mismatch
            matrix[row+2][i+2] = max(vertical, horizontal, diagonal)

    return matrix



if __name__ == "__main__":

    # make sure there are no less than two arguments
    arg_count = len(sys.argv) - 1
    if arg_count < 5:
        raise Exception("This script requires 5 arguments: two strings and three numbers")
    if not re.match('^[ATGC]+$', sys.argv[1]) or not re.match('^[ATGC]+$', sys.argv[2]):
        raise Exception("Please only input DNA sequences")


    rows = len(sys.argv[1])
    cols = len(sys.argv[2])

    seq1 = sys.argv[1]
    seq2 = sys.argv[2]

    match = int(sys.argv[3])
    mismatch = int(sys.argv[4])
    gap = int(sys.argv[5])
    matrix = create_matrix(rows, cols, seq1, seq2)
    matrix = scoring_matrix(match, mismatch, gap)
    # for n in range(len(matrix)):
    #     print ("{}\n".format(matrix[n]))

    df = pandas.DataFrame(matrix)
    print(df)