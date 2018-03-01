
s = raw_input().strip()
n = int(raw_input().strip())

check = [False] + ([False] * (10 ** 7))
# check = [False] + ([False] * 10)

current_uniform = None
s = s + '0'
alphabet = "0abcdefghijklmnopqrstuvwxyz"
for i in range(len(s)-1):
    weight = alphabet.find(s[i])
    check[weight] = True
    if s[i] == s[i+1]:
        if current_uniform and s[i] in current_uniform:
            current_uniform += s[i]
            check[weight * len(current_uniform)] = True
        else:
            current_uniform = s[i]
    else:
        if current_uniform:
            current_uniform += s[i]
            check[weight * len(current_uniform)] = True
            current_uniform = None

for a0 in xrange(n):
    x = int(raw_input().strip())
    print 'Yes' if check[x] else 'No'
