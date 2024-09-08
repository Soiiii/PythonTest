# 주식가격
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
#
# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.

def solution(prices):
    n = len(prices)
    answer = [0] * n  # 결과를 저장할 배열 (초기값은 0)
    stack = []  # 가격이 떨어지지 않은 시점들의 인덱스를 저장할 스택

    # 주식 가격을 한 번씩 탐색
    for i in range(n):
        # 스택에 저장된 인덱스 중 현재 가격보다 큰 경우를 처리
        while stack and prices[stack[-1]] > prices[i]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index  # 가격이 떨어지기 전까지의 시간을 기록
        stack.append(i)  # 현재 시점을 스택에 저장

    # 스택에 남아 있는 시점들은 끝까지 가격이 떨어지지 않은 경우
    while stack:
        prev_index = stack.pop()
        answer[prev_index] = n - 1 - prev_index  # 끝까지 유지된 시간을 계산

    return answer
