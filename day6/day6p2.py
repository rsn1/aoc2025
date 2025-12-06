import math
from collections import defaultdict

with open("input.txt") as f:
    data = [list(x) for x in f.read().split('\n')]

N_ROWS, N_COLS = len(data), len(data[0])
dictlist = defaultdict(list)
index = 0
#parse all numbers columnwise
for j in range(N_COLS):
    n_empty = 0
    current_number = ""
    for i in range(N_ROWS):
        val = data[i][j]
        if val == ' ':
            n_empty += 1
            continue
        if val in ['*','+']:
            dictlist[index].insert(0,val)
            continue
        current_number = current_number + val
    if n_empty == N_ROWS:
        #all empty column
        index += 1
        continue
    dictlist[index].append(int(current_number))

#parsing done, add/multiply the numbers
ans = 0
for _, numbers in dictlist.items():
    operand = numbers[0]
    if operand == '+':
        ans += sum(numbers[1:])
    else:
        ans += math.prod(numbers[1:])

print(ans)

