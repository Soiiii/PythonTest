# 2의 영역
# 정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을
# return 하는 solution 함수를 완성해 주세요.
# 단, arr에 2가 없는 경우 [-1]을 return 합니다.

def solution(arr):
    answer = []
    result = []
    if 2 in arr:
        for a in range(len(arr)):
            if arr[a] == 2:
                answer.append(a)
        if len(answer) > 1:
            result = arr[answer[0]:answer[-1]+1]
        else:
            result.append(arr[answer[0]])
    else:
        result.append(-1)
    return result

# print(solution([1, 2, 1, 4, 5, 2, 9]))
# print(solution([1, 1, 1]))
print(solution([1, 2, 1, 2, 1, 10, 2, 1]))