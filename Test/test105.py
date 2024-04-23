# 같은 숫자는 싫어
#
# An array arr is given. Each element of arr is a number
# between 0 through 9. You want to remove all the duplicate numbers
# in the array arr except for only one. However, the order of each element
# in the array arr should be maintained. For example,
# When arr = [1, 1, 3, 3, 0, 1, 1], return [1, 3, 0, 1].
# When arr = [4, 4, 4, 3, 3], return [4, 3].
# Write a function solution to return the remaining numbers after removing
# the duplicate numbers in the array arr except only one.

def solution(arr):
    b = []
    for i in range(len(arr)):
        if i == 0:
            b.append(arr[i])
        elif arr[i] != arr[i-1]:
            b.append(arr[i])

    return b
