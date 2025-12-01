with open("input.txt") as f:
    data = f.read().split('\n')

cur = 50
ans = 0
for x in data:
    to_rotate = int(x[1:])
    if x[0] == 'L':
        for i in range(to_rotate):
            cur = cur - 1
            if cur == -1:
                cur = 99
            if cur == 0:
                ans += 1
    elif x[0] == 'R':
        for i in range(to_rotate):
            cur = cur + 1
            if cur == 100:
                cur = 0
                ans += 1
