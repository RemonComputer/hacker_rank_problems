# Circular Array Rotation 

## Link:
https://www.hackerrank.com/challenges/circular-array-rotation/problem



## Explaination:

When rotating by `k`, `idx` will be `(idx + k) % n`, so if the new index is `idx1` the index before rotation will be `(idx1 - k) % n`.


## Code:

```
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    resulted_elements = []
    n = len(a)
    for q_i in queries:
        idx_before_rotation = (q_i - k) % n
        resulted_elements.append(a[idx_before_rotation])
    return resulted_elements

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
```
