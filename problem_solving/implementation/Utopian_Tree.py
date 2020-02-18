#!/bin/python3
# Link: https://www.hackerrank.com/challenges/utopian-tree/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    height = 1
    for season_idx in range(n):
        if season_idx % 2 == 0:
            height *= 2
        else:
            height += 1
    return height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
