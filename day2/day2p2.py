
with open("input.txt") as f:
    data = [x.split('-') for x in f.read().split(',')]

to_check = [2,3,4,5,6,7]

#for e.g 12, check
#6-6
#2-2-2-2-2-2
#3-3-3-3
#4-4-4

def valid_digit(s):
    #print(f"checking s:{s}")
    slen = len(s)
    for num in to_check:
        #num = 2, quote = 6, want to check 6: :6
        #num = 3, quote = 4, want to check :4, 4:8, 8:12
        quot = slen//num
        if quot * num == slen:
            #evenly divisible
            substrings = []
            for i in range(0,slen,quot):
                substrings.append(s[i:i+quot])
            valid = all(x == substrings[0] for x in substrings)  
            if valid:
                return True

    #print(f"substr:  {substrings}")
    return False


tot = 0
for x in data:
    rang = range(int(x[0]),int(x[1])+1)
    for num in rang:
        if valid_digit(str(num)):
            #print(f"valid: {str(num)}")
            tot += num
    print('---')


print(tot)

