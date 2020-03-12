# Link: https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    new_char_array = []
    for c in s:
        if 'a' <= c <= 'z':
            new_char = chr(ord(c) - ord('a') + ord('A'))
        elif 'A' <= c <= 'Z':
            new_char = chr(ord(c) - ord('A') + ord('a'))
        else:
            new_char = c
        new_char_array.append(new_char)
    return ''.join(new_char_array)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
