#!/bin/python3
# Link: https://www.hackerrank.com/challenges/rectangular-game/problem

import os
import sys

# Complete the solve function below.
def solve(steps):
    min_y = min(steps, key=lambda el:el[0])[0]
    min_x = min(steps, key=lambda el:el[1])[1]
    return min_y * min_x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    steps = []

    for _ in range(n):
        steps.append(list(map(int, input().rstrip().split())))

    result = solve(steps)

    fptr.write(str(result) + '\n')

    fptr.close()

