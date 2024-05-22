# 행렬의 곱셈
#
# 2차원 행렬 arr1과 arr2를 입력받아,
# arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        lists = []
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer
