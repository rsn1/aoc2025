from itertools import combinations
from functools import reduce

with open("input.txt") as f:
    data = [x.split(' ') for x in f.read().splitlines()]

total_ans = 0
for line in data:
    lights = line[0]
    lights = lights[1:-1]
    numbers = line[1:-1]
    n_bits = len(lights)
    
    #parse right side
    right_side = []
    for num in numbers:
        parsed_number = 0
        for c in num:
            if c.isdigit():
                parsed_number += 2**(n_bits-1-int(c))
        right_side.append(parsed_number)

    #parse left side
    target_num = 0
    for idx, c in enumerate(lights):
        if c == '#':
            target_num += 2**(n_bits-1-idx)

    #first try press each button alone, then 2 buttons, then 3 etc.
    n_presses = 0
    found = False
    for i in range(1,len(right_side)+1):
        for c in combinations(right_side,i):
            ans = reduce(lambda x, y: x ^ y, c)
            if ans == target_num:
                n_presses = i
                found = True
                break
        if found:
            break

    total_ans += n_presses
print(total_ans)
