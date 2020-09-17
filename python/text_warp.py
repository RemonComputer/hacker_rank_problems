# Link: https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap
import math

def wrap(string, max_width):
    number_of_lines = int(math.ceil(len(string)/max_width))
    lines = []
    for line_idx in range(number_of_lines):
        lines.append(string[line_idx * max_width: (line_idx + 1) * max_width])
    return '\n'.join(lines)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
