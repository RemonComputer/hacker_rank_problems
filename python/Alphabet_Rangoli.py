# Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def compute_board_width(size):
    # I am calculating the board size from the middle line
    # in the middle line you will see the first charcter (this accounts for 1) and
    # (size - 1) charcters on it's left and right, this accounts for (size - 1) * 2
    # and for each charcter there is an associates '-' so the number of charcters with
    # dashes becomes (size - 1) * 2 * 2, so the total count is 1 + (size - 1) * 2 * 2 
    return 1 + (size - 1) * 2 * 2 

def print_upper_rangholi_line(board_width, line_idx, size):
    start_character = chr(size - 1 + ord('a'))
    if line_idx == 0:
        middle_area = start_character
    else:
        middle_charcters = []
        # putting the up rising charcaters
        for char_idx in range(line_idx):
            middle_charcters.append(chr(ord(start_character) - char_idx))
        # putting the middle character
        middle_character = chr(ord(start_character) - line_idx)
        middle_charcters.append(middle_character)
        for char_idx in range(line_idx):
            middle_charcters.append(chr(ord(middle_character) + char_idx + 1))
        middle_area = '-'.join(middle_charcters)
    line = middle_area.center(board_width, '-')
    print(line)

def print_rangoli(size):
    board_width = compute_board_width(size)
    upper_height = size - 1
    # printing the upper part
    for line_idx in range(upper_height):
        print_upper_rangholi_line(board_width, line_idx, size)
    # printing the middle line
    print_upper_rangholi_line(board_width, upper_height, size)
    # printing the bottom part
    for line_idx in range(upper_height - 1, -1, -1):
        print_upper_rangholi_line(board_width, line_idx, size)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
