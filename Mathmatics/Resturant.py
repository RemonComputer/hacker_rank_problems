#!/bin/python3
# Link: https://www.hackerrank.com/challenges/restaurant/problem

import os
import sys


def get_highest_common_multiple(l, b):
    if l > b:
        start_number = b
    else:
        start_number = l
    while start_number > 1:
        if l % start_number == 0 and b % start_number == 0:
            break
        start_number -= 1
    return start_number
#
# Complete the restaurant function below.
#
def restaurant(l, b):
    #
    # Write your code here.
    #
    highest_common_multiple = get_highest_common_multiple(l, b)
    l_silces = l // highest_common_multiple
    b_sicles = b // highest_common_multiple
    return l_silces * b_sicles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        lb = input().split()

        l = int(lb[0])

        b = int(lb[1])

        result = restaurant(l, b)

        fptr.write(str(result) + '\n')

    fptr.close()

