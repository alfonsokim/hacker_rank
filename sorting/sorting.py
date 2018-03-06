
memory = {}
def is_sorted(numstrings):
    for i in range(len(numstrings) - 1):
        a, b = numstrings[i], numstrings[i+1]
        if len(a) > len(b):
            return False
        if len(a) == len(b):
            for j in range(len(a)-1, -1, -1):
                if a[j] > b[j]:
                    return False 
    return True

# =======================================================================================
def bigSorting(arr):
    current_digit = 1
    while not is_sorted(arr):
        print current_digit
        arr.sort(key=lambda v: v[current_digit * -1] if len(v) >= current_digit else '0')
        current_digit += 1
    return arr


# =======================================================================================
# print my_radix_sort(['31415926535897932384626433832795', '1', '3', '10', '3', '5'])
# print bigSorting(['31415926535897932384626433832795', '1', '3', '10', '3', '5'])

"""
from collections import defaultdict

n = int(raw_input().strip())
bucket = defaultdict(list)

for _ in xrange(n):
    number = raw_input().strip()
    bucket[len(number)].append(number)
    
for key in sorted(bucket):
    for value in sorted(bucket[key]):
        print(value)
"""

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print bigSorting(['0', '31415926535897932384626433832795', '777777777', '999999999999999999999', '888888888888', '777777777', '66666666', '55555555'])
    else:
        n = int(raw_input().strip())
        arr = []
        arr_i = 0
        for arr_i in xrange(n):
            arr_t = str(raw_input().strip())
            arr.append(arr_t)
        print 'len: %i' % len(arr)
        print 'max_len: %i' % max(map(len, arr))
        result = bigSorting(arr)
        print "\n".join(map(str, result))

