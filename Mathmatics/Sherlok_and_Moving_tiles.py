 #!/bin/python3
# Link: 
import os
import sys
import math

#
# Complete the movingTiles function below.
# https://www.hackerrank.com/challenges/sherlock-and-moving-tiles/problem

def movingTiles(l, s1, s2, queries):
    #
    # Write your code here.
    #
    if s1 > s2:
        delta_S = s1 - s2
    else:
        delta_S = s2 - s1
    denomenator = delta_S * math.cos(math.pi/4)
    t = [(l - math.sqrt(q_i))/denomenator for q_i in queries]
    return t

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lS1S2 = input().split()

    l = int(lS1S2[0])

    s1 = int(lS1S2[1])

    s2 = int(lS1S2[2])

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

