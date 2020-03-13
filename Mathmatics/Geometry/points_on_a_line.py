#!/bin/python3

# Link: https://www.hackerrank.com/challenges/points-on-a-line/problem

import math
import os
import random
import re
import sys


def isHorizontalLine(points):
    x_first = points[0][0]
    for x_i, _ in points[1:]:
        if x_i != x_first:
            return False
    return True

def isVerticalLine(points):
    y_first = points[0][1]
    for _, y_i in points[1:]:
        if y_i != y_first:
            return False
    return True

def testCondition(points):
    if isHorizontalLine(points) or isVerticalLine(points):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    n = int(input())

    points = []
    for n_itr in range(n):
        xy = input().split()

        x = int(xy[0])

        y = int(xy[1])
        points.append((x, y))
    testCondition(points)

