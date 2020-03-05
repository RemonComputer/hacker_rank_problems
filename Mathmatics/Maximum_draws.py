#!/bin/python3
# Link: https://www.hackerrank.com/challenges/maximum-draws/problem
import os
import sys

#
# Complete the maximumDraws function below.
#
def maximumDraws(n):
    #
    # Write your code here.
    #
    if n == 1:
        return 2
    else:
        return n + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = maximumDraws(n)

        fptr.write(str(result) + '\n')

    fptr.close()

