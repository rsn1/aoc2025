import re

with open("input.txt") as f:
    data = [re.sub(' +', ' ', x).strip().split(' ') for x in f.read().split('\n')]

operands = data[-1]
del data[-1]

def apply_operand(num1, num2, op):
    if op == '*':
        return num1*num2
    return num1+num2

output = [0 for _ in range(10000)]
for row in data:
    for idx, num in enumerate(row):
        if output[idx] == 0 and operands[idx] == '*':
            output[idx] = 1
        output[idx] = apply_operand(output[idx], int(num), operands[idx])

ans = 0
for out in output:
    if out == 0:
        break
    ans += out

print(ans)