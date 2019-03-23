
def solution(S):
    # write your code in Python 2.7
    max_i, left, right = 0, 0, 0
    size = len(S)
    for i in range(size):
        left += 1 if S[i] == '(' else 0
        right += 1 if S[size-i-1] == ')' else 0
        # right += 1 if S[i] == ')' else 0
        print size-i-1, S[:i], S[i:], i, left, right
        if left == right:
            max_i = i
    assert max_i > 0
    return max_i




if __name__ == '__main__':
    print '*' * 10
    # print solution('(())')
    print solution('(())))(')
    # print solution('(())')
