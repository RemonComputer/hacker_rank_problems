# PACMan - DFS 

## Link:

https://www.hackerrank.com/challenges/pacman-dfs/problem

## Explaination:

Depth First search using a stack

## Notes:

I cannot access the sample answer and hackerrank says that my answer is incorrect although I believe it is correct.

## Code:

```

def get_illegal_moves_set(grid, grid_n_y, grid_n_x):
    s = set()
    for idx_y in range(grid_n_y):
        for idx_x in range(grid_n_x):
            if grid[idx_y][idx_x] == '%':
                s.add((idx_y, idx_x))
    return s

if __name__ == '__main__':
    pacman_y, pacman_x = (int(x) for x in input().split())
    food_y, food_x = (int(x) for x in input().split())
    grid_n_y, grid_n_x = (int(x) for x in input().split())
    grid = []
    for _ in range(grid_n_y):
        grid.append(input())
    illegal_moves = get_illegal_moves_set(grid, grid_n_y, grid_n_x)
    stack = [(pacman_y, pacman_x, None)]
    illegal_moves.add((pacman_y, pacman_x)) # add the robot position because it is now on the stack
    n_explored = 0
    moves_deltas = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    explored_nodes = []
    while len(stack) > 0:
        next_node = stack.pop()
        n_explored += 1
        explored_nodes.append((next_node[0], next_node[1]))
        if next_node[0] == food_y and next_node[1] == food_x:
            found_food_node = next_node
            break
        for move_delta_y, move_delta_x in moves_deltas:
            new_y = next_node[0] + move_delta_y
            new_x = next_node[1] + move_delta_x
            if (new_y, new_x) not in illegal_moves:
                      stack.append((new_y, new_x, next_node))
                      illegal_moves.add((new_y, new_x))
    last_node = found_food_node
    path = []
    while last_node != None:
        path.append((last_node[0], last_node[1]))
        last_node = last_node[2]
    path.reverse()
    print(f"{n_explored}")
    for idx_y, idx_x in explored_nodes:
        print(f"{idx_y} {idx_x}")
    print(f"{len(path) - 1}")
    for idx_y, idx_x in path:
        print(f"{idx_y} {idx_x}")

```
