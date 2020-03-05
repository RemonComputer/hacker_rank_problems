#!/bin/python3

# Link: https://www.hackerrank.com/challenges/game-with-cells/problem
import os
import sys

#
# Complete the gameWithCells function below.
#
def gameWithCells(n, m):
    #
    # Write your code here.
    #
    if n % 2 == 0:
        rows_points = n // 2
    else:
        rows_points = (n + 1) // 2
    if m % 2 == 0:
        column_points = m // 2
    else:
        column_points = (m + 1) // 2
    return rows_points * column_points

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()

