with open("input.txt") as f:
    data = [list(x) for x in f.read().split('\n')]

N_ROWS = len(data)
N_COLS = len(data[0])
print(f"ROWS,COLS: {N_ROWS},{N_COLS}")
def adj8(i,j):
    adj = []
    for di,dj in [(x,y) for x in range(-1,2) for y in range(-1,2) if (x,y) != (0,0)]:
        newi,newj = i+di,j+dj
        if newi < N_ROWS and newi > -1 and newj < N_COLS and newj > -1:
            adj.append((newi,newj))
    return adj

def removable_papers(grid):
    removable = []
    for i in range(N_ROWS):
        for j in range(N_COLS):
            if data[i][j] == '@':
                num_adjacent_forklifts = 0
                valid_adjacent_indices = adj8(i,j)
                for x,y in valid_adjacent_indices:
                    if data[x][y] == '@':
                        num_adjacent_forklifts += 1
                if num_adjacent_forklifts < 4:
                    removable.append((i,j))
    return removable

def remove_papers(grid, to_remove):
    for (i,j) in to_remove:
        grid[i][j] = '.'
    
gridcpy = data[:]

tot = 0
while True:
    removable = removable_papers(gridcpy)
    remove_papers(gridcpy,removable)
    tot += len(removable)
    if len(removable) == 0:
        break

print(gridcpy)
print(tot)