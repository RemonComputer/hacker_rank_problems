# Arrays: Left Rotation 

## Link:

https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

## Explaination:

Left rotation on the original Array

## Code:

```

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    a_length = len(a)
    output_arr = []
    for idx_i in range(a_length):
        idx_orig = (idx_i + d) % a_length
        output_arr.append(a[idx_orig])
    return output_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


```
