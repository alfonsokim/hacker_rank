
def solution(A):
    # write your code in Python 2.7
    """
    def base_minus_2(S):
        print 'base', S
        return sum(S[i] * (-2**i) for i in range(len(S)))
    A.insert(0, 1)
    X = [1, 0]
    inverse = True    
    for x in A[2:]:
        if x == 1:
            inverse = False        
        X.append(x if inverse else 1 if x else 0)
    print 'X', X
    print 'B', A
    print base_minus_2(X)
    print base_minus_2(A)
    return A
    """
    base_minus_2 = lambda S: sum(S[i] * (-2)**i for i in range(len(S)))
    print 'Original: %s = %i' % (str(A), base_minus_2(A))
    X = [A[0]]
    X += [0 if a else 1 for a in A[1:]]
    # X[0] = 0 if A[0] else 1
    print 'Nuevo: %s = %s' % (str(X), base_minus_2(X))

    A = [1,  0,  0,  1,  1]
    I = [0,  1,  2,  3,  4]
    M = [1, -2,  4, -8, 16]
    S = [1,  0,  0, -8, 16]  # 9

    A = [1,  1,  1,  0,  0]


if __name__ == '__main__':
    print solution([1, 0, 0, 1, 1])
