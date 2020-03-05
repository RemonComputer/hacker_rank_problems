#!/bin/python3
# Link: https://www.hackerrank.com/challenges/leonardo-and-prime/problem

import os
import sys


def isPrime(prime_factors, n):
    for factor in prime_factors:
        if n % factor == 0:
            return False
    return True

#
# Complete the primeCount function below.
#
def primeCount(n):
    #
    # Write your code here.
    #
    if n <= 1:
        return 0
    prime_factors = [2]
    product=2
    current_number = 2
    while product <= n:
        current_number += 1
        if isPrime(prime_factors, current_number):
            prime_factors.append(current_number)
            product *= current_number
    return len(prime_factors) - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()

