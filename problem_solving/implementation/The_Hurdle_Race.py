#!/bin/python3
# Link: https://www.hackerrank.com/challenges/the-hurdle-race/problem
import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    
    # getting the max height
    max_height = height[0]
    for el_height in height:
        if el_height > max_height:
            max_height = el_height
    min_dosages = max(0, max_height - k)
    return min_dosages
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
