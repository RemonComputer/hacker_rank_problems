# Strange Grid Again
## Link:
https://www.hackerrank.com/challenges/strange-grid/problem


## Explaination:

- Every Odd Row First Element is multiple of 10
- Every Even Row First Element is one plus its last Odd Row First Element
- Every Elmenet in a specific coloumn is two plus the previous coloumn

## Code:

```
#!/bin/python3

import os
import sys


def get_value_from_first_number_in_row(first_number, col_number):
    # if row_number == 1:
    #     return first_number
    # else:
    #     return first_number + (col_number - 1) * 2
    return first_number + (col_number - 1) * 2

def calculate_first_number_in_odd_row(row_number):
    # accmulator = 0
    # for _ in range(0, row_number, 2):
    #     last_element_in_even_row = (accmulator + 1) + 8
    # accmulator += 1
    # return accmulator
    return (row_number - 1) // 2 * 10

def calculate_first_number_in_row(row_number):
    if row_number % 2 == 0:
        last_odd_number_first_element = calculate_first_number_in_odd_row(row_number - 1)
        return last_odd_number_first_element + 1
    else:
        return calculate_first_number_in_odd_row(row_number)
#
# Complete the strangeGrid function below.
#
def strangeGrid(r, c):
    #
    # Write your code here.
    #
    first_number_in_row = calculate_first_number_in_row(r)
    print(first_number_in_row)
    return get_value_from_first_number_in_row(first_number_in_row, c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rc = input().split()

    r = int(rc[0])

    c = int(rc[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()

```
