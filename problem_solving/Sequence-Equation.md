# Sequence Equation 

## Link:
https://www.hackerrank.com/challenges/permutation-equation/problem


## Explaination:

Since the numbers are unique and from 1 to n, then their inverse will also be unqie and from 1 to n,
So I map the function in forward way and put the inverse to be the required array.

## Code:

```
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    inverse_permutation = [0] * len(p)
    for p_i in p:
        x = p[p[p_i - 1] - 1]
        inverse_permutation[x - 1] = p_i
    return inverse_permutation

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

```
