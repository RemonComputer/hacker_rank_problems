# Bot saves princess-2 

## Link:

https://www.hackerrank.com/challenges/saveprincess2

## Explaination:

Make one move towards the princess, The princess is randomly initialized at any position and the bot is randomly initialized at any position 

## Code:

```

#

def find_princess_position(grid):
    n = len(grid)
    for idx_y in range(n):
        for idx_x in range(n):
            if grid[idx_y][idx_x] == 'p':
                return (idx_y, idx_x)
            
def nextMove(n,r,c,grid):
    princess_y, princess_x = find_princess_position(grid)
    bot_y = r
    bot_x = c
    delta_y = princess_y - bot_y
    if delta_y < 0:
        return "UP"
    if delta_y > 0:
        return "DOWN"
    delta_x = princess_x - bot_x
    if delta_x < 0:
        return "LEFT"
    if delta_x > 0:
        return "RIGHT"
        
    return ""

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))

```
