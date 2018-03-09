import os, sys


MINUS_INF = (10 ** 10) * -1


# =======================================================================================
def max_cross_subarray(A, left, mid, right):
    zum, left_sum, left_max = 0, MINUS_INF, 0
    for i in range(mid, left-1, -1):
        zum += A[i]
        if zum > left_sum:
            left_sum = zum
            left_max = i
    zum, right_sum, right_max = 0, MINUS_INF, 0
    for j in range(mid+1, right+1):
        zum += A[j]
        if zum > right_sum:
            right_sum = zum
            right_max = j    
    return (left_max, right_max, (left_sum + right_sum))


# =======================================================================================
def max_subarray(A):
    def recursive_max_subarray(A, left, right):
        if left == right:
            return (left, right, A[left])
        else:
            mid = (left + right) // 2
            left_low, left_max, left_sum = recursive_max_subarray(A, left, mid)
            right_low, right_max, right_sum = recursive_max_subarray(A, mid + 1, right)
            cross_low, cross_max, cross_sum = max_cross_subarray(A, left, mid, right)
            if left_sum >= right_sum and left_sum >= cross_sum:
                return left_low, left_max, left_sum
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return right_low, right_max, right_sum
            else:
                return cross_low, cross_max, cross_sum    
    return recursive_max_subarray(A, 0, len(A) - 1)


R = ['ACT', 'AGT', 'CGT']

def find_genes(dna):
    found = set()
    array, coords, buff = [], [0], ''
    for cidx, c in enumerate(dna + 'XXX'):
        if len(buff) == 3:
            if buff in R:
                found.add(R.index(buff) + 1)
                array.append(3)
                coords.append(cidx)
                buff = c
            else:
                buff = buff[-2:] + c
                array.append(-1)
                coords.append(cidx)
        else:
            buff += c
    bounds = max_subarray(array)
    if sum(found) == 6:
        return dna[coords[bounds[0]] : coords[bounds[1]]+1]
    else:
        return ''



if __name__ == "__main__":
    #                 3 -1, 3, -1, -1, 3, -1, 3, 3
    print find_genes('ACTACGTTTAGTAACTCGTCT')
