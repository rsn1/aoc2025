with open("input.txt") as f:
    data = [x.split('-') for x in f.read().split(',')]

def valid_digit(s):
    slen = len(s)
    mid = slen//2
    return s[mid:] == s[:mid]

tot = 0
for x in data:
    rang = range(int(x[0]),int(x[1])+1)
    for num in rang:
        if valid_digit(str(num)):
            tot += num

print(tot)

