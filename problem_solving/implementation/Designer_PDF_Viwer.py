#!/bin/python3
#Link: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?h_r=next-challenge&h_v=zen
import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    max_letter_height = -1
    for letter in word:
        letter_height = h[ord(letter) - ord('a')]
        if letter_height > max_letter_height:
            max_letter_height = letter_height
    word_length = len(word)
    return word_length * max_letter_height 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()

