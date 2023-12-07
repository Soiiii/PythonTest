# Generating Minimum Value
#Suppose that there are arrays "A" and "B" that have the same length. Each array consists of natural numbers.
# Pick two numbers from array "A" and "B", one from each, and multiply them. Repeat this procedure for the whole array. The multiplied values are added accumulatively. The final goal is to minimize the accumulated value. (However, when the k-th number is chosen from each array, that number cannot be selected again.)
# For example, when "A" = [1, 4, 2] , "B" = [5, 4, 4],
# Pick the first number of "A" 1 and the first number of "B" 5, and multiply them. (accumulated value : 0 + 5(1x5) = 5)
# Pick the second number of "A" 4 and the third number of "B" 4, and multiply them. (accumulated value : 5 + 16(4x4) = 21)
# Pick the third number of "A" 2 and the second number of "B" 4, and multiply them. (accumulated value : 21 + 8(2x4) = 29)
# This case produces the minimum value, therefore return 29.
# Given arrays "A" and "B", write a function "solution" to return the minimum accumulated value.

import random

def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    print(A)
    B.sort()
    print(B)
    for i in range(len(A)):
        answer += A[i] * B[i]
    print(answer)
    return answer

solution([1, 4, 2],[5, 4, 4])