# Reverse Game: 

## Link: 

https://www.hackerrank.com/challenges/reverse-game/problem)

## Explaination:

Try to notice the pattern when solving for N=3, N=5 and N=4

### For N=3

```
0 1 2
2 1 0
2 0 1
2 0 1
```
### For N=5

```
0 1 2 3 4
4 3 2 1 0
4 0 1 2 3
4 0 3 2 1
4 0 3 1 2
4 0 3 1 2
```

### For N=4

```
0 1 2 3
3 2 1 0
3 0 1 2
3 0 2 1
3 0 2 1
```

## Code:

```
#!/bin/python3

import math
import os
import random
import re
import sys

# def construct_final_array(n):
#     final_array = [0] * n
#     if n % 2 == 0:
#         last_idx = n
#         for i in range(0, n-1, 2):

def get_ball_idx(n, k):
    if n % 2 == 0:
        if k < n // 2:
            return (k + 1) * 2 - 1
        else:
            k = k - n // 2
            reversed_idx = (k + 1) * 2 - 1
            true_idx = (n - 1) - reversed_idx
            return true_idx
    else:
        if k < n // 2:
            return (k + 1) * 2 - 1
        else:
            k = k - n // 2
            reversed_idx = k * 2
            true_idx = (n - 1) - reversed_idx
            return true_idx

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        print(get_ball_idx(n, k))
```

