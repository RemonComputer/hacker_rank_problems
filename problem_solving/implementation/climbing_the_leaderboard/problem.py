#!/bin/python3
#link: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

# Status: I couldn't solve all the test cases

import math
import os
import random
import re
import sys

def getUniqueScores(scores):
    unique_scores = [scores[0]]
    previous_score = scores[0]
    for score_el in scores[2:]:
        if score_el != previous_score:
            unique_scores.append(score_el)
            previous_score = score_el
    return unique_scores

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores = getUniqueScores(scores)
    alice_positions = []
    highest_alice_position_idx = len(scores)
    for alice_score in alice:
        while highest_alice_position_idx > -1 and alice_score >= scores[highest_alice_position_idx - 1]:
            print(alice_score, ':', highest_alice_position_idx + 1)
            highest_alice_position_idx -= 1
        if highest_alice_position_idx <= -1:
            highest_alice_position_idx = 0
        print('Final alice Position: (',alice_score, ':', highest_alice_position_idx + 1, ')')
        alice_positions.append(highest_alice_position_idx + 1)
    return alice_positions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

