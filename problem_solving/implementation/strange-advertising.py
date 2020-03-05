#!/bin/python3

# link: https://www.hackerrank.com/challenges/strange-advertising/problem
import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    lastDaySharedCount = 5
    sumLiked = 0
    shareFactor = 3
    for _ in range(n):
        currentLiked = lastDaySharedCount // 2
        sumLiked += currentLiked
        lastDaySharedCount = currentLiked * shareFactor
    return sumLiked

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

