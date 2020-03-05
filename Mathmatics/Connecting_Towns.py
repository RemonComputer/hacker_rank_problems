#!/bin/python3

# Link: https://www.hackerrank.com/challenges/connecting-towns/problem

import os
import sys

#
# Complete the connectingTowns function below.
#
def connectingTowns(n, routes):
    #
    # Write your code here.
    #
    n_routes = 1
    for n_i in routes:
        n_routes *= n_i
    return n_routes % 1234567

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)

        fptr.write(str(result) + '\n')

    fptr.close()

