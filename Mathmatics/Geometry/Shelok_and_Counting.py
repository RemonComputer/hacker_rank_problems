#!/bin/python3
# Link: https://www.hackerrank.com/challenges/sherlock-and-counting/problem

import os
import sys
import math

# Complete the solve function below.
def solve(n, k):
    under_root_term = n ** 2 - 4 * n * k
    # the equation has imaginary roots, it doesn't touch the x-axis
    if under_root_term <= 0:
        return n - 1 # all positive numberss smaller than n can satisfy the equation
    number_of_positive_integers_satisfying_equ = 0
    first_root = (n - math.sqrt(under_root_term)) / 2
    first_int_root = math.floor(first_root)
    second_root = (n + math.sqrt(under_root_term)) / 2
    second_int_root = math.ceil(second_root)
    if first_int_root < 0 and second_int_root <= 0:
        return n - 1
    elif first_int_root <= 0: # and of course the second is greater than zero
        if second_int_root < n:
            return n - second_int_root
        else:
            return 0
    else: # they are both greater than zeros
        number_of_positive_integers_satisfying_equ += first_int_root - 0
        if second_int_root < n:
            number_of_positive_integers_satisfying_equ += n - second_int_root
        return number_of_positive_integers_satisfying_equ

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = solve(n, k)

        fptr.write(str(result) + '\n')

    fptr.close()

