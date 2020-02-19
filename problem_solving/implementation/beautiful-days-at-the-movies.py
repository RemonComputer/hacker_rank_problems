#!/bin/python3

import math
import os
import random
import re
import sys

def reverseNumber(number):
    return int(''.join(reversed(str(number))))

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    beautiful_numbers_count = 0
    for num in range(i, j + 1):
        if abs(num - reverseNumber(num)) % k == 0:
            beautiful_numbers_count += 1
    return beautiful_numbers_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()

