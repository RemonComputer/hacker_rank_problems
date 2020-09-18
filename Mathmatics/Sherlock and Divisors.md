# Sherlock and Divisors

## Explaination

- You Should loop for divisors unitl you hit sqrt(n) -> this is a know trick
- When the divisors are the same don't increase the count 2 times just 1 time

## Code:

```
#!/bin/python3

import os
import sys
import math
#
# Complete the divisors function below.
#
def divisors(n):
    #
    # Write your code here.
    #
    divisor_cnt = 0
    n_sqrt_floor = math.floor(math.sqrt(n))
    for i in range(1, n_sqrt_floor + 1):
        if n % i == 0:
            divisor_1 = i
            divisor_2 = n // i
            if divisor_1 % 2 == 0:
                divisor_cnt += 1
            if divisor_2 % 2 == 0 and (divisor_2 != divisor_1):
                divisor_cnt += 1
    return divisor_cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = divisors(n)

        fptr.write(str(result) + '\n')

    fptr.close()

```
