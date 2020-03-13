# Link: https://www.hackerrank.com/challenges/python-string-formatting/problem

import math

def print_formatted(number):
    number_binary_width = math.floor(math.log(number, 2) + 1)
    for num in range(1, number + 1):
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(num, width=number_binary_width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
