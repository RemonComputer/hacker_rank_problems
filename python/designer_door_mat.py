# Link: https://www.hackerrank.com/challenges/designer-door-mat/problem

def draw_upper_part_lock_line(m, line_idx):
    number_of_or_sign = 1 + 2 * line_idx
    intermidiate_or_signs = '..'.join(['|'] * number_of_or_sign)
    middle_locks = '.' + intermidiate_or_signs + '.'
    lock_line = middle_locks.center(m, '-')
    print(lock_line)

def draw_lock_map(n, m):
    upper_lock_map_height = n // 2
    # drawing upper lock map lines
    for line_idx in range(upper_lock_map_height):
        draw_upper_part_lock_line(m, line_idx)
    # drawing the Welcome message
    print('WELCOME'.center(m, '-'))
    for line_idx in range(upper_lock_map_height - 1, -1, -1):
        draw_upper_part_lock_line(m, line_idx)

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    tokens = input().split()
    n = int(tokens[0])
    m = int(tokens[1])
    draw_lock_map(n, m)
