# 2D Array - DS 

## Link:

https://www.hackerrank.com/challenges/2d-array/problem?

## Explaination:

calculate the sum of subset of the array and find the max sum

## Code:

```

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_hour_sum = None
    for idx_corner_i in range(len(arr) - 3 + 1):
        for idx_corner_j in range(len(arr[0]) - 3 + 1):
            sum = 0
            for i in range(3):
                for j in range(3):
                    sum += arr[idx_corner_i + i][idx_corner_j + j]
            sum -= arr[idx_corner_i + 1][idx_corner_j + 0]
            sum -= arr[idx_corner_i + 1][idx_corner_j + 2]
            if max_hour_sum == None or sum > max_hour_sum:
                max_hour_sum = sum
                print(f"{idx_corner_i}, {idx_corner_j}")
    return max_hour_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


```
