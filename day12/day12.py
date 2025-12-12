with open("input.txt") as f:
    data = f.read().split('\n\n')

questions = [x.split(': ') for x in data[-1].splitlines()]

ans = 0
for grid,presents in questions:
    w,h = grid.split('x')
    area = int(w)*int(h)
    n_regions = int(area/9)
    presents = [int(x) for x in presents.split(' ')]
    poss = True
    for present in presents:
        n_regions -= present
        if n_regions < 0:
            poss = False
            break
    if poss:
        ans += 1

print(ans)
