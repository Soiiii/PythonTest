# 소수찾기
#
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)
# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.


def solution(n):
    answer = 0
    for i in range(2, n+1):
        num = 0
        for j in range(2,i+1):
            if (i % j) == 0:
                break
            if num <= 2 and i != 1:
                print('i',i,'j',j,'num',num)
                answer += 1
    return answer