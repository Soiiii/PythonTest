# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [i, j] 꼴입니다.
# 각 query마다 순서대로 arr[i]의 값과 arr[j]의 값을 서로 바꿉니다.
# 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.


def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        query = queries[i]
        a = query[0]
        b = query[1]
        originNum = arr[a]
        changeNum = arr[b]
        arr[b] = originNum
        arr[a] = changeNum
        answer = arr
    return answer
solution([0, 1, 2, 3, 4], [[0, 3],[1, 2],[1, 4]])

def solution2(arr, queries):
    for a,b in queries:
        print('a:', a, 'b:', b)
        arr[a],arr[b] = arr[b],arr[a]
solution2([0, 1, 2, 3, 4], [[0, 3,2],[1, 2,3],[1, 4,4]])
