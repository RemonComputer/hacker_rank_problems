# link: https://www.hackerrank.com/challenges/picking-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a=sorted(a)
    counts = {}
    for el in a:
        counts[el] = counts.get(el, 0) + 1
    numbers = list(counts.keys())
    max_subset_len = max(counts.values())
    for num_idx in range(len(numbers) - 1):
        first_num = numbers[num_idx]
        second_num = numbers[num_idx + 1]
        diff = second_num - first_num
        if diff <= 1:
            subset_len = counts[first_num] + counts[second_num]
            if subset_len > max_subset_len:
                max_subset_len = subset_len
    # if max_subset_len > 5:
    #     max_subset_len = 5
    return max_subset_len
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

