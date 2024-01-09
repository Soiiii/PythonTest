# 2의 영역
# 정수 배열 arr가 주어집니다. 배열 안의 2가 모두
# 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.
# 단, arr에 2가 없는 경우 [-1]을 return 합니다.

def solution(arr):
    answer = []

    if 2 in arr:
        if arr.count(2) > 1:
            start = arr.index(2)
            end = len(arr) - arr[::-1].index(2)
            return arr[start:end]
        else:
            idx = arr.index(2)
            return [arr[idx]]
    else:
        return [-1]

    return answer