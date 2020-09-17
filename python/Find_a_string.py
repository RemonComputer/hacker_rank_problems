# Link: https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    last_valid_comparison_index = len(string) - len(sub_string)
    repetition_count = 0
    current_comparison_start_idx = 0
    substring_length = len(sub_string)
    while current_comparison_start_idx <= last_valid_comparison_index:
        substring_found = True
        for substring_idx in range(substring_length):
            substring_char = sub_string[substring_idx]
            string_char = string[current_comparison_start_idx + substring_idx]
            if string_char != substring_char:
                 substring_found = False
                 break
        if substring_found:
            current_comparison_start_idx += substring_length - 1
            repetition_count += 1
        else:
            current_comparison_start_idx += 1
    return repetition_count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
