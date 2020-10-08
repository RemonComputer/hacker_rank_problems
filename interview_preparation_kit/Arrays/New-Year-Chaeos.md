# New Year Chaos 

## Link: https://www.hackerrank.com/challenges/new-year-chaos/problem



## Explaination:

Solved by three solutions:

- First is fast but failed with 3rd test case
- Second passes all test cases but it is slow for the Submit test cases
- Third is the optimized solution that passes all the cases and it is solved by simulating the bribing process and counting bribes

## Code:

```

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes_failed_with_cases(q):
    n_bribes = 0
    for idx in range(len(q)):
        stiker_shoud_be = idx + 1
        current_person_stiker = q[idx]
        if current_person_stiker > stiker_shoud_be: # bibes happened
            # print(f"Condition happened at {idx}")
            current_bribes = current_person_stiker - stiker_shoud_be 
            # print(f"Current Bribes: {current_bribes} at {stiker_shoud_be}") 
            if current_bribes > 2:
                print('Too chaotic')
                return
            n_bribes += current_bribes
    print(n_bribes)

def count_smaller_elements_before_it(q, idx):
    target_el = q[idx]
    n_smaller_elements = 0
    sub_array = q[idx +1:]
    for el in sub_array:
        if el < target_el:
            n_smaller_elements += 1
    return n_smaller_elements

def minimumBribes_that_needs_optimization(q):
    n_bribes = 0
    for idx_i in range(len(q)):
        current_n_bibes = count_smaller_elements_before_it(q, idx_i)
        if current_n_bibes > 2:
            print('Too chaotic')
            return
        n_bribes += current_n_bibes
    print(n_bribes)

def  estimate_number_of_transitions(start_idx, max_search_transitions, target_element, arr):
    # n_transitions = -1
    max_search_idx = min(start_idx + max_search_transitions, len(arr) - 1)
    # print("Estimating Number of Transitions")
    # print(f"Searching from {start_idx + 1} to {max_search_idx + 1}")
    for idx_i in range(start_idx + 1, max_search_idx + 1):
        if arr[idx_i] == target_element:
            return idx_i - start_idx
    return -1

def make_one_bribe(arr, bribe_el_idx):
    temp = arr[bribe_el_idx]
    arr[bribe_el_idx] = arr[bribe_el_idx - 1]
    arr[bribe_el_idx - 1] = temp

# solved by  simulating the bribing process
def minimumBribes(q):
    q_len = len(q)
    modified_array = list(range(1, q_len + 1))
    checking_idx = 0
    n_bribes = 0
    while checking_idx < q_len:
        # the element has not modified
        if q[checking_idx] == modified_array[checking_idx]:
            checking_idx += 1
            continue
        # print(f"Current q: {q}")
        # print(f"Current line: {modified_array}, checking at: {checking_idx}")
        current_element = modified_array[checking_idx]
        target_element = q[checking_idx]
        current_bribes = estimate_number_of_transitions(checking_idx, 2, target_element, modified_array)
        # print(f"estimated current bribes: {current_bribes}")
        if current_bribes == -1:
            print("Too chaotic")
            return
        n_bribes += current_bribes
        current_target_element_idx = checking_idx + current_bribes
        for _ in range(current_bribes):
            make_one_bribe(modified_array, current_target_element_idx)
            current_target_element_idx -= 1
            # print(f"After Bribing: {modified_array}")
        checking_idx += 1
    print(n_bribes)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)


```
