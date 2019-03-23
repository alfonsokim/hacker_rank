
from collections import defaultdict

def consecutive(array):
    seen = defaultdict(list)
    longest_len, longest = 0, []
    # for n in array:
    #     seen[n] = [n]
    for n in array:
        upper = seen[n+1]
        lower = seen[n-1]
        this = seen[n]
        if len(this) == 0:
            this.append(n)
        this.insert(0, n)
        this.append(n)
        seen[n+1] = this
        seen[n-1] = this
        seen[n] = this
        print 'n=%i, upper=%s, lower=%s, seen=%s' % (n, ', '.join(map(str, upper)), ', '.join(map(str, lower)), seen)
        if len(upper) > len(longest):
            longest = upper
        if len(lower) > len(longest):
            longest = lower
        if len(this) > len(this):
            longest = this
    print longest



print consecutive([1, 3, 2, 4, 5])
