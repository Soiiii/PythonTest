# 수열과 구간 쿼리 2
# 정수 배열 numLog가 주어집니다.
# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.
# 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾습니다.
# 각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성해 주세요.
# 단, 특정 쿼리의 답이 존재하지 않으면 -1을 저장합니다.
# def solution(arr, queries):
#     answer = []
#     for i in range(len(queries)):
#         #queries[i][j] 저장할 필요없이 한 번에 가능
#         s,e,k = queries[i]
#         #무한대를 나타내는 부동 소수점 수
#         #inf는 무한대를 나타내며, float()는 부동소수점 수를 생성하는 함수다
#         #초기에 최솟값을 무한대로 설정하기 위해서 사용
#         min_value = float('inf')
#
#         for j in range(s, e+1):
#             if arr[j] > k and arr[j] < min_value:
#                 min_value = arr[j]
#         if min_value == float('inf'):
#             answer.append(-1)
#         else:
#             answer.append(min_value)

def solution(arr, queries):
    answer= []
    for query in queries:
        s,e,k = query
        temp_list = []
        for i in range(s, e+1):
            if arr[i] > k:
                temp_list.append(arr[i])
        try:
            answer.append(min(temp_list))
        except:
            answer.append(-1)
    return answer

# def solution(arr, queries):
#     answer = []
#     a=0
#     for i in range(len(queries)):
#         s = queries[i][0]
#         e = queries[i][1]
#         k = queries[i][2]
#         for j in range(s,e+1):
#             ii = arr[j]
#             if j+1 != e+1:
#                 jj = arr[j+1]
#             if ii < jj:
#                 ii = jj
#         if(ii == k):
#             ii = -1
#         else:
#             ii = arr[e]
#         answer.append(ii)
#         print(answer)
#     return answer

solution([0, 1, 2, 4, 3], [[0, 4, 2],[0, 3, 2],[0, 2, 2]])