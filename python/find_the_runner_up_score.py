# Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

def get_runner_up_score(arr):
    arr = list(set(arr))
    if arr[0] > arr[1]:
        first_max = arr[0]
        second_max = arr[1]
    else:
        first_max = arr[1]
        second_max = arr[0]
    # first_max = -101
    # second_max = -101
    for a_i in arr[2:]:
        if a_i > second_max and a_i < first_max:
            second_max = a_i
            # print('first_max: ', first_max, 'second_max:', second_max)
        elif a_i > first_max:
            second_max = first_max
            first_max = a_i
            # print('first_max: ', first_max, 'second_max:', second_max)
    return second_max
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_runner_up_score(arr))
