# Bot-Saves-Princess 

## Link:

https://www.hackerrank.com/challenges/saveprincess

## Explaination:

Princess in Corner and the Bot in the middle of the Maze and the bot moves towards it

## Code:

```

#!/usr/bin/python

def find_pricess_position(grid):
    n = len(grid)
    possible_positions = [(0,0), (n-1, 0), (n-1, n-1), (0, n-1)]
    for idx_y, idx_x in possible_positions:
        if grid[idx_y][idx_x] == 'p':
            return (idx_y, idx_x)
    return None # Bug

def displayPathtoPrincess(n,grid):
    #print all the moves here
    robot_y = n // 2
    robot_x = n // 2
    princess_y, princess_x = find_pricess_position(grid)
    delta_y = princess_y - robot_y
    delta_x = princess_x - robot_x
    move_y = 'DOWN'
    if delta_y < 0:
        move_y = 'UP'
        delta_y *= -1
    move_x = 'RIGHT'
    if delta_x < 0:
        move_x = 'LEFT'
        delta_x *= -1
    for _ in range(delta_y):
        print(move_y)
    for _ in range(delta_x):
        print(move_x)


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)

```
