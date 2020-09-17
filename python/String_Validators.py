# Link: https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    has_digits = False
    has_lowercase = False
    has_uppercase = False
    str_idx = 0
    condition = (not has_digits or not has_lowercase or not has_uppercase) and (str_idx < len(s)) 
    while condition:
        current_char = s[str_idx]
        if '0' <= current_char <= '9':
            has_digits = True
        elif 'a' <= current_char <= 'z':
            has_lowercase = True
        elif 'A' <= current_char <= 'Z':
            has_uppercase = True
        str_idx += 1
        condition = (not has_digits or not has_lowercase or not has_uppercase) and (str_idx < len(s))
    has_alphabetic = has_lowercase or has_uppercase
    has_alphanumeric = has_alphabetic or has_digits
    print(has_alphanumeric)
    print(has_alphabetic)
    print(has_digits)
    print(has_lowercase)
    print(has_uppercase)
