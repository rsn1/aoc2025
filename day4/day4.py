with open("input.txt") as f:
    data = f.read().split('\n')

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

tot = 0
for i in range(N_ROWS):
    for j in range(N_COLS):
        if data[i][j] == '@':
            num_adjacent_forklifts = 0
            valid_adjacent_indices = adj8(i,j)
            for x,y in valid_adjacent_indices:
                if data[x][y] == '@':
                    num_adjacent_forklifts += 1
            if num_adjacent_forklifts < 4:
                tot += 1

print(tot)