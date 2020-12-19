#!/bin/python3

import os
import sys
import math

def get_vector_length(translated_vector_head):
    return math.sqrt(translated_vector_head[0] ** 2 + translated_vector_head[1] ** 2 + translated_vector_head[2] ** 2)

def get_translated_vector(point_A, point_B):
    return (point_B[0] - point_A[0], point_B[1] - point_A[1], point_B[2] - point_A[2])

def cross_product(vec_a, vec_b):
    cross_x = vec_a[1] * vec_b[2] - vec_a[2] * vec_b[1]
    cross_y = -(vec_a[0] * vec_b[2] - vec_a[2] * vec_b[0])
    cross_z = vec_a[0] * vec_b[1] - vec_a[1] * vec_b[0] 
    return (cross_x, cross_y, cross_z)

# Complete the solve function below.
def solve(points):
    epsilon = 1e-5
    vectors = [get_translated_vector(points[0], points[1]), get_translated_vector(points[1], points[2]), get_translated_vector(points[2], points[3]), get_translated_vector(points[3], points[0])] # computing the relative vectors
    first_cross_product = cross_product(vectors[0], vectors[1]) # which will produce a vector perpendicular to both vectors (first and second)
    second_cross_product = cross_product(vectors[2], vectors[3]) # which will produce a vector perpendicular to both vectors (second and third)
    final_cross_product = cross_product(first_cross_product, second_cross_product) # should produce the zero vector if both of the first cross product and second cross product are parallel, and in this case the 4 points are in the same plane
    if get_vector_length(final_cross_product) < epsilon:
        return 'YES'
    else:
        return 'NO'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        points = []

        for _ in range(4):
            points.append(list(map(int, input().rstrip().split())))

        result = solve(points)

        fptr.write(result + '\n')

    fptr.close()

