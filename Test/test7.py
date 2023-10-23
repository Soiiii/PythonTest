# flag에 따라 다른 값 반환하기
# 두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때,
# flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.

def solution(a, d, included):
    answer = 0
    number = 0
    for i in included:
        if 'True' in str(i):
            answer = answer + a + (d*(number))
        number += 1
    return answer

# 나은 답
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer