#!/bin/python3
# Link: https://www.hackerrank.com/challenges/lowest-triangle/problem

import sys
import math

def lowestTriangle(base, area):
    # Complete this function
    float_height = 2 * area / base
    return int(math.ceil(float_height))

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
