def miniMaxSum(arr):
    # Complete this function
    a_min, a_max = 10 ** 10 + 1, 0
    for skip in range(len(arr)):
        a_sum = sum([a for idx, a in enumerate(arr) if idx != skip])
        if a_sum > a_max:
            a_max = a_sum
        if a_sum < a_min:
            a_min = a_sum
    print '%i %i' % (a_min, a_max)


def timeConversion(s):
    # Complete this function
    suffix = s[-2:]
    hour, minute, second = int(s[0:2]), s[3:5], s[6:8]
    offset = 0
    if suffix == 'AM' and hour == 12:
        offset = -12
    if suffix == 'PM' and hour < 12:
        offset = 12
    return '%02d:%s:%s' % (hour + offset, minute, second)


def chiefHopper(arr):
    # Complete this function
    import math
    min_energy = 0
    for building_idx in range(len(arr)-1, -1, -1):
        building = int(arr[building_idx])
        if building > min_energy:
            min_energy += math.ceil((building - min_energy) / 2.0)
        elif building < min_energy:
            min_energy = math.ceil((building + min_energy) / 2.0)
    return int(min_energy)


def super_reduced_string(s):
    # Complete this function
    top, stack = -1, []
    for c in s:
        if top < 0 or stack[top] != c:
            stack.append(c)
            top += 1
        else:
            stack.pop()
            top -= 1
    return ''.join(stack) if len(stack) > 0 else 'Empty String'


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    n = len(password)
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    num, lower, upper, special = range(4)
    check = [0, 0, 0, 0]
    for c in password:
        if c in numbers:
            check[num] += 1
        if c in lower_case:
            check[lower] += 1
        if c in upper_case:
            check[upper] += 1
        if c in special_characters:
            check[special] += 1
    if n >= 6 and all(check):
        return 0
    missing = sum(map(lambda c: 1 if c == 0 else 0, check))
    if (n + missing) >= 6:
        return missing
    if missing + n >= 6:
        return missing
    return 6 - n


def twoCharaters(s):
    # Complete this function
    import itertools
    def test(a_str):
        pairs = set(a_str[::2])
        evens = set(a_str[1::2])
        return pairs != evens and len(pairs) == 1 and len(evens) == 1
    distinct, deleted = set(s), set()
    num_to_delete = len(distinct) - 2
    if test(s):
        return len(s)        
    if len(distinct) <= 2:
        return 0
    if num_to_delete < 0 or num_to_delete >= len(distinct):
        return 0
    max_len = 0
    for comb in itertools.combinations(list(distinct), num_to_delete):
        filtered = s
        for c in comb:
            filtered = filtered.replace(c, '')
        # print 'r:[%s] f:[%s]' % (''.join(comb), filtered)
        if test(filtered) and len(filtered) > max_len:
            max_len = len(filtered)
    return max_len


def caesarCipher(s, k):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = []
    while len(lower_case) < k:
        lower_case += lower_case
    while len(upper_case) < k:
        upper_case += upper_case
    lower_case += lower_case
    upper_case += upper_case
    for c in s:
        if c in lower_case:
            encrypted.append(lower_case[lower_case.find(c) + k])
        elif c in upper_case:
            encrypted.append(upper_case[upper_case.find(c) + k])            
        else:
            encrypted.append(c)
    return ''.join(encrypted)


def marsExploration(s):
    # Complete this function
    ok = 'SOS' * (len(s) / 3)
    return sum(map(lambda i: 1 if s[i] != ok[i] else 0, range(len(s))))


def hackerrankInString(s):
    # Complete this function
    letters = 'hackerrank'
    idx = 0
    for c in s:
        idx += 1 if c == letters[idx] else 0
        if idx == len(letters):
            return 'YES'
    return 'YES' if idx == len(letters) else 'NO'


def pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    for c in s.lower():
        if c in alphabet:
            alphabet.remove(c)
    not_str = '' if len(alphabet) == 0 else 'not '
    return '%spangram' % not_str


def weightedUniformStrings(s, w):
    weights = {}
    uniform = {}
    current_uniform = None
    s = s + '0'
    for i in range(len(s)-1):
        if s[i] == s[i+1]:  # uniform
            # print 'match with %s%s' % (s[i], s[i+1])
            if current_uniform and s[i] in current_uniform:
                current_uniform += s[i]
            else:
                current_uniform = s[i]
        else:
            # print 'no match with %s%s' % (s[i], s[i+1])
            if current_uniform:
                # print 'no match with CU[%s] %s%s' % (current_uniform, s[i], s[i+1])
                current_uniform += s[i]
                # print 'new CU: %s' % current_uniform
                uniform[s[i]] = len(current_uniform)
                current_uniform = None
            else:
                uniform[s[i]] = 1
    # print uniform
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter, lenghts in uniform.iteritems():
        for lenght in range(lenghts):
            weight = (lenght + 1) * (alphabet.find(letter) + 1)
            # print letter * (lenght + 1), weight
            weights[letter * (lenght + 1)] = weight
    # print weights
    weights_set = set(weights.values())
    return 'Yes' if w in weights_set else 'No'



# =======================================================================================
if __name__ == "__main__":
    print weightedUniformStrings('abccddde', 6)
    print weightedUniformStrings('abccddde', 1)
    print weightedUniformStrings('abccddde', 3)
    print weightedUniformStrings('abccddde', 12)
    print weightedUniformStrings('abccddde', 5)
    print weightedUniformStrings('abccddde', 9)
    print weightedUniformStrings('abccddde', 10)
    # arr = map(int, '256741038 623958417 467905213 714532089 938071625'.split(' '))  # 2063136757 2744467344
    # miniMaxSum(arr)
    # print timeConversion('12:00:00PM')
    # print super_reduced_string('abba')
    # print minimumNumber(11, 'Ab1')
    # print twoCharaters('aaaaa')  # 0
    # print twoCharaters('beabeefeab')
    # print twoCharaters('ab')
    # print twoCharaters('cobmjdczpffbxputsaqrwnfcweuothoygvlzugazulgjdbdbarnlffzpogdprjxvtvbmxjujeubiofecvmjmxvofejdvovtjulhhfyadr')
    # print twoCharaters('clmgakmobtdtdvqttrpgzkjmhcwnflzuazzobixbnyzxbgoszbneqfshlzqspjxtbxhyybxklcqiheeqmkjfpgcjzgzlsanhikvprhedxbvyyksppxkcywwobeakjuvmzzdjptjkzvvovbmakdhabbwrvnztzxoptsytwjgglfdgyhpffwrtqbjgcarmnmuvniwvozocwukpdmaktuqqsufxdqazjppqkolcxsjonluxkhqnwsyudlyvmtgblbzqmjifqpgibndldpdkdsqeesikxwmnrzepefbveihjeacodnljfxjdniribcumqrcnwexjbahwuct') # 0
    # print caesarCipher('middle-Outz', 2)  # 'okffng-Qwvb'
    # print caesarCipher('Zz', 1)
    # print caesarCipher('Zz-Aa', 100)
    # print marsExploration('SOSSQS')
    # print marsExploration('SOSSOS')
    # print marsExploration('SOSS1SS2SS3SS4SS5SS6SS7SS8SS9S')
    # print marsExploration('AAA')
    # print hackerrankInString('hereiamstackerrank')
    # print hackerrankInString('hackerworld')
    # for line in open('hackerrank_input.txt', 'r'):
    #     print hackerrankInString(line.strip())
    # print pangram('We promptly judged antique ivory buckles for the next prize')
    # print pangram('We promptly judged antique ivory buckles for the prize')
    # print pangram('')
    # print pangram('abcdefghijklmnopqrstuvwxyz')
