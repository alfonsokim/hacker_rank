NR_POSSIBLE_ROLLS = 6
MIN_VALUE = -10000000001
 
def solution(A):
    # print(A)
    sub_solutions = [MIN_VALUE] * (len(A)+NR_POSSIBLE_ROLLS)
    # print(sub_solutions)
    sub_solutions[NR_POSSIBLE_ROLLS] = A[0]
    # print(sub_solutions)
     
    # iterate over all steps
    for idx in xrange(NR_POSSIBLE_ROLLS+1, len(A)+NR_POSSIBLE_ROLLS):
        print('idx: {}'.format(idx))
        max_previous = MIN_VALUE
        for previous_idx in xrange(NR_POSSIBLE_ROLLS):
            print('previous_idx:{}'.format(previous_idx))
            print('sub_solutions[idx-previous_idx-1]:{}'.format(sub_solutions[idx-previous_idx-1]))
            max_previous = max(max_previous, sub_solutions[idx-previous_idx-1])
            print('max_previous:{}'.format(max_previous))
            print('*' * 10)
        # the value for each iteration is the value at the A array plus the best value from which this index can be reached
        print('-' * 10)
        print('sub_solutions[idx]:{}'.format(sub_solutions[idx]))
        print('A[idx-NR_POSSIBLE_ROLLS]:{}'.format(A[idx-NR_POSSIBLE_ROLLS]))
        print('max_previous:{}'.format(max_previous))
        sub_solutions[idx] = A[idx-NR_POSSIBLE_ROLLS] + max_previous
        print('sub_solutions:{}'.format(sub_solutions))
     
    return sub_solutions[len(A)+NR_POSSIBLE_ROLLS-1]

if __name__ == '__main__':
    print solution([1, -2, 0, 9, -1, -2])