# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

#함수 사용
def factorial(i):
    #결과값으로 1을 먼저 선언
    result = 1
    #값이 1 이상이면 ! 이 계속 돌고 값이 0이면 1이 출력됨
    if i>0:
        result = i * factorial(i-1)
    return result

#입력값을 받음
i = int(input())
print(factorial(i))