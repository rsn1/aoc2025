import functools

with open("input.txt") as f:
    grid = [list(x) for x in f.read().split('\n')]

N_ROWS, N_COLS = len(grid), len(grid[0])
print(N_ROWS,N_COLS)

def find_start(grid):
    for i in range(N_ROWS):
        for j in range(N_COLS):
            if grid[i][j] == 'S':
                return (i,j)

def display_grid(grid):
    for i in range(N_ROWS):
        for j in range(N_COLS):
            print(grid[i][j], end='')
        print()

splits = 0
@functools.cache
def recursive_solve(i,j):
    global splits
    if i == N_ROWS:
        #at bottom
        return 1
    if j == N_COLS:
        #outside
        return 0
    if grid[i][j] == '^':
        #solve recursively
        splits += 1
        return recursive_solve(i,j+1) + recursive_solve(i,j-1)
    elif grid[i][j] == '|':
        #Already been here
        #This only works for p2 since im using functools.cache, without it we will get wrong answer
        return 0
    else:
        assert grid[i][j] == '.'
        grid[i][j] = '|'
        return recursive_solve(i+1,j)

starti, startj = find_start(grid)
p2 = recursive_solve(starti+1, startj)

display_grid(grid)
print(f"p1={splits}")
print(f"{p2=}")