# Link: https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    # your code goes here
    for idx_start in range(0, len(string), k):
        substring = string[idx_start : idx_start + k]
        new_substring = []
        previous_encontered_chars = set()
        for char in substring:
            if char not in previous_encontered_chars:
                new_substring.append(char)
                previous_encontered_chars.add(char)
        print("".join(new_substring))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
