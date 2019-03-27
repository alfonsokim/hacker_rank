
memory = {}

def fibonnaci(n):
    if n < 2:
        return n
    if n in memory:
        return memory[n]
    n1 = fibonnaci(n-1)
    n2 = fibonnaci(n-2)
    memory[n] = n1 + n2
    return n1 + n2


sum_10 = sum([fibonnaci(i+1) for i in range(10)])
assert sum_10 == 143

i, result = 1, 0
while True:
    value = fibonnaci(i)
    if value < 40000000:
        result += value
        i += 1
    else:
        break

print result
