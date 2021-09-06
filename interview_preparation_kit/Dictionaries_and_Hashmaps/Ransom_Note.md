# Ransom Note

## Link:
https://www.hackerrank.com/challenges/ctci-ransom-note/problem


## Explaination:



## Code:

```
#!/bin/python3

import math
import os
import random
import re
import sys

def countWords(word_list):
    word_list_dict = {}
    for word in word_list:
        if word not in word_list_dict:
            word_list_dict[word] = 0
        word_list_dict[word] += 1
    #print(word_list_dict)
    return word_list_dict

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_word_count = countWords(magazine)
    note_word_count = countWords(note)
    for word, count in note_word_count.items():
        if (word not in magazine_word_count) or (count > magazine_word_count[word]):
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

```
