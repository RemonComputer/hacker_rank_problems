# Link: https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    new_chars = []
    current_char = s[0]
    if 'a' <= current_char <= 'z':
        current_char = chr(ord(current_char) - ord('a') + ord('A'))
    new_chars.append(current_char)
    for char_idx in range(1, len(s)):
        previous_char = s[char_idx - 1]
        current_char = s[char_idx]
        if previous_char == ' ' and 'a' <= current_char <= 'z': 
            current_char = chr(ord(current_char) - ord('a') + ord('A'))
        new_chars.append(current_char)
    result = "".join(new_chars)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

