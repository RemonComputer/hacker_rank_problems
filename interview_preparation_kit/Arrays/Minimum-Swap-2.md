# Minimum-Swap-2 

## Link: https://www.hackerrank.com/challenges/minimum-swaps-2/problem



## Explaination: 

This is the Naive Algorithm, use set in the indices to avoid searching in it as as array.


## Code:

```

#!/bin/python3

import math
import os
import random
import re
import sys

# def get_wrong_elements(arr):
#     wrong_elements = []
#     for el_should_be, el in enumerate(arr, start=1):
#         if el_should_be != el:
#             wrong_elements.append(el_should_be)
#     return wrong_elements

# def swap_elements(arr, number_i, number_j):
#     temp = arr[number_i - 1]
#     arr[number_i - 1] = arr[number_j - 1]
#     arr[number_j - 1] = arr[number_i - 1]

# def make_double_hit_swaps(arr, wrong_elements):
#     n_swaps = 0
#     wrong_elements_length = len(wrong_elements)
#     current_wrong_el_idx = 0
#     while current_wrong_el_idx < wrong_elements_length:
#         current_wrong_number_should_be = wrong_elements[current_wrong_el_idx]
#         current_wrong_number_is = arr[current_wrong_number_should_be - 1]
#         second_wrong_number_is = arr[current_wrong_number_is - 1]
#         if current_wrong_number_should_be == second_wrong_number_is:
#             swap_elements(arr, current_wrong_number_is, second_wrong_number_is)
#             n_swaps += 1
#             wrong_elements.remove(current_wrong_number_is)
#             wrong_elements.remove(second_wrong_number_is)
#             wrong_elements_length -= 2
#             print(f"Elements {current_wrong_number_is} and {second_wrong_number_is} are swapped")
#             print(f"current wrong elements: {wrong_elements}")
#             print(f"Current Array is: {arr}")
#         else:
#             current_wrong_el_idx += 1
#     print("Double hit swaps are finished")
#     print(f"Total Double hit swaps is: {n_swaps}")
#     return n_swaps

# def make_two_swaps_trible_hits(arr, wrong_elements):
#     n_swaps = 0
#     wrong_elements_length = len(wrong_elements)
#     current_wrong_el_idx = 0
#     while current_wrong_el_idx < wrong_elements_length:
#         current_wrong_number_should_be = wrong_elements[current_wrong_el_idx]
#         current_wrong_number_is = arr[current_wrong_number_should_be - 1]
#         second_wrong_number_is = arr[current_wrong_number_is - 1]
#         third_wrong_number = arr[second_wrong_number_is - 1]
#         if third_wrong_number == current_wrong_number_should_be:
#             print(f"Found three numbers: {current_wrong_number_is}, {second_wrong_number_is}, {third_wrong_number}")
#             swap_elements(arr, current_wrong_number_should_be, second_wrong_number_is)
#             print(f"After first swap: {arr}")
#             swap_elements(arr, third_wrong_number, second_wrong_number_is)
#             print(f"After second swap: {arr}")
#             n_swaps += 2
#             wrong_elements.remove(current_wrong_number_is)
#             wrong_elements.remove(second_wrong_number_is)
#             wrong_elements.remove(third_wrong_number)
#             wrong_elements_length -= 3
#             print(f"current wrong elements: {wrong_elements}")
#             print(f"Current Array is: {arr}")
#         else:
#             current_wrong_el_idx += 1
#     print("two_swaps_trible_hits are finished")
#     print(f"Total Double hit swaps is: {n_swaps}")
#     return n_swaps

# def make_one_hit_swaps(arr, wrong_elements):
#      n_swaps = 0
#     wrong_elements_length = len(wrong_elements)
#     while wrong_elements_length > 0:
#         current_wrong_element = wrong_elements[0]
#         second_wrong_element = arr[current_wrong_element - 1]
#         swap(arr, current_wrong_element, second_wrong_element)
#         n_swaps += 1


def get_wrong_elements_indices_and_dict(arr):
    wrong_indices = []
    number_vs_index_dict = {}
    for idx, el in enumerate(arr):
        if (idx + 1) != el:
            wrong_indices.append(idx)
            number_vs_index_dict[el] = idx
    return wrong_indices, number_vs_index_dict

    # Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # print(f"Original Array: {arr}")
    # wrong_elements = get_wrong_elements(arr)
    # print(f"Wrong elements: {wrong_elements}")
    # n_swaps = make_double_hit_swaps(arr,  wrong_elements)
    # n_swaps += make_two_swaps_trible_hits(arr, wrong_elements)
    wrong_indices, number_vs_index_dict = get_wrong_elements_indices_and_dict(arr)
    wrong_indices = set(wrong_indices)
    # print(f"Current Array: {arr}")
    # print(f"Wrong indices: {wrong_indices}")
    # print(f"number_vs_index_dict: {number_vs_index_dict}")
    n_swaps = 0
    while len(wrong_indices) > 0:
        current_wrong_index = wrong_indices.pop()
        current_number_should_be = current_wrong_index + 1
        second_number_index = number_vs_index_dict[current_number_should_be]
        arr[second_number_index], arr[current_wrong_index] = arr[current_wrong_index], arr[second_number_index]
        # print(f"Swapping {current_wrong_index} and {second_number_index}")
        # print(f"Current Array is: {arr}")
        n_swaps += 1
        # wrong_indices = wrong_indices[1:]
        # wrong_indices.remove(current_wrong_index)
        del number_vs_index_dict[current_number_should_be]
        if (second_number_index + 1) == arr[second_number_index]:
            wrong_indices.remove(second_number_index)
            del number_vs_index_dict[arr[second_number_index]]
            # print("It is a double hit")
        else:
            number_vs_index_dict[arr[second_number_index]] = second_number_index
        # print(f"Current Wrong indices: {wrong_indices}")
        # print(f"Current number_vs_index_dict: {number_vs_index_dict}")
    return n_swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()


```
