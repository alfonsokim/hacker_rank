== Rotaciones
def solution(A, K):
    # write your code in Python 3.6
    if K == 0 or len(A) == 0:
        return A
    rotations = K % len(A)
    # print(rotations)
    return A[-rotations:] + A[:-rotations]


### Max counters
def solution(N, A):
    # write your code in Python 3.6
    counters = [0] * N
    max_counter = 0
    for a in A:
        if a <= N:
            counters[a-1] += 1
            if counters[a-1] > max_counter:
                max_counter = counters[a-1]
        else:
            counters = [max_counter] * N
    return counters


### Nesting:
def solution(S):
    # write your code in Python 3.6
    stack = []
    for s in S:
        if s == '(':
            stack.append(s)
        if s == ')':
            if len(stack) == 0:
                return 0
            if stack.pop() != '(':
                return 0
    return 1 if len(stack) == 0 else 0


## Binary Gap
def solution(A):
    # write your code in Python 3.6
    
    if len(A) == 0:
        return 1
    if len(A) == 1:
        return 1 if A[0] == 2 else 2
    
    expected_sum = 0
    da_sum = 0
    for i in range(len(A)):
        expected_sum += (i + 1)
        da_sum += A[i]
    return (expected_sum + i + 2) - da_sum

# Balanced tape (83%)
def solution(A):
    min_diff = float('inf')
    lhs, rhs = 0, sum(A)
    for a in A:
        lhs += a
        rhs -= a
        diff = abs(lhs - rhs)
        if diff < min_diff:
            min_diff = diff
    return min_diff

# Dominator
def solution(A):
    # write your code in Python 3.6
    candidate_idx, count = 0, 0
    
    for i in range(len(A)):
        if count == 0:
            candidate_idx = i
            count += 1
        elif A[i] == A[candidate_idx]:
            count += 1
        else:
            count -= 1
    
    count = sum([1 if a == A[candidate_idx] else 0
                 for a in A])
    
    if count > len(A) // 2:
        return candidate_idx
    else:
        return -1


## Distinct (sorting)
def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 0
    A.sort()
    distinct = 1
    for i in range(len(A) - 1):
        if A[i] != A[i + 1]:
            distinct += 1
    return distinct


## brackets
def solution(S):
    # write your code in Python 3.6
    stack = []
    for s in S:
        if s in '{[(':
            stack.append(s)
        else:
            if len(stack) == 0:
                return 0
            c = stack.pop()
            if (c == '(' and s != ')') or (c == '[' and s != ']') or (c == '{' and s != '}'):
                return 0
    return 1 if len(stack) == 0 else 0


## Frog jump
def solution(X, Y, D):
    # write your code in Python 3.6
    diff = Y - X
    if diff <= 0:
        return 0
    jumps = diff / D 
    return int(jumps + (1 if diff % D > 0 else 0))