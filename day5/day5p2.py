with open("input.txt") as f:
    data = [x.split('\n') for x in f.read().split('\n\n')]

ranges = [tuple(map(int,x.split('-'))) for x in data[0]]

sorted_ranges = sorted(ranges, key=lambda x: x[0] )

filtered = [sorted_ranges[0]]
for low,high in sorted_ranges[1:]:
    prev_low, prev_high = filtered[-1]
    if low <= prev_high:
        filtered[-1] = (prev_low, max(prev_high,high))
    else:
        filtered.append((low,high))

tot = 0
for low,high in filtered:
    tot += high-low+1

print(tot)