
MINUS_INF = (10 ** 10) * -1


# =======================================================================================
def max_cross_subarray(A, left, mid, right):
    """
    """
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
    """
    """
    def recursive_max_subarray(A, left, right):
        """
        """
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
    # --------------------------------------------------------------
    return recursive_max_subarray(A, 0, len(A) - 1)


# =======================================================================================
                  #  0   1    2   3   4    5    6   7   8   9  10  11   12  13  14 15
msa = max_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
print 'Max Subarray From %i to %i. Sum = %i' % (msa)


