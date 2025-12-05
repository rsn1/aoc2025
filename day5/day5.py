with open("input.txt") as f:
    data = [x.split('\n') for x in f.read().split('\n\n')]

ranges = [tuple(map(int,x.split('-'))) for x in data[0]]
numbers = [int(x) for x in data[1]]

tot = 0
for x in numbers:
    for low,high in ranges:
        if x >= low and x <= high:
            tot += 1
            break

print(tot)
