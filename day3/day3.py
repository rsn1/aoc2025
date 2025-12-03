with open("input.txt") as f:
    data = f.read().split('\n')

tot = 0

for row in data:
    biggest = 0
    rlen = len(row)
    for i in range(rlen-1):
        for j in range(i,rlen):
            if i != j:
                first = row[i]
                second = row[j]
                cur = int(first + second)
                if cur > biggest:
                    biggest = cur
    tot += biggest

print(tot)