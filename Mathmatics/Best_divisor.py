#!/bin/python3
# Link: https://www.hackerrank.com/challenges/best-divisor/problem

import math
import os
import random
import re
import sys

def find_divisors(n):
    divisors = []
    for n_i in range(1, n+1):
        if n % n_i == 0:
            divisors.append(n_i)
    #print(divisors)
    return divisors

def get_divisor_score(d):
    d_str = str(d)
    score = 0
    for d_i in d_str:
        score += int(d_i)
    return score

def get_best_divisor(n):
    divisors = find_divisors(n)
    max_divisor_score = get_divisor_score(divisors[0])
    best_divisor = divisors[0]
    for d_i in divisors[1:]:
        d_i_score = get_divisor_score(d_i)
        if d_i_score > max_divisor_score:
            #print(d_i)
            max_divisor_score = d_i_score
            best_divisor = d_i
    return best_divisor

if __name__ == '__main__':
    n = int(input())
    print(get_best_divisor(n))
