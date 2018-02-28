
def solution(A):
    # write your code in Python 2.7
    size = len(A)
    tail, head = 0, 0
    for i in range(len(A)):
        head += A[i]
        tail += A[len(A)-i-1]
        if head == tail:
            return i+1
    return -1


def solution2(A):
    from collections import defaultdict
    freqs = defaultdict(int)
    freqs[N//2]
    for a in A:
        freqs[a] += 1
    print max(freqs.values())


"""
  A[0] = 4
  A[1] = 2
  A[2] = 2
  A[3] = 3
  A[4] = 2
  A[5] = 4
  A[6] = 2
  A[7] = 2
  A[8] = 6
  A[9] = 4
"""
if __name__ == '__main__':
    # print solution([-1, 3, -4, 5, 1, -6, 2, 1])
    # print solution([])
    # print solution([2**20])
    # print solution([-2147483648, 2147483647])
    # print solution([2147483647, 0, 2147483647])
    # print solution(range(10000))
    # print solution(range(10000) + [0] + range(10000)) # 3.7s
    print solution2([4, 2, 2, 3, 2, 4, 2, 2, 6, 4])
