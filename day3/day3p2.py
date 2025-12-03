with open("test.txt") as f:
    data = f.read().split('\n')

tot = 0

DIGITS=12
for row in data:
    rlen = len(row)
    best = ""
    for i in range(rlen-1,-1,-1):
        best = row[i] + best
    
    print(best[:DIGITS])
