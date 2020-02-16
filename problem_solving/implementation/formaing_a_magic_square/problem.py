# link: https://www.hackerrank.com/challenges/magic-square-forming/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import math
import os
import random
import re
import sys
from copy import deepcopy
import heapq

def isMagicSquare(s):
    m = s[0][0] + s[0][1] + s[0][2] # magic_number
    
    # checking rows sums
    for row in s:
        row_sum = 0
        for row_element in row:
            row_sum += row_element
        if row_sum != m:
            return False
    for row_idx in range(3):
        col_sum = 0
        for col_idx in range(3):
            col_sum += s[col_idx][row_idx]
        if col_sum != m:
            return False
    if s[0][0] + s[1][1] + s[2][2] != m:
        return False
    if s[0][2] + s[1][1] + s[2][0] != m:
        return False
    return True

class Path:
    def __init__(self, initial_state, initial_vertex):
        self.current_state = deepcopy(initial_state)
        self.ordered_vertices = [initial_vertex]
        self.cost = 0
        self.visited_vertices = set([initial_vertex])
    
    def addVertex(self, next_vertex):
        last_vertex = self.ordered_vertices[-1]
        self.cost += abs(self.current_state[last_vertex[0]][last_vertex[1]] - self.current_state[next_vertex[0]][next_vertex[1]])
        self.visited_vertices.add(next_vertex)
        self.ordered_vertices.append(next_vertex)
        tmp_val = self.current_state[next_vertex[0]][next_vertex[1]]
        self.current_state[next_vertex[0]][next_vertex[1]] = self.current_state[last_vertex[0]][last_vertex[1]]
        self.current_state[last_vertex[0]][last_vertex[1]] = tmp_val
    
    def expandPath(self):
        for i in range(3):
            for j in range(3):
                next_vertex = (i,j)
                if next_vertex not in self.visited_vertices:
                    new_path = deepcopy(self)
                    new_path.addVertex(next_vertex)
                    yield new_path
    
    def isCompletePath(self):
        return isMagicSquare(self.current_state)
    
    def __lt__(self, other):
        return self.cost < other.cost
    
    def __le__(self, other):
        return self.cost <= other.cost
    
    def __repr__(self):
        return str(self.ordered_vertices)

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    min_heap = []
    # Multi-point Dijekstra Algorithm
    # adding the initial paths
    for i in range(3):
        for j in range(3):
            initial_vertex = (i, j)
            new_path = Path(s, initial_vertex)
            #print(initial_vertex)
            #print(new_path.cost)
            heapq.heappush(min_heap, new_path)
    print(min_heap)
    while len(min_heap) > 0:
        current_path = heapq.heappop(min_heap)
        print(current_path)
        if current_path.isCompletePath():
            return current_path.cost
        for child_path in current_path.expandPath():
            heapq.heappush(min_heap, child_path)
    print('Path not found')

# I simply mis-understood the problem
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = [[5, 9, 2], [3, 4, 7], [8, 1, 5]]

    # for _ in range(3):
    #     s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
