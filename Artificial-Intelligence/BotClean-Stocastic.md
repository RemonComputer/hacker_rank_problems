# Bot Clean Stocastic 

## Link:

https://www.hackerrank.com/challenges/botcleanr?hr_b=1

## Explaination:

Make the bot move towards the dirt

## Code:

```

#!/bin/python3

def get_dirty_position(board):
    n = len(board)
    for idx_y in range(n):
        for idx_x in range(n):
            if board[idx_y][idx_x] == 'd':
                return (idx_y, idx_x)
            
def nextMove(posr, posc, board):
    robot_y = posr
    robot_x = posc
    dirt_y, dirt_x = get_dirty_position(board)
    delta_y = dirt_y - robot_y
    delta_x = dirt_x - robot_x
    if delta_y < 0:
        print("UP")
    elif delta_y > 0:
        print("DOWN")
    elif delta_x < 0:
        print("LEFT")
    elif delta_x > 0:
        print("RIGHT")
    else:
        print("CLEAN")
    print("")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)

```
