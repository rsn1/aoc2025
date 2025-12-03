with open("input.txt") as f:
    data = f.read().split('\n')

def get_first_highest_number(row):
    biggest_digit = max(row)
    index = row.index(biggest_digit)
    return biggest_digit, index

DIGITS=12
tot = 0

for row in data:
    output = ""
    rowcpy = row[:]
    for i in range(DIGITS):
        #first iteration, remove last 11 elements, second iteration remove last 10, etc
        elements_to_remove = DIGITS-1-i
        if elements_to_remove != 0:
            cur = rowcpy[:-elements_to_remove]
        else:
            cur = rowcpy
        #pick first highest number
        val, idx = get_first_highest_number(cur)
        output = output + val
        #consider rest of array after first highest number
        rowcpy = rowcpy[idx+1:]
    tot += int(output)

print(tot)
        
