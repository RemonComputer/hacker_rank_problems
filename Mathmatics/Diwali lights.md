# Diwali Lights

## Link:

https://www.hackerrank.com/challenges/diwali-lights/problem

## Explaination

- Simple Premutation problem -> 2 ** n
- Only Exception is the all zero case so it is -> 2 ** n -1
- The answer needs to be modulo 10 ** 5 so it is (2 ** n - 1) % (10 ** 5)   








## Code:

```
#!/bin/python3

import os
import sys

#
# Complete the lights function below.
#
def lights(n):
    #
    # Write your code here.
    #
    return (2 ** n - 1) % (10 ** 5)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = lights(n)

        fptr.write(str(result) + '\n')

    fptr.close()
```
